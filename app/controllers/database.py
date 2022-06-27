from config import CONNECT_DB
import pymongo 

connect = pymongo.MongoClient(CONNECT_DB)

dbs = connect.list_database_names()

def users_table():
    users = connect["project"]["users"]
    return users

def rockets_table():
    rockets = connect["project"]["rockets"]
    return rockets
    
def quotations_table():
    quotation = connect["project"]["quotations"]
    return quotation

contents = [{
  "name": "Atlas Rocket 01",
  "quest": "viagem para mercurio",
  "active": 0,
  "engine": "ionico",
  "value": 8547190
},{
  "name": "Atlas Rocket 02",
  "quest": "Ida sem volta",
  "active": 1,
  "engine": "quimco",
  "value": 70000000
},{
  "name": "Atlas Rocket 03",
  "quest": "viagem para marte",
  "active": 1,
  "engine": "terminco",
  "value": 64070000
},{
  "name": "Atlas Rocket 04",
  "quest": "viagem para plutão",
  "active": 0,
  "engine": "terminco",
  "value": 61856645
}]

v = False

for db in dbs:
    if db == "project":
        v = True
        break


if not v:
    for content in contents:
        rockets_table().insert_one(content)
            
