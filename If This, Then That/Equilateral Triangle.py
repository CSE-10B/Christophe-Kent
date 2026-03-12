x = int(input("Enter the length of the first side of the triangle: "))
y = int(input("Enter the length of the second side of the triangle: "))
z = int(input("Enter the length of the third side of the triangle: "))

if x == y and y == z:
    print("It is an equilateral triangle")
else:
    print("It is not an equilateral triangle")