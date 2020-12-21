import xmltodict

# a=xmltodict.parse(GzipFile("Badges2.xml"))

# print(a)

with open("Badges2.xml") as xml_file:
    a = xmltodict.parse(xml_file.read())
    # pass

xml_file.close()
print(a)

# Python code to illustrate 
# inserting data in MongoDB 
from pymongo import MongoClient 
def part():
    print("------------------------------------------------")
try: 
    conn = MongoClient() 
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB") 
  
# database 
#Creates a connection to a MongoDB instance and returns the reference to the database.
db = conn.database

print(db)

# Created or Switched to collection names: 
collection = db.badges_2

# Insert Data 
rec_id1 = collection.insert_one(a) 
  
print("Data inserted with record ids",rec_id1) 
part()
# Printing the data inserted 
cursor = collection.find() 
for record in cursor: 
    print(record) 