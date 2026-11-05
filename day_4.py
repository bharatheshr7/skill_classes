#DSA hash tableZ
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
# def binary_search(arr,target):
#      left=0
#      right=len(arr)-1
     
#      while left<=right:
#       mid=(left+right)//2
        
        
#       if arr[mid]==target:
#          return mid 
#       elif arr[mid]<target:
#          left=mid+1
       
#       else:
#          right=mid-1
# #      return -1   
# number=list(map(int,input("enter the list of number").split())) 
# sorted_numbers=insertion_sort(number)
# print("sorted number",sorted_numbers)
# target=int(input("enetr the number to search"))
# result=binary_search(sorted_numbers,target)
# if result !=-1:
#     print(f"number{target}found at index {result}")
# else:
#     print(f"number{target}not  found  in the list") 
    

    
        #binary search
def binarysearch(nums,target):
    n=len(nums)
    low=0
    high=n-1
    while low<=high:
        
       mid=(low+high)//2
       if nums[mid]==target:
        return mid
       elif nums[mid]<target:
        low=mid + 1
       else :
        high= mid- 1
    return -1
num=list(map(int,input("enter list of elements   ").split()))
sorted_form=insertion_sort(num)
print("sorted number",sorted_form)   
target=int(input("enter the target number"))       
result=binarysearch(sorted_form,target)
print("index",result)
if result==-1:
    print("sorry it dosent exsists")
    
          
    
     