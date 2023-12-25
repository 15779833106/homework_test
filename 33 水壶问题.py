def shwt(a,b, target):
    #ac A含水量  bc B含水量
    if a == target or b == target or (a + b) == target or abs(a - b) == target:
        return True

    if (a + b) < target:
        return False

    queue = [(0, 0)]
    visited = set()
    visited.add((0, 0))
    while queue:
        ac, bc = queue.pop(0)
        # 判断此时水壶中水是否正好构成target
        if ac == target or bc == target or (ac + bc) == target:
            return True
        # 1、A倒空；2、A装满；3、B倒空；4、B装满；5、A倒进B，直到B倒满或者A倒空；6、B倒进A，直到A倒满或者B倒空
        for x, y in [(0, bc), (a, bc), (ac, 0), (ac, b),(max(ac + bc - b, 0),min(ac + bc, b)),
                    (min(ac + bc, a), max(ac + bc - a, 0))]:
            if (x, y) not in visited:
                queue.append((x, y))
                visited.add((x, y))
    return False

if __name__=="__main__":
    print(shwt(3,5,4))