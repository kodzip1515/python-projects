#init
password = "hello"
guess = 0
passguess = ""

#process
for x in range(3):
    passguess = input("please enter your password: ")
    if passguess == password:
        print("correct password")
        break
    guess = guess + 1
    if guess == 3:
        print("error to many attemps")
