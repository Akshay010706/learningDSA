#The Dutch National Flag (DNF) algorithm
#3 color -- 3 digits to work
# sort of 0s, 1s , 2s without a sorthing algorithm
# 00000111111222222
#      !  !  !      low , mid , high
""" mid =0
       swap(low,mid)
       mid +=1
       low+=1
    mid =1
       mid +=1
    mid =2
       swap(mid,high)   
       high -=1
"""


def swap(l,r,arr):
    arr[l],arr[r]=arr[r],arr[l]
    return arr



def dnfalgo(givennums):
    n= len(givennums)
    
    low =0 
    mid= 0
    high = n-1
    
    while mid<=high:
        if givennums[mid]==0:
            swap(low,mid,givennums)
            mid+=1
            low+=1
        elif givennums[mid] ==1:
            mid+=1
        else:
            swap(mid,high,givennums)
            high -=1
    return givennums                
            
nums=[0,1,2,2,1,2,0,2,0,0,1,2,0,0] 
print(dnfalgo(nums))    