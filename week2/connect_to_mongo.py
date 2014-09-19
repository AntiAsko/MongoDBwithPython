import pymongo
import sys

# MongoClient mongo = new MongoClient("mongodb://localhost")
connection = pymongo.MongoClient("mongodb://localhost", 27017)

db = connection.test
names = db.names


def find():

    print "find a name"

    query = {'name ': 'anti'}

    try:
        doc = names.find_one(query)

    except:
        print "Error:", sys.exc_info()[0]

    print doc


find()
