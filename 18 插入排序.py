A=[11,6,8,19,4,10,5,17,43,49,31]
for i in range(1,len(A)):
    a=A[i]
    j=i-1
    while j>=0:
        if a<A[j]:
            A[j+1]=A[j]
            #A[j]=a
            j=j-1
        else:
            break
    A[j+1]=a
    print(A)


