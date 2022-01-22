import pymongo

# Connect to mongodb
myclient = pymongo.MongoClient("mongodb://localhost:27017/", username='root', password='example')

mydb = myclient["test"] # Select the databse
mycol = mydb["testcol"] # Select the collection

# Find these documents where the customer_id equals to A85123
myquerry = {"Customer_id": "A85123"}
mydoc = mycol.find(myquerry)

# Return only specific parts of the document
# myreturnonly = { "_id": 0, "Customer_id": 1}
# mydoc = mycol.find(myquery, myreturnonly)

# Print out document
for x in mydoc:
    print(x)

# how to sort the data that you will retrieve
# find order ASC .sort("Cusomter_id") or .sort("Cusomter_id", 1)
# find order DSC .sort("Cusomter_id",-1)  