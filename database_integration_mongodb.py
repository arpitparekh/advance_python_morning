from pymongo import *

# pip install pymongo

client = MongoClient("mongodb://localhost:27017/")

# check connection
print(client.list_database_names())

# create database
db = client['python_morning_virat']

# create collection
col = db['student']

dic = {
    "name": "Virat",
    "age": 30,
    "city": "Delhi"
}

# insert data into collection
# col.insert_one(dic)

# display data
data =  col.find()
for i in data:
    print(i)

