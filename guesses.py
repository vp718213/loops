import random
guesses=3
while guesses>0:
    random_number=random.randint(1,10)
    mynumber=int(input("Please enter your guess"))
    if mynumber==random_number:
        print("You win")
    else:
        print("You loose")
        guesses=guesses-1
