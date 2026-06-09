#KMP algorithm
#Q- given two string a and b ? find if b is a substring of a
# ex- a= abefabcd  b=abc   yes b is a substring of a

#M1 - bruteforce  O(n*m)
# def kmpalog(a,b):
#     #range(len(a)-len(b)+1) cause loops think about it a = "abcdef"
#     # b = "abc"

#     # Can a match start at index 5?

#     # Why or why not?
#     for i in range(len(a)-len(b)):
#         mat_ched = True
    

#         for j in range(len(b)):
#             if a[i+j] != b[j]:
#                 #matched is false only for that iteration of i
#                 mat_ched = False
#                 break

#         if mat_ched:
#             return True
#     return False    






# M2 - kmp algo 
#lps (longest prefix string)
#Longest Proper Prefix which is also Suffix
#Why Are We Building This Array?
#"How many characters from the beginning are repeating at the end?"

# Proper Prefix

# Prefix means:

# Starts from beginning.

# For:

# abcd

# Prefixes:

# a
# ab
# abc
# abcd

# Proper prefix means:

# a
# ab
# abc

# Whole string not allowed.

# Suffix

# Ends at the end.

# For:

# abcd

# Suffixes:

# d
# cd
# bcd
# abcd

# Example

# String:

# abab

# Prefixes:

# a
# ab
# aba

# Suffixes:

# b
# ab
# bab

# Common:

# ab

# Length:

# 2


#---------------------------------------------------------------------------
# 2. WHAT DOES THE LPS ARRAY STORE?

# Suppose pattern is:

# ababaca

# LPS array will be:

# index : 0 1 2 3 4 5 6
# char  : a b a b a c a
# lps   : 0 0 1 2 3 0 1

# Let's understand ONE position.

# Index 4:

# ababa

# Question:

# What is longest prefix which is also suffix?

# Prefixes:

# a
# ab
# aba
# abab

# Suffixes:

# a
# ba
# aba
# baba

# Common:

# a
# aba

# Longest:

# aba

# Length:

# 3

# Therefore:

# lps[4] = 3


#-----------------------------------------------------------------------------------------------------------
# Why Are We Building This Array?

# This is the most important question.

# Suppose pattern:

# ababaca

# While matching, you've already matched:

# ababa

# Then suddenly mismatch occurs.

# A normal algorithm says:

# Start over.

# KMP says:

# No.
# I already know something useful.

# The LPS tells us:

# ababa

# has:

# prefix = suffix = aba

# Length = 3

# So instead of starting from zero:

# jump directly to length 3

# Huge time saving.


def computelps(str,lps):
    n = len(str)
    i = 1
    temp =0
    while i<n:
        if str[i]==str[temp]:
            temp+=1
            lps[i]=temp
            i+=1
        else:
            if temp!=0:
                temp = lps[temp-1]
            else:
                lps[i]=0
                i+=1


def KMP(a,b):
    n= len(a)
    m= len(b)
    lps = [0]*m
    computelps(b,lps)  
    i =0
    j=0
    while i<n:
        if a[i]==b[j]:
            i+=1
            j+=1
        if j ==m:
            print("b is a substring")
            return
        elif i<n and a[i]!=b[j]:
            if j!=0:
                j = lps[j-1]
            else:
                i+=1
                
    print("b is not a substr")                                          
                

a = "abefabcd"
b = "abciabs"
print(KMP(a,b))
