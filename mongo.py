import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Database Name
db = client["mushin_aqua"]
  
# Collection Name
col = db["products"]
  
x = col.find_one()

for item in x:
    if(item=="part_name"):
        print(x[item])

