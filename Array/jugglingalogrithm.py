# Juggling algorithm

# Q --- [1,2,3,4,5]
# d times right rotation
# 1 time - [5,1,2,3,4]
# 2 time - [4,5,1,2,3]

# M1. dublicate list 
# time - o(n) space -o(n)
#m2 - repeated rotation 
# time o(n*d)  space - o(n)
#m3 - juggling algo -- time -o(n)   space-o(1)

#Juggling algorithm 
# swapping in cycled 
# gcd(n,d%n)

import math

def rotate(arr,d):
    n = len(arr)
    gcdval = math.gcd(n,d%n)
    for i in range(gcdval):
        temp = arr[i]
        j=i
        while True:
            k = (j-d)%n
            if k == i:
                break
            arr[j] = arr[k]
            j=k
            
        arr[j] = temp
        
    return arr
   
arr = [1,2,3,4,5]
print(rotate(arr,2))     
        
    