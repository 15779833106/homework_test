def cross(p1,p2,p0):
    return (p1[0]-p0[0])*(p2[1]-p0[1])-(p1[1]-p0[1])*(p2[0]-p0[0])


def inConvexPolygon(polygon, point):
    length = len(polygon)
    if (cross(point, polygon[1], polygon[0]) > 0 and cross(point, polygon[length - 1], polygon[0]) < 0):
        return False
    s=1
    e = len -1
    line = -1
    while s <= e:
        m = s + ((e-s) >> 1)
        if (cross(point, polygon[m], polygon[0]) > 0):
            line = m
            e = m -1
        else:
            s = m + 1
    return cross(polygon[line], point,polygon[line -1]) > 0

polygon=[[0,0],[0,3],[0,4],[2,4],[4,4],[4,2],[4,0],[2,0]]
point=[9,9]
print(inConvexPolygon(polygon,point))
