class Rocket:
    def __init__(self, image, name, engine, value, active, quest):
        self.image = image
        self.name = name
        self.engine = engine
        self.value = value
        self.active = active
        self.quest = quest
    
    def __str__(self):
        return f'{"image":self.image,"name":self.name,"engine":self.engine, "value":self.value, "active":self.active,"quest":self.quest}'

class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{"name":self.name,"age":self.age}'

class Quote:
    def __init__(self,rocket, date, porcent):
        self.image = f'assets/{rocket["name"]}.png'
        self.rocket = rocket
        self.date = date
        self.porcent = porcent

    def gain(self, porcent):
        return self.rocket.value * ( self.porcent / 100 )

def __str__(self):
    return f'{"image":self.image,"name":self.name,"engine":self.engine, "value":self.gain, "date":self.date}'