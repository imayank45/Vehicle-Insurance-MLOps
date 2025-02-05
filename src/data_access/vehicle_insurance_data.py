import sys
import pandas as pd
import numpy as np
from typing import Optional
from src.configuration.mongo_db_connection import MongoDBClient
from src.constants import DATABASE_NAME
from src.exception import MyException

class VehicleInsuranceData:
    
    """
    Class to record export MongoDB records as a pandas dataframe.
    """
    
    def __init__(self) -> None:
        
        """
        Initialize MongoDB client
        """
        
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise MyException(e, sys)
        
    def export_collection_as_dataframe(self, collection_name:str, database_name: Optional[str]=None) -> pd.DataFrame:
        
        """
        Export MongoDB collection as a pandas dataframe.
        
        Parameters:
         - collection_name (str): Name of the MongoDB collection to be exported.
         - database_name (str, optional): Name of the MongoDB database. Defaults to DATABASE_NAME.
         
        Returns:
         - pd.DataFrame: Pandas dataframe containing the data from the MongoDB collection,
         '_id' column removed and 'na' values replaced with NaN.
        """
        
        try:
            
            # access specified collection from default or specified database
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
            
            # convert collection data to dataframe and preprocess
            print("Fetching data from MongoDB")
            
            df = pd.DataFrame(list(collection.find()))
            print(f"Data fetch with length; {len(df)}")
            
            if "id" in df.columns.to_list():
                df = df.drop(columns=["id"], axis=1)
                
            df.replace({"na":np.nan}, inplace=True)
            return df
        
        except Exception as e:
            raise MyException(e, sys)