#Kadane Algorithm

#leetcode 53
#given an integer array nums , find the subarray with rthe largeset sum, and return its sum

#Method 1


def maxsubarray(nums):
    cs =nums[0]
    ls = nums[0]
    for i in range(1,len(nums)):
        if cs+nums[i]>nums[i]:
            cs=cs+nums[i]
        else:
            cs = nums[i]
        ls=max(ls,cs)
    return ls
    
nums=[4,3,-2,6,-14,7,-1,4,5,7,-10,2]

print(maxsubarray(nums))    


#method 2


def max_subarray(nums):
    maxsum = nums[0]
    currentsum = nums[0]
    for num in nums[1:]:
        currentsum = max(num,currentsum+num)
        maxsum = max(currentsum,maxsum)
    return maxsum


nums=[4,3,-2,6,-14,7,-1,4,5,7,-10,2]

print(max_subarray(nums))      