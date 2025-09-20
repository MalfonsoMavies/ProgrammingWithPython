def volume(length, hight, width):
    return length * hight * width

def area(length, height, width):
    return (length * height + length * width + height * width) * 2

length, height, width = map(int, input().split())
print("The volume of a " + str(length) + " by " + str(height) + " by " + str(width) + " box is " + str(volume(length, height, width)) + ".")
print("The surface area of a " + str(length) + " by " + str(height) + " by " + str(width) + " box is " + str(area(length, height, width)) + ".")