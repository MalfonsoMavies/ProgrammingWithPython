def mult(x, y, z):
    return x * y * z


while True:
    try:
        x, y, z = map(int, input().split())
        print(mult(x, y, z))
    except EOFError:
        break
