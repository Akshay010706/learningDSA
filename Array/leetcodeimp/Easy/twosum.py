#[E] 1. Two Sum [Hash Map] - Complement lookup in O(N).
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#1. using hash map 
def twoSum( nums, target):
        d = {}
        for i, num in enumerate(nums): # enumerate keep track of both the current item and its index at the same time.
            complement = target - num
            if complement in d:
                return [d[complement], i]  
            d[num] = i
            
# M2 - sort --- but this will change the indexes

            
            
            