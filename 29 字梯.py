def zt(bw,ew,wlst):
    if ew not in wlst:
        return 0
    if bw in wlst:
        wlst.remove(bw)
    wdict=dict()
    for w in wlst:
        for i in range(len(w)):
            tmp=w[:i]+"_"+w[i+1:]
            wdict[tmp]=wdict.get(tmp,[])+[w]
    stack,visited=[(bw,1)],set()
    while stack:
        w,step=stack.pop(0)
        if w not in visited:
            visited.add(w)
            if w==ew:
                return step
            for i in range(len(w)):
                tmp=w[:i]+"_"+w[i+1:]
                neigh_words=wdict.get(tmp,[])
                for neigh in neigh_words:
                    if neigh not in  visited:
                        stack.append(neigh,step+1)
