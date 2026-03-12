year = int(input("enter code: "))
if year % 4 == 0.: # year divisible by 4
    leap = True
else:
    leap = False
if year %400 == 0: # year divisble by 400
    leap = True
else:
    leap = False