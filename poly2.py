class Flight:
    def __init__(self ,brand,model):
        self.brand=brand
        self.model=model
    def fly(self):
        print("FLY")
f1=Flight("Kingfisher","123re") 
print(f1.brand)
print(f1.model)  
f1.fly()
for x in(f1):
 x.fly()
