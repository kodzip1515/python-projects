#init
import random
words = ["dog", "man", "cat", "git"]
guess = ""
attemps = 6

# process
word = random.choice(words)
guessed = []

for x in range(attemps):
    guess = input("enter a letter: ")
    if guess in word:
        print("correct!")
        guessed.append(guess)
    else:
        print("incorrect")
    
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"
            
    # output
    print(display)
print(f"the word was {word}")