n = int(input("Input your number:"))
if n % 2 == 0:
    print("Weird")
else:
    if n % 2 != 0 and n >= 1 and n <= 5:
        print("Not Weird")
if n == 2 or n == 3 or n == 4 or n == 5:
    print("not weird")
if n==6 or n==7 or n==8 or n==9 or n==10:
    print("weird")
if n % 2 != 0 and n >= 6 and n >= 20:
    print("not weird")
