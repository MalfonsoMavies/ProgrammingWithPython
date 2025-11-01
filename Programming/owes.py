while True:
    try:
        x, name1, name2 = input().split()
        amount = float(x)
        print(f"{name1} owes ${amount:.2f} dollars to {name2}.")
    except EOFError:
        break
