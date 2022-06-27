from app.controllers.database import users_table, rockets_table, quotations_table
from app.models.model import Rocket

users = users_table()
rockets_list = rockets_table()
quotations_list = quotations_table()

def dbfind(name):
    v = False
    if users.find_one({"name":name}):
        v = users.find_one({"name":name})
    return v

def dbinsert(cad):
        users.insert_one(cad)

def rkfind(name = None):
    if name:
        return rockets_list.find_one({"name":name})
    return rockets_list.find({})

def rockets(name = None):
    rockets = []
    if name:
        rocket = rkfind(name)
        return Rocket(image(rocket["name"]),rocket["name"],rocket["engine"],rocket["value"],rocket["active"],rocket["quest"])
    for rocket in rkfind():
        rocket = Rocket(image(rocket["name"]),rocket["name"],rocket["engine"],rocket["value"],rocket["active"],rocket["quest"])
        rockets.append(rocket)
    return rockets
    
def quotations(quote = None):
    if quote:
        return quotations_list.find_one({"image":f"assets/{quote}.png"})
    return quotations_list.find({})

def insertquotes(content):
    quotations_list.insert_one(content)

def updatequote(quote, newdate, newporcent):
    print("COMO ESTA >> ", quotations(quote))
    if quotations(quote):
        quot = quotations(quote)
        id_obj = quot['_id']
        quot["date"] = newdate
        quot["porcent"] = newporcent
        print("COMO FICA >>> ",quot)
        quotations_list.update_one({"_id":id_obj},{"$set":quot})

def image(name):
    return f'assets/{name}.png'