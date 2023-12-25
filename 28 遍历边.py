def bfs(graph,source):
    front=[source]
    travel=[source]
    while front:
        nexts=[]
        for x in front:
            for cur in graph[x]:
                if cur not in travel:
                    travel.append(cur)
                    nexts.append(cur)
        front=nexts
    return travel

graph={}
graph['a']=['b']
graph['b']=['c','d']
graph['c']=['e']
graph['d']=[]
graph['e']=['a']

print(bfs(graph,'b'))