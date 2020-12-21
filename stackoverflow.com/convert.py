import xmltodict
from pymongo import MongoClient
import sys

def part():
    print("------------------------------------------------")

try: 
    conn = MongoClient() 
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB") 
  
#Creates a connection to a MongoDB instance and returns the reference to the database.
db = conn.database

print(db)




def get_collection_name(path):
    # slash_there=False
    pos=-1
    for i in range(0,len(path)):
        if path[i]=='/':
            pos=i
    if pos==-1:
        return path[:-4]
    else:
        return path[pos+1:-4]





def insert_from_xml_path(path_to_file):
    coll_name=get_collection_name(path_to_file)
    print(coll_name)
    #return
    # Created or Switched to collection names: 
    with open(path_to_file) as xml_file:
        a = xmltodict.parse(xml_file.read())
    collection = db[coll_name]

    # Insert Data 
    rec_id1 = collection.insert_one(a) 
    
    print("Data inserted with record ids",rec_id1) 
    part()
    # Printing the data inserted 
    cursor = collection.find() 
    for record in cursor: 
        print(record) 
    part()
    part()


# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)

if n<=1:
    print("Error: Enter positive number of args")
    sys.exit()
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])
 
print("\nArguments passed:", end = "\n--------------------\n")
for i in range(1, n):
    print(f"{i}->",sys.argv[i], end = "\n")
    insert_from_xml_path(sys.argv[i])
     


