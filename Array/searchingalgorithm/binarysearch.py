# used in sorted array 
def binarysearch(nums,target,mid):
    n=  len(nums)
    start = 0 
    last = n-1
    if start-last<=1:
        if nums[start]==target:
            return start
        else:
            return last
    mid = (start+last)//2
    if nums[mid]==target:
        return mid
    elif nums[mid]>target:
        binarysearch(nums,target,last)
    else:
        binarysearch(nums,target,start)
            
        