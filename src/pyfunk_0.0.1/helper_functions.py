import pymongo
import pandas as pd

class HelperFunctions:
    '''
    This class is designed to allow users multiple useful functions to utilize beside
    their code. This class will be developed further in the future as we continue 
    to work on it. 
    '''
    def __init__(self):
        pass

    def to_mongo_collection_from_df(df: pd.DataFrame, connection_str: str, db_name: str, collection_name:str):
        '''
        Create a Mongo Collection from dataframe object.
        
        Input: 
        df = DataFrame object to upload to MongoDB
        connection_str = string used to connect Python to MongoDB instance.
        db_name = name of the database you would like to create or connect to
        collection_name = name of the collection you would like to create or connect to

        Process:
        * Create a client connection using provided MongoDB connection string
        * Instantiate/Connect to given database and collection names
        * Insert one function to MongoDB. Iterates through dataframe and uploads row by row each document.
        Output: 
        Message stating the upload has been completed and prompting users to check 
        their MDB database to ensure proper completion
        '''

        # Create client connection
        client = pymongo.MongoClient(connection_str)
        # Instantiate/Connect to listed database
        db = client[db_name]
        # Instantiate/Connect to listed collection
        collection = db[collection_name]

        # Upload dataframe object to collection
        for x in df.index:
            collection.insert_one(df.loc[x].to_dict())
        return "Mongo Collection has been successfully updated with your data"