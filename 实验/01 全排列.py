'''
def permutation(array):
    s=[]
    if len(array)==1:
        return [array]
    else:
        for i in range(len(array)):
            array[i],array[0]=array[0],array[i]
            temp=permutation(array[1:])
            for l in temp:
                s.append([array[0]]+l)
            array[i],array[0]=array[0],array[i]
    return s


print(permutation([1,2,3]))

'''

from queue import PriorityQueue

def dijkstra_algo(graph, start):
    # 初始化距离字典和前驱字典
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    prev = {node: None for node in graph}

    # 初始化优先队列，存放节点的估计距离和节点本身
    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        # 取出当前最小估计距离的节点
        cur_dist, cur_node = pq.get()

        # 遍历当前节点的邻居
        for neigh_node in graph[cur_node]:
            # 计算新的估计距离
            new_dist = cur_dist + graph[cur_node][neigh_node]

            if new_dist < dist[neigh_node]:
                # 如果新的估计距离更小，则更新距离字典和前驱字典
                dist[neigh_node] = new_dist
                prev[neigh_node] = cur_node
                pq.put((new_dist, neigh_node))

    return prev, dist
