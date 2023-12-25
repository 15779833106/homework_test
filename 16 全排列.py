def permute(nums):
    rt = []
    newrt = []
    for i in range(len(nums)):
        for j in range(max(len(rt), 1)):
            for k in range(0, len(nums)):
                if len(rt) == 0:
                    newlist = rt + [nums[k]]
                else:
                    if [nums[k]] == rt[j] or nums[k] in rt[j]:
                        continue
                    newlist = rt[j] + [nums[k]]
                newrt.append(newlist)
        rt = newrt
        newrt = []
    return rt

def permutation(str):
    lenstr=len(str)
    if lenstr<2:
        return str
    else:
        result=[]
        for i in range(lenstr):
            ch=str[i]
            rest=str[0:i]+str[i+1:lenstr]
            for s in permutation(rest):
                result.append(ch+s)
    return result


print(permutation("ABCD"))

