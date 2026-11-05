class stack:
    def __init__(self):
     self.stack=[]
     
     
    def product_push(self,element):
     self.stack.append(element)
     
    def isEmpty(self):
     return len(self.stack)==0
    def product_pop(self):
        if self.isEmpty():
            return"stack is empty"
        return self.stack.pop()
    def product_peek(self):
            if self.isEmpty():
                return"stack is empty"
            return self.stack.pop(-1)
    def product_size(self):
            return len(self.stack)
my_stack=stack()
my_stack.product_push("product 1")
my_stack.product_push("product 2")
my_stack.product_push("product 3")
print("popped: ",my_stack.product_pop())
print("peeked: ",my_stack.product_peek())
print("remaining ele in stack : ",my_stack.stack)




cmd=int(input("enter ur comd"))
match cmd:
    case 1:
         print("Elements present",my_stack.stack)
    case 2:
        a=input("Eter ele to push")
        my_stack.product_push(a)
        print(my_stack.stack)
    case 3:
        print("popped elements",my_stack.product_pop())
    case 4:
        print("peeked: ",my_stack.product_peek())
    case 5:
        print("empty",my_stack.isEmpty())
    case 6:
        print("remaining ele in stack ",my_stack.stack)




#Q......................................................................................................



        