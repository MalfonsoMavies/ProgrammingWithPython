def triangleAngleType(x, y, z):
    if x * x + y * y == z * z or x * x + z * z == y * y or y * y + z * z == x * x:
        return "right"
    elif x * x + y * y < z * z or x * x + z * z < y * y or y * y + z * z < x * x:
        return "obtuse"
    else:
        return "acute"


while True:
    try:
        x, y, z = map(int, input().split())
        if x + y <= z or x + z <= y or y + z <= x:
            print("impossible")
        elif x == y and x == z and y == z:
            print(f"equilateral {triangleAngleType(x, y, z)}")
        elif x != y and x != z and y != z:
            print(f"scalene {triangleAngleType(x, y, z)}")
        else:
            print(f"isosceles {triangleAngleType(x, y, z)}")
    except EOFError:
        break
