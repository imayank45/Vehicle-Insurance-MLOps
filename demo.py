# from src.logger import configure_logger
# import logging

# # Ensure logging is configured
# configure_logger()

# logging.debug("This is a debug message.")
# logging.info("This is an info message.")
# logging.warning("This is a warning message.")
# logging.error("This is an error message.")
# logging.critical("This is a critical message.")


# below code is to check exception configuration
# from src.logger import logging
# from src.exception import MyException
# import sys

# try:
#     a = 1 + 'z'
# except Exception as e:
#     logging.info(e)
#     raise MyException(e, sys) from e


from src.pipline.training_pipeline import TrainPipeline

pipeline = TrainPipeline()
pipeline.run_pipeline()