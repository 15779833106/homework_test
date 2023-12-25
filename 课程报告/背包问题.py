def bag(W,wt,val,n):
    K=[[0 for x in range(W+1)] for x in range(n+1)]

    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w]=0
            elif wt[i-1]<=w:
                K[i][w]=max(val[i-1]+K[i-1][w-wt[i-1]],K[i-1][w])
            else:
                K[i][w]=K[i-1][w]

    return K
def show(n, W, wt, value):
    print('最大价值为:', value[n][W])
    x = [0 for i in range(n)]
    j = W
    for i in range(n, 0, -1):
        if value[i][j] > value[i - 1][j]:
            x[i - 1] =1
            j -= wt[i - 1]
    print('背包中所装物品为:')
    print(x)
if __name__=="__main__":
    value=bag(30,[16,15,15],[45,25,25],3)
    show(3,30,[16,15,15],value)
