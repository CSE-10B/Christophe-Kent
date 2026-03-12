# WAP to print the day based on the number input. (For example: if input = 1, output = Monday)
num = int(input("Enter a number (1-7): "))
days = ("Monday", "Tuesday", "Wednsday", "Thursday", "Friday", "Saturday", "Sunday")
if 1 <= num <= 9:
    print(days[num - 1])
else:
    print("invalid number")