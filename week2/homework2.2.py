import pymongo

connection = pymongo.MongoClient("mongodb://localhost", 27017)
db = connection.students
grades = db.grades

iter = grades.aggregate([{'$match': {'type': 'homework'}}, {
                                        '$group': {'_id': '$student_id', 'minscore': {'$min': '$score'}}}])

sanity = 0
for doc in iter['result']:
    res = grades.remove(
        {'student_id': doc['_id'], 'type': 'homework', 'score': doc['minscore']})
    print(res)
