import time

def sum_nums(low,high):
    if high<low:
        print("error")
        return
    sumnum=0
    #for i in range(low,high+1):
        #sumnum+=i

    while low<=high:
        sumnum+=low
        low+=1
    return sumnum

if __name__=="__main__":
    start=time.time()
    print(sum_nums(1,100))
    end=time.time()
    print(end-start)


