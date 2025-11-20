def volume(l, w, h):
    return l * w * h


def surfaceArea(l, w, h):
    return 2 * (l * h + w * h + w * l)


while True:
    try:
        # defines variable line and strips
        line = input().strip()
        # checks if line isn't empty
        if not line:
            # if empty, skips to next iteration
            continue
        # next iteration
        l, w, h = map(int, line.split())
        print(f"The volume of a {l} by {w} by {h} box is {volume(l, w, h)}.")
        print(
            f"The surface area of a {l} by {w} by {h} box is {surfaceArea(l, w, h)}.\n"
        )
    except EOFError:
        break
