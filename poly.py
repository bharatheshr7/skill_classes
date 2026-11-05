class Car:
    def __init__(self ,brand,model):
        self.brand=brand
        self.model=model
    def hey(self):
        print("drive")
car1=Car("BMW","M5") 
print(car1.brand)
print(car1.model)  
#print(Car.l)     
car1.hey()
