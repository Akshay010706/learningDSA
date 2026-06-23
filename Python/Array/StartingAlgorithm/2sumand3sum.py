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

# givennums = [1,5,2,10,7]

# print(solve2sum(givennums,7))




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

        for i in range(n-3):
            while i>0 and nums[i]==nums[i+1]:
                continue
            for j in range(i+1, n-3):
                while j>i+1 and nums[j]==nums[j+1]:
                    continue
                finalt = target - nums[i] - nums[j]

                first, last = j+1, n

                while first < last:
                    total = nums[first] + nums[last]

                    if total == finalt:
                        ans.append([nums[i], nums[j], nums[first], nums[last]])
                        while first<last and nums[first]==nums[first+1]:
                            first+=1
                        while first<last and nums[last]==nums[last-1]:
                            last-=1
                        first+=1
                        last-=1        

                    elif total > finalt:
                        last -= 1

                    else:
                        first += 1
                        

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
                print(quad)
                print(f'{nums[i]} is appended')
                print("function call inside function")
                ksum(k-1,i+1,target-nums[i])
                print('----------------------------------------------------')
                a=quad.pop()
                print(f'{a} is poped')
                print("#####################################################")
            return 
        #base case , two sum 2
        l,r = start , len(nums)-1
        while l<r:
            if nums[l]+nums[r]<target:
                l+=1
            elif nums[l] +nums[r]>target:
                r-=1
            else:
                res.append(quad+[nums[l],nums[r]])
                print(res)
                l+=1
                while l<r and nums[l]==nums[l-1]:
                    l+=1
    ksum(4,0,target) 
    print("final result")  
    return res   

nums = [1,0,-1,0,-2,2]
print(four_sum(nums,0))                

 