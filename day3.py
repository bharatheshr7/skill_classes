# queue=[]
# queue.append('A')
# queue.append('B')
# print("queue:",queue)
# #peek
# frontElement=queue[0]
# print("peek:",frontElement)
# # deq
# pop=queue.pop(0)
# print("dequeue",pop)
# print("elements after dequeue",queue)
# #is empt
# isEmpty=not bool(queue)
# print("is it empty ?",isEmpty)
# #size
# size=len(queue)
# print("size",size)

# cmd=int(input("enter ur cmd"))
# match cmd:
#   case 1:
      

# class Node :
#   def __init__(self,data):
#     self.data=data
#     self.next=None
# def Traversandprint(head):
#   curr=head
#   while curr:
#     print(curr.data,end="-->")
#     curr=curr.next
#   print("null")

# node1=Node(7)      
# node2=Node(11)      
# node3=Node(2)      
# node4=Node(4)      
# node5=Node(5)      
# node6=Node(3)      



# node1.next=node2
# node2.next=node3
# node3.next=node4
# node4.next=node5 
  
# node5.next=node6



# Traversandprint(node2)







#doubly linked list

# class Node:
#   def __init__(self,data):
#     self.data=data
#     self.next=None
#     self.prev=None



# def traverse(head):
#  curr=head 
#  while curr:
#     print(curr.data,end="-->")
#     curr=curr.next
#     print("null")
# def insertAtHead(head,data):
#   newNode=Node(data)
#   newNode.next=head
#   if head:
#     head.prev=newNode
#   head=newNode
#   return head


# head=None
# head=insertAtHead(head,1)  
# head=insertAtHead(head,2)  
# head=insertAtHead(head,3)  
# traverse(head)
# print("head:",head.data)



#circular linked list

class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
    self.prev=None
    
    
class CircularLinkedList:
  def __init__(self):
    self.head=None
    self.tail=None

  def insertAtHead(self,data):
    newNode=Node(data)
    if not self.head:
      self.head=newNode
      self.tail=newNode
      newNode.next=newNode
      newNode.prev=newNode
    else:
      newNode.next=self.head
      newNode.prev=self.tail
      self.head.prev=newNode
      self.tail.next=newNode
      self.head=newNode

  def traverse(self):
    if not self.head:
      print("List is empty")
      return
    curr=self.head
    while True:
      print(curr.data,end="-->")
      curr=curr.next
      if curr==self.head:
        break
    print("null")    
    print("head:",self.head.data)
    print("tail:",self.tail.data)
    print("head prev:",self.head.prev.data)
    print("tail next:",self.tail.next.data)
    print("tail prev:",self.tail.prev.data)
    print("head next:",self.head.next.data)
cll=CircularLinkedList()
cll.traverse()