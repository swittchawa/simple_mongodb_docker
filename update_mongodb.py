import pymongo

# Connect to mongodb
myclient = pymongo.MongoClient("mongodb://localhost:27017/", username='root', password='example')

mydb = myclient["test"] # Select the databse
mycol = mydb["testcol"] # Select the collection

# Add more attributes to a document
def add_more_to_document():
    myquery = {"Customer_id": "A85123"}
    newvalues = {"$set": {"Name": "Switt"}}

    x = mycol.update_one(myquery, newvalues)

    for x in mycol.find(myquery):
        print(x)

# add_more_to_document()

# Change attributes of a document
def update_document():
    myquery = {"Customer_id": "A85123"}
    newvalues = {"$set": {"Name": "Switt Chawa"}}

    x = mycol.update_many(myquery, newvalues)

    for x in mycol.find():
        print(x)

update_document()