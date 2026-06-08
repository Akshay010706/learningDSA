# Juggling algorithm

# Q --- [1,2,3,4,5]
# d times right rotation
# 1 time - [5,1,2,3,4]
# 2 time - [4,5,1,2,3]

# M1. dublicate list 
# time - o(n) space -o(n)
# def rotate(arr,d):
#     n= len(arr)
#     new = [0]*n
#     for i in range(n):
#         new[(i+d)%n] = arr[i]
#     return new    





#m2 - repeated rotation 
# time o(n*d)  space - o(n)
# def rotate(arr,d):
#     n = len(arr)
#     for j in range(d):
#         last = arr[-1]
    

#     for i in range(n-1,0,-1):
#         arr[i] = arr[i-1]

#     arr[0] = last
#     return arr





#m3 - juggling algo -- time -o(n)   space-o(1)

#Juggling algorithm
# swapping in cycled 
# gcd(n,d%n)
def gcd_val(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# def rotate(arr,d):
#     n = len(arr)
#     #number of cylcle is find by gcd
#     gcdval = gcd_val(n,d%n)
#     for i in range(gcdval):
#         temp = arr[i]
#         j=i
#         while True:
#             k = (j+d)%n# left rotation 
#             # for right rotation k = (j - d + n) % n 
#             #when one cycle is completed , we arrived at from where we started we break the loop
#             #0-2-4-0 break loop
#             if k == i:
#                 break
#             arr[j] = arr[k]
#             j=k
            
#         arr[j] = temp
        
#     return arr





arr = [1,2,3,4,5]
print(rotate(arr,2))     
        
    