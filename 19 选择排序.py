A=[11,6,8,19,4,10,5,17,43,49,31]

for i in range(len(A)):
    min=A[i]
    for j in range(i+1,len(A)):
        if A[j]<min:
            min=A[j]
            minindex=j
    temp=A[i]
    A[i]=min
    A[minindex]=temp
    print(A)