import random
user = ""

user = input("enter: ")
amount = random.randint(2, len(user))
final = user[:amount]

num = random.randint(1,1000)
print(f"{final}{num}")