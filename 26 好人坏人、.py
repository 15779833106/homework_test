lis=[0]*1000
def printcol(graph):
    for i in range(len(graph)):
        if lis[i]==0 and not dfs(graph,i,1):
            return False
        return True

def dfs(graph,node,colour):
    if lis[node]==0:
        lis[node]=colour
    else:
        if lis[node]!=colour:
            return False
    for j in graph[node]:
        if lis[j]==0:
            lis[j]=3-colour
            if not dfs(graph,j,3-colour):
                return False
            else:
                if lis[j]==colour:
                    return False
    return True

graph=[[1],[2,3],[4],[4],[]]
result=printcol(graph)
if result==False:
    print("error")
else:
    for i in range(len(graph)):
        if lis[i]==1:
            print("第"+str(i+1)+"号选手当好人")
        else:
            print("第"+str(i+1)+"号选手当坏人")