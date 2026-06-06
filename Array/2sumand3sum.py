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


def solve2sum(givennums,target):
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