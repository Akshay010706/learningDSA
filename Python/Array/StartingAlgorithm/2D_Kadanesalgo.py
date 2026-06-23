# 2D kadanes algorithm 
#Maximum Sum of rectangle in a matrix
# bruteforece - o(n**2)*o(n**2)*o(n**2)=o(n**6)
# 2d kadanes -- o(n)*o(n**2)= o(n**3)'1d kadanes * combination with every rows'

import sys

def kadanealgorithm(givennums):
    start = 0
    end =0
    
    currsum =0
    maxsum = -sys.maxsize-1
    
    
    n= len(givennums)
    
    while end<n:
        while currsum <0:
            currsum -= givennums[start]
            start += 1
        currsum += givennums[end]
        end += 1 
        
        maxsum = max(maxsum, currsum)
    return maxsum  


matrix =[[3,8,9,1,3],[-4,-1,1,7,-6],[-2,-3,8,1,-1]]
## ans =31


n = len(matrix)# number of rows 
m = len(matrix[0])# number of columns
ans = -sys.maxsize-1

print(matrix)

for i in range(m):
    temp=[]
    for j in range(n):
        temp.append(matrix[j][i])
    print(temp , f"for the {i} column")   
    # 1d kadanes algo
    ans = max(ans,kadanealgorithm(temp)) 
    print(ans)   
        
    for j in range(i+1,m):
        for k in range(n):
            temp[k]+=matrix[k][j]
        print(temp)    
        # 1d kadanes algo    
        ans = max(ans,kadanealgorithm(temp))
        print(ans)  
    print("-----------------------------")    
        
print(ans,' is the final answer')        
        