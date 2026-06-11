#238. Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


#M1 - we can make an array with all the element as multiplication all the element in nums and then divide the elemt in that specific index but that plan has a flow 
# we can do it if nums contains 0

def productExceptSelf(nums):
    r,l=1,1
    n = len(nums)
    answer = [1]*n
    for i in range(n):
        answer[i]*=r
        r*=nums[i]
    for j in range(n-1,-1,-1):
        answer[j]*=l
        l*=nums[j]
    return answer        
    
          
nums = [1,2,3,4]
print(productExceptSelf(nums))                      
    