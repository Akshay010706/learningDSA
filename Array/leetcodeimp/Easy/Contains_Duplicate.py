#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#m1 - using sets
# def containsDuplicate(nums):
    
#     l1 = len(nums)
#     l2 = len(set(nums))
#     if l1 == l2:
#         return False
#     return True

#using hash set 
def containsDuplicate(nums):
    fre ={}
    for num in nums:
        if num in fre:
            return True
        else:
            fre[num]=1
    return False        

nums = [1,2,3,1]
print(containsDuplicate(nums))