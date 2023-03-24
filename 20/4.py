from math import sin, cos, radians

print("x[°]   sin(x)   cos(x)")
for x in range(0, 361, 30):
    r: float = radians(x)
    print("{:3d}   {:6.3f}   {:6.3f}".format(x, sin(r), cos(r)))
