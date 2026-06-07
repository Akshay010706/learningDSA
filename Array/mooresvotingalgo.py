# moore's voting algorith 

# Q - find the majority elements
# fequency>n/2
# brote force - two loops - o(n**2)
# optimize - sort -- o(nlog(n))

#1.sort and find  ----- o(nlog(n))
def majorityEle(givennums):
    givennums.sort()
    majorityelement = givennums[0]
    count=1
    maxcount =0
    
    for i in range(len(givennums)-1):
        if givennums[i] != givennums[i+1]:
            if maxcount < count:
                majorityelement = givennums[i]
                maxcount = count
            count=1
        else:
            count+=1
    if maxcount<count:
        majorityEle - givennums[-1]
                  
    return majorityelement      



#2. map of frequency ----------- time -o(n)  space-- o(n)


#3. moores voting algorithm time ---o(n) space --o(1)

# [1,3,2,1,1]
# majelement - 1 , 3 , 2, 1 , 1
# count - 1 , 1-1=0 , 1 , 1-1=0, 1
# one is the majority element
# works only when an elemnt is occuring more then n//2 times

def majorityEle(givennums):
    majorityelemt = givennums[0]
    votes = 1
    for i in givennums:
        if votes == 0:
            majorityelemt = i
            votes = 1
        else:
            if majorityelemt == i:
                votes+=1
            else:
                votes-=1    
    return majorityelemt     

    #assumption freq >n/2 is not given 
    votes = 0
     
    for i in givennums:
        if majorityelemt == i:
            votes +=1
    if votes . len(givennums)//2:
        return  majorityelemt
    return -1       
                   
                       
    

givennums = [1,3,3,1,1,1,12,1,1,1,1] # frequency of 1 > n/2 =5/2
print(majorityEle(givennums))




