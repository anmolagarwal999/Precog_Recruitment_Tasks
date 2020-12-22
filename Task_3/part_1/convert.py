import camelot
import pandas as pd
from pymongo import MongoClient


def part():
    print("------------------------------------------------")


#######################################
curr_counter = 0
curr_collection_name = "collection_name_"
#########################################

try:
    conn = MongoClient()
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

# database
db = conn.database


def insert_data(data_obj):
    global curr_collection_name
    global curr_counter
    col_name = curr_collection_name + str(curr_counter)
    collection_obj = db[col_name]
    curr_counter += 1
    collection_obj.insert_many(data_obj)

    part()
    # Printing the data inserted
    cursor = collection_obj.find()
    for record in cursor:
        print(record)


##################################################
################################################################
####################################################

# ENTER path here instead
path_to_file = "./psp.pdf"
tables = camelot.read_pdf(path_to_file,
                          line_scale=20,
                          shif_text=[''],
                          strip_text='\n')
print(f"Path is {path_to_file} and number of tables found is {tables.n}")
# print(tables[0].df.columns)
# https://stackoverflow.com/a/52519002/6427607
# Setting 1st row as column names
# tables[0].df.rename(columns=tables[0].df.iloc[0])
# tables[0].df.drop(tables[0].df.index[0])
# print(tables[0].df.columns)
for j in range(0,tables.n):
    data_dict = tables[j].df.to_dict("records")
    # print(type(data_dict))
    # print(data_dict)
    for i in range(0, len(data_dict)):
        keys_values = data_dict[i].items()
        data_dict[i] = {str(key): value for key, value in keys_values}

    insert_data(data_dict)

############################################################3
