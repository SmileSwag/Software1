class Cat:
    def __init__(self, name):
        self.name=name
        
class CatCafe(Cat):

    def __init__(self):
        self.cats=[]
    def add_cat(self,cat):
        self.cats.append(cat)
    def list_cats(self):
        for i in self.cats:
            print(i)
cafe = CatCafe()
cafe.add_cat(Cat("Veikko"))
cafe.add_cat(Cat("Vito"))

print(cafe.cats[0].name)
print(cafe.cats[1].name)



class Engine:
    def __init__(self, horsepower, engine_type="Fuel"):
        self.horsepower=horsepower
        self.engine_type=engine_type
class Vehicle(Engine):
    def __init__(self, make, model,year,engine):
        self.make=make
        self.model=model
        self.year=year
        self.engine=engine

    def start(self):
        print(f"{self.make} {self.model} ({self.year}) with {self.engine.engine_type} engine is starting.")
    def stop(self):
        print(f"{self.make} {self.model} ({self.year}) with {self.engine.engine_type} engine is stopping.")
engine1= Engine(123)

engine2= Engine(400,"Hybrid")
car1= Vehicle("VW", "Pascal", 2013 , engine1)
car2= Vehicle("Volvo", "XC19", 2022 , engine2)
car1.start()
car1.stop()
car2.start()
car2.stop()


