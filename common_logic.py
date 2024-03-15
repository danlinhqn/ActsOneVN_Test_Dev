import json
import os
from data_global import *


# Check and add data to the database
def check_And_Append_Database(order_Data, database_File):
    try:
        
        # Read data from the database.json file
        with open(database_File, 'r', encoding='utf-8') as file:
            database = json.load(file)
    except FileNotFoundError:database = {}
        
    # Check if the data already exists in the database
    if order_Data not in database.values():
        
        # add new data to the database
        database[len(database) + 1] = order_Data
        
        # Write new data to the database.json file
        with open(database_File, 'w', encoding='utf-8') as file:

            # Use indent=4 to write data to the file in a beautiful format
            json.dump(database, file, indent=4) 

        # Order successful
        notify_For_Client.insert(0,1)
        print("Data imported successfully.")
    else:
        
        # Order failed
        notify_For_Client.insert(0,2)
        print("Data already exists in the database.")
