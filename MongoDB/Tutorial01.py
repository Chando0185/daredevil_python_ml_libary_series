import pymongo

client=pymongo.MongoClient("mongodb://127.0.0.1:27017/")

mydb=client['Student']

collection = mydb.studentcollection

records  = [{
    'Name':'Chando Dhar',
    'ID':'19010116',
    'Department':'CSE'
}, 
{
    'Name':'Mishu Dhar',
    'ID':'19010116',
    'Department':'CSE'
},
{
    'Name':'Mishu Dhar Chando',
    'ID':'19010116',
    'Department':'CSE'
},
]

# collection.insert_one(records)
collection.insert_many(records)