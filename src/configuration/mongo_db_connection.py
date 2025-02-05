import os
import sys
import pymongo
import certifi
from src.exception import MyException
from src.logger import logging
from src.constants import  DATABASE_NAME, MONGODB_URL_KEY

# load certificate authority file to avoid timeout errors when connecting to MongoDB
ca = certifi.where()

class MongoDBClient:
    """
    MongoDBClient is responsible for establishing a connection to MongoDB database
    
    Attributes:
    
     - client: MongoClient
     A shared MongoClient instance for the class
     
     - database: Database
     The specified database instance that MongoDBClient is connected to
     
    Methods:
     - __init__(self, db_name: str):
     Initializes the MongoDB connecion with the given database name
    """
    
    client = None
    
    def __init__(self, database_name: str = DATABASE_NAME) -> None:
        """
        Initializes the MongoDB connection with the given database name.
        If no existing connection is found, it establish a new connection
        
        Parameters:
        
         - database_name: str, optional
         Name of the MongoDB database to connect to. Default is set by DATABASE_NAME constant.
         
        Raises:
        
         - MyException
         If there is an issue connecting to MongoDB or if the environment
         for the MongoDB URL is not set.
        
        """
        try:
            
            # check if MongoDB client connection is available, if not create connection
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                
                if mongo_db_url is None:
                    raise Exception(f"Environment variable '{MONGODB_URL_KEY}' not set")
                
                # establish a new MongoDB clinet connection
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
                
            # use the shared MongoDB client connection
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB client connection established")
            
        except Exception as e:
            
            # raise the custom exception with traceback details if connection fails
            raise MyException(e, sys)