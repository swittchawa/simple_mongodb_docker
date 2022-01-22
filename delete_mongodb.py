import pymongo

# Connect to mongodb
myclient = pymongo.MongoClient("mongodb://localhost:27017/", username='root', password='example')

mydb = myclient["test"] # Select the databse
mycol = mydb["testcol"] # Select the collection

# Function to delete a single document
def delete_single():
    # find the document
    mydict = {"Customer_id": "A85123"}

    # delete one document to the collection, if there are multiple ones it only delete one
    x = mycol.delete_one(mydict)

    # this is the id field of the new document
    print(x.deleted_count, "deleted")

# delete single document
delete_single()