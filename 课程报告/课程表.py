def canFinish(numCourses, preList):
    graph = [[] for _ in range(numCourses)]
    vis = [0] * numCourses
    #建图
    for c, pre in preList:
        graph[c].append(pre)

    def dfs(cur):
        #如果结点在深度搜索中已经访问过，返回false
        if vis[cur] == -1:
            return False
        #如果结点已访问过，进行标记
        if vis[cur] == 1:
            return True
        #将正在访问的结点进行标记
        vis[cur] = -1
        #深度优先搜索结点
        for v in graph[cur]:
            if not dfs(v):
                return False
        #深度优先搜索完所有结点后将其标记为已访问
        vis[cur] = 1
        return True
    for v in range(numCourses):
        if not dfs(v):
            return False
    return True

if __name__=="__main__":

    print(canFinish(2,[[1,0]]))
    print(canFinish(2,[[1,0],[0,1]]))


