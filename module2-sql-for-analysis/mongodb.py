"""
Exploring Mongodb
Both Elephantsql and mongodb require a username and password connection and
specific lines of code that connect information back and forth. I don't think
one type is easier than the other yet since I have not worked extensively
with either db. Mongo is for documents while sql seems more dataframe focused
but its hard to tell the difference at this point.
"""
# must whitelable the ip address
# #ipecho.net gives local comp ip
# #!curl ipecho.net/plain in colab
#
# michhottinger
# Utb7WKiR$c+z@k_

import pymongo
import urllib.parse

user = "michhottinger"
pw = "Utb7WKiR$c+z@k_"
client = pymongo.MongoClient("mongodb://" + user + ":" + urllib.parse.quote_plus(pw) + "@cluster0-shard-00-00-vlelc.mongodb.net:27017,cluster0-shard-00-01-vlelc.mongodb.net:27017,cluster0-shard-00-02-vlelc.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test
#client.nodes
#help(db)
#insert a document
db.test.insert_one({'x':1})
#count how many documents
print(db.test.count_documents({'x':1}))

#looking for a document
db.test.find({'x':1})

curs = db.test.find({'x':1})

#create some docs for testing
stephanie_doc = {
    'favorite animal': 'alpaca',
    'favorite color': 'blue'
}

zoli_michelle_doc = {
    'favorite animal': ['Black Panther', 'Unicorn']
}

dorothy_doc = {
    'favorite animal': 'dog'
}

db.test.insert_many([stephanie_doc, zoli_michelle_doc, dorothy_doc])
#look at the docs
list(db.test.find())

#make more

more_docs = []
for i in range(10):
    doc = {'even': i % 2 ==0}
    doc['value'] = i
    more_docs.append(doc)

more_docs

db.test.insert_many(more_docs)

list(db.test.find({'even':False}))

db.test.update_one({'value':3},
                   {'$inc': {'value':5}})

list(db.test.find())

db.test.delete_many({'even':False})

list(db.test.find())

db.test.update_many({'value':3},
                   {'$inc': {'value':100}})

rpg_character = (1, "King Bob", 10, 3, 0, 0, 0)
#you would get error if you did db.test.insert_one(rpg_character)
#here to cast a dict
db.test.insert_one({'rpg_character': rpg_character})
#this will insert

db.test.insert_one({
    'sql_id': rpg_character[0],
    'name': rpg_character[1],
    'hp': rpg_character[2],
    'level': rpg_character[3]
})

list(db.test.find())
