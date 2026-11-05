def insertion_sort(arr):
    for i in range(1, len(arr)):
        key=arr[i]
        j=i-1
        
        
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
            
            
        arr[j+1]=key
            
    return arr
# numbers=list(map(str,input("enetr a list of numbers ").split()))        
# print("orginal arrys ",numbers)
# sorted_numbers=insertion_sort(numbers)
# print("sorted number ", sorted_numbers)
 
 
 
 #binary search
def binary_search(arr,target):
     left=0
     right=len(arr)-1
     
     while left<=right:
      mid=(left+right)//2
        
        
     if arr[mid]==target:
         return mid 
     elif arr[mid]<target:
         left=mid+1
       
     else:
        right=mid+1
     return -1   
number=list(map(int,input("enter the list of number").split())) 
sorted_numbers=insertion_sort(number)
print("sorted number",sorted_numbers)
target=int(input("enetr the number to search"))
result=binary_search(number,target)
if result !=-1:
    print(f"number{target}found at index {result}")
else:
    print(f"number{target}not  found  in the list") 
    