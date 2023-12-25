def max_profit_dc(prices):
    len_prices=len(prices)
    if len_prices<=1:
        return 0
    mid=len_prices//2
    prices_left=prices[:mid]
    prices_right=prices[mid:]
    maxProfit_left=max_profit_dc(prices_left)
    maxProfit_right=max_profit_dc(prices_right)
    maxProfit_left_right=max(prices_right)-min(prices_left)
    return max(maxProfit_left_right,maxProfit_right,maxProfit_left)

def max_list(lst):
    length=len(lst)
    if length<=1:
        return lst
    mid=length//2
    left=lst[:mid]
    right=lst[mid:]
    max_left=max_list(left)
    max_right=max_list(right)
    maxlst=left+right
    max1=sum(max_left)
    j=0
    templist=[max_left,max_right,maxlst]
    for i in range(3):
        if sum(templist[i])>max1:
            max1=sum(templist[i])
            j=i
    return templist[j]


def max_lst1(lst):
    if len(lst)==0:
        return 0
    res=0
    dp=[0]*len(lst)
    dp[0]=lst[0]
    for i in range(1,len(lst)):
        dp[i]=max(dp[i-1]+lst[i],lst[i])
        res=max(dp[i],res)

    return res

#A=[13,17,15,8,14,15,19,7,8,9]
#print(max_profit_dc(A))
B=[1.-4,3,-4,9,21,-9,30]
print(max_list(B))