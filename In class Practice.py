import random 
number = random.randint(1, 9)
guess = int(input("Guess the number:"))
done = False
while done == False:
    if guess == number:
        print("you win")
        done = True
        While done == False:
        if guess == number:
            print("you win")
            done = True
        else:
            print ("you lose")
            guess = int(input("guess the number: "))
