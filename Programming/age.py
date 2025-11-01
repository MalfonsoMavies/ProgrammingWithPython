while True:
    try:
        name, x = input().split()
        age = int(x)  # Ensure x is an integer in string form
        print(name + " is " + str(age) + " years old.")
    except EOFError:
        break