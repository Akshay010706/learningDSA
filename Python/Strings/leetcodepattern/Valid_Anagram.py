#242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

def isAnagram(s, t):
        l = {}
        d = {}
        if len(s)!=len(t):
            return False
        for i in s:
            if i in l:
                l[i]+=1
            else:
                l[i]=1
        for i in t:
            if i in d:
                d[i]+=1
            else:
                d[i]=1 
        for i in l:
            if i not in d:
                return False
            elif l[i]!=d[i]:
                return False
                
        return True
    
s = "anagram"
t = "nagaram"
print(isAnagram(s,t))    