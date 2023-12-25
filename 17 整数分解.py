m = int(input())
a = [0]*15
def dfs(n,s):
    global a
    if n==0:
        if s<=2:
            return
        for i in range(1,s-1):
            print("{}+".format(a[i]),end="")
        print(a[s-1])
    for i in range(1,n+1):
        if i>=a[s-1]:
            a[s]=i
            dfs(n-i,s+1)
dfs(m,1)



