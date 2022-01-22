import pymongo

# Connect to mongodb
myclient = pymongo.MongoClient("mongodb://localhost:27017/", username='root', password='example')

mydb = myclient["test"] # Select the databse
mycol = mydb["testcol"] # Select the collection

# Function to insert single document
def insert_single():
    # create a dummy document
    mydict = {"Customer_id": "A85123", "Country": "UK"}

    # Write the document to the collection
    x = mycol.insert_one(mydict)

    # this is the id field of the new document
    print(x.inserted_id)


# insert single document
#insert_single()


def insert_multiple():
    # create a dummy document
    mylist = []

    mylist.append({ "Customer_id": "B85123", "Country": "DE"})
    mylist.append({ "Customer_id": "C85123", "Country": "US"})

    # Write the documents to the collection
    x = mycol.insert_many(mylist)

    # This is the id field of the new documents
    print(x.inserted_ids)

insert_multiple()
