import pymongo
import sys
import datetime

connection = pymongo.MongoClient("mongodb://localhost", 27017)

db = connection.test
names = db.names


def using_save():
    try:
        name = names.find_one()
        print "before:", name

        # add a new field
        name['date'] = datetime.datetime.utcnow()

        names.save(name)
        name = names.find_one()
        print "after:", name

    except:
        print "Error", sys.exc_info()[0]
        raise


def using_update():
    try:
        name = names.find_one()
        print "before:", name

        # add a new field
        name['date'] = datetime.datetime.utcnow()

        names.update({'name': 'anti'}, name)
        name = names.find_one()
        print "after:", name

    except:
        print "Error", sys.exc_info()[0]
        raise


def using_set():
    try:
        name = names.find_one()
        print "before:", name

        names.update(
            {'name': 'anti'}, {'$set': {'date': datetime.datetime.utcnow()}})
        name = names.find_one()
        print "after:", name

    except:
        print "Error", sys.exc_info()[0]
        raise


using_set()