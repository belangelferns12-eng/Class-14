import random
r = random.randint(1, 10)

lives = 5
while lives >=1:
    print("💗"* lives)
    guess = int(input("Enter Your Guess: "))
    if guess == r:
        print("Thats the right guess!!")
        break
    else:
        print("Thats the wrong guess. Please try again")
    lives = lives - 1

