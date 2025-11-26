# init
tip = ""
total = ""
payment = ""

# process
payment = float(input("enter amount to pay: £"))
tip = float(input("enter tip %: "))
total = payment + (tip / 100 * payment)

# output
print(f"your total is £{total}")