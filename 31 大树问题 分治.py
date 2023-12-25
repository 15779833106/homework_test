def mul(a,b):
    if len(a)>len(b):
        a,b=b,a
    if(len(a)<3):
        return str(int(a)*int(b))
    mid=len(a)//2
    a1=a[:mid]
    a2=a[mid:]
    return add(mul(a1,b)+"0"*len(a2),mul(a2,b))
def add(a,b):
    return str(int(a)+int(b))

if __name__=="__main__":
    a="123456789"
    b="3456789631323"
    print(mul(a,b))