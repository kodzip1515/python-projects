import random
number = 0
guess = 0
level = 0
status = ""

level = level + 1
print(f"Level {level}")
number = random.randint(1,100)
while True:

    guess = int(input("enter your guess: "))

    if guess > number:
        print("too high!")

    elif guess < number:
        print("too low!")

    elif guess == number:
        print("Correct!!")
        replay = input("play again Y/n: ")
        if replay == "n".lower:
            break
        
print("thanks for playing!")
    

