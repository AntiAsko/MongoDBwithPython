import pymongo
import sys

#connect to mongo with port
connection = pymongo.MongoClient("mongodb://localhost", 27017)

#select database and document
db = connection.reddit
stories = db.stories


def find():

    print "find reddit titles for Google\n"

    query = {'title': {'$regex': 'Google'}}
    projection = {'title': 1, '_id': 0}

    try:
        iter = stories.find(query, projection)

    except:
        print "Error:", sys.exc_info()[0]

    sanity = 0
    for doc in iter:
        print doc
    sanity += 1


def findWithInput():

    print "\nfind reddit titles for my Input\n"

    tit = raw_input("Give a title:")

    query = {'title': {'$regex': tit}}
    projection = {'title': 1, '_id': 0}

    try:
        iter = stories.find(query, projection)
        #sorting and limiting the results of query
        iter = iter.sort('title', pymongo.ASCENDING).limit(1)
    except:
        print "Error:", sys.exc_info()[0]
    sanity = 0
    print "\n"
    for doc in iter:
        print doc
    sanity += 1

find()
findWithInput()
