c = int(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print(c, "°C is", int(f), "in Fahrenheit")

f = int(input("Enter temperature in Fahrenheit: "))
c = (f - 32) * 5/9
print(f, "°F is", int(c), "in Celsius")
