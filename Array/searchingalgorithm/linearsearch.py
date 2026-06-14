# search linearly 

def binsearch(nums,target):
    found= False
    for i in nums:
        if i == target:
            found = True
            break
    if found==True:
        print(f"target num at index {i}")
    else:
        print('no')        
        
n= int(input())
nums = [int(ele) for ele in input().split()]
target = int(input()) 
binsearch(nums,target)       