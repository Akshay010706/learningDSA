#53. Maximum Subarray
#Given an integer array nums, find the subarray with the largest sum, and return its sum.


# M1 - brute force
# def maxSubArray(nums):
#     n= len(nums)
#     mx=0
#     for i in range(n):
#         sm = 0
#         for j in range(i,n):
#             sm += nums[j]
#             mx = max(mx,sm)
#     return mx



#M2 - optimizeed
def maxSubArray(nums):
    n= len(nums)
    mx,sm=nums[0],nums[0]
    for i in range(n):
        sm = max(nums[i],sm+nums[i])
        mx = max(mx,sm)
    return mx    


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))        
            