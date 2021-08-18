import pymongo
import pprint

connection = pymongo.MongoClient("class-mongodb.cims.nyu.edu",27017,username="cgb355",password="o8a95SrJ",authSource="cgb355")
db = connection["cgb355"]

# docs = collection.aggregate(
#     [
#         {
#         "$project": {
#             "_id":0,
#             "neighbourhood_group_cleansed":1,
#             "name":1,
#             "beds":1,
#             "review_scores_rating":1,
#             "price":1
#             }
#         },
#         {
#         "$match": 
#             {"$and": [
#                 {"beds":{"$gt":2}},
#                 {"neighbourhood_group_cleansed":"Centro"},
#                 {"review_scores_rating": {"$nin": ["NULL"]}}
#                 ]
#         }
#     },
#         {
#         "$sort":
#             {"review_scores_rating":-1}}
#     ])

docs = db.examreview.find({
    "$or": [
        {
            "price": {
                "$gte":2,
            },
        },
        {
            "edition": "Penguin",
        }
    ]
    })

for doc in docs:
    pprint.pprint(doc)

