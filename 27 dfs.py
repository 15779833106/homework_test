def dfs(graph,i,color):
    r=len(graph)
    color[i]=-1
    have_circle=0
    for j in range(r):
        if graph[i][j]!=0:
            if color[j]==-1:
                have_circle=1
            elif color[j]==0:
                have_circle=dfs(graph,j,color)
    color[i]=1
    return have_circle

def findcircle(graph):
    r=len(graph)
    color=[0]*r
    have_circle=1
    for i in range(r):
        if color[i]==0:
            have_circle=dfs(graph,i,color)
            if have_circle==0:
                break
    return have_circle


G=[[0,1,0],[0,0,1],[1,0,0]]  #邻接矩阵存储图
have_circle=findcircle(G)
print(have_circle)