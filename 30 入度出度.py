def rc(heap):
    n=len(heap)
    in_d=[0]*1000
    out_d=[0]*1000
    for i in range(n):
        if i*2+1<n:
            out_d[i]+=1
            in_d[i*2+1]+=1
            if i*2+2<n:
                out_d[i]+=1
                in_d[i*2+2]+=1
    return in_d[:n],out_d[:n]