class Animal:
    def __init__(self,name):
        self.name=name
    def info(self):
        print("Animal name : ",self.name)  
class Dog(Animal):
        def sound(self):
            print(self.name,"Barks")
d=Dog("Tommy")
d.info()             
d.sound()
class Lion(Animal):
    def sound(self):
        print(self.name,"roars")
l=Lion("cmha")
l.info()             
l.sound()        