#important question

#1. 2-sum
# sum of two elements is equal to the target
# bruteforce -- 2 for loops--o(n**2)
#sortfist , then seleted first and last to get the target -- o(nlog(n) + n)==== o(nlog(n))

def solve2sum(givennums,target):
    temp = givennums.copy()
    n = len(givennums)
    givennums.sort()
    start = 0
    end = n-1
    while start<=end:
        currsum = givennums[start]+ givennums[end]
        if currsum == target:
            ans=[]
            for i in range(len(temp)):
                if givennums[start] == temp[i] or givennums[end]==temp[i]:
                    ans.append(i)
            return ans
            # return [givennums(start),givennums(end)]# this wil return indexes of the sorted array not the original array ,, hence instread of returning the indexes it is better to return values 
        
        if currsum>target:
            end-=1
        else:
            start+=1    
        
    return -1  

givennums = [1,5,2,10,7]

print(solve2sum(givennums,7))




# 3 - sum 
# sum of 3 element equal to target 
# bruteforce -- three loop -- o(n**3)
# optimize -- select one element then apply 2 sum for rest 2 element 
# that is sum of 2 element = target - selected element --- o(n**2)


def solve3sum(givennums,target):
    temp = givennums.copy()
    givennums.sort()
    for k in range(len(givennums)):
        temptarget = target
        temptarget -= givennums[k]
        start = k+1
        end = len(givennums)-1
        while start<=end:
            currsum = givennums[start]+ givennums[end]
            if currsum == temptarget:
                ans=[]
                
                
                for i in range(len(temp)):
                    if givennums[start] == temp[i] or givennums[end]==temp[i] or givennums[k]==temp[i]:
                        ans.append(i)
                return ans
            
            
            if currsum>target:
                end-=1
            else:
                start+=1    
            
    return -1  



# 4- sum 
# 18. 4Sums
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

# not a good solution (my solution )

def fourSum(nums, target):
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n):
            for j in range(i+1, n):
                finalt = target - nums[i] - nums[j]

                first, last = j+1, n-1

                while first < last:
                    total = nums[first] + nums[last]

                    if total == finalt:
                        ans.append([nums[i], nums[j], nums[first], nums[last]])
                        first += 1

                    elif total > finalt:
                        last -= 1

                    else:
                        first += 1
                        

        return ans  
    
    
    
    
    
    
# my approch in better way 
def fourSum(nums, target):
    nums.sort()
    n = len(nums)
    ans = []

    for i in range(n - 3):

        # skip duplicate i
        if i > 0 and nums[i] == nums[i-1]:
            continue

        # pruning
        if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
            break

        if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
            continue

        for j in range(i + 1, n - 2):

            # skip duplicate j
            if j > i + 1 and nums[j] == nums[j-1]:
                continue

            first = j + 1
            last = n - 1

            while first < last:
                total = nums[i] + nums[j] + nums[first] + nums[last]

                if total == target:
                    ans.append([nums[i], nums[j], nums[first], nums[last]])

                    # skip duplicate first
                    while first < last and nums[first] == nums[first+1]:
                        first += 1

                    # skip duplicate last
                    while first < last and nums[last] == nums[last-1]:
                        last -= 1

                    first += 1
                    last -= 1

                elif total < target:
                    first += 1

                else:
                    last -= 1

    return ans    
    
  
  
# neetcode general k sum approch     
def four_sum(nums,target):
    nums.sort()
    res,quad = [],[]
    
    def ksum(k,start,target):
        if k!=2:
            for i in range(start,len(nums)-k+1):
                if i>start and nums[i]==nums[i-1]:
                    continue
                quad.append(nums[i]) 
                ksum(k-1,i+1,target-nums[i])
                quad.pop()
            return 
        #base case , two sum 2
        l,r = start , len(nums)-1
        while l<r:
            if nums[l]+nums[r]<target:
                l+=1
            elif nums[l] +nums[r]>target:
                r-=1
            else:
                res.append(quad+nums[l],nums[r])
                l+=1
                while l<r and nums[l]==nums[l-1]:
                    l+=1
    ksum(4,0,target)   
    return res                    

 