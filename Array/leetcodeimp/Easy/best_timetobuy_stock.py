#121. Best Time to Buy and Sell Stock
#You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0

#M1 - 2 loops for i and j and finding profit every time
# def maxprofit(prices):
#     n = len(prices)
#     currprofit = 0
#     maprofit = 0
#     for i in range(n):
#         for j in range(i+1,n):
#             currprofit = prices[j]-prices[i]
#             maprofit = max(currprofit,maprofit)
#     return maprofit        




#M2-- optimized
def maxProfit(prices):
        l,r=0,1
        mp =0
        while r<len(prices):
            if prices[l]<prices[r]:
                profit = prices[r]-prices[l]
                mp = max(profit,mp)
            else:
                l=r
            r+=1
        return mp    
    
#my code
def maxProfit(self,prices):
    n = len(prices)
    curprofit,maprofit = 0,0
    i,j=0,1
    while j<n:
        if prices[i]>prices[j]:
            i=j
            j+=1
        else:
            curprofit=prices[j]-prices[i]
            j+=1
        maprofit = max(maprofit,curprofit)
    return maprofit               
    








prices = [7,1,5,3,6,4]
print(maxprofit(prices))
