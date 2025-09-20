x, y, z = map(int, input().split())
if x + y <= z or x + z <= y or y + z <= x:
    print("impossible")
elif x == y and x == z and z == y:
    print("equilateral")
elif x != y and x != z and y != z:
    print("scalene")
else:
    print("isosceles")