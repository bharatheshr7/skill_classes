class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def get_age(self):
         return self.__age  
p1=Person("bharathesh",20)
print(p1.name)
print(p1.get_age())      
        