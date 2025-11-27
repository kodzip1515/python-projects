print("tempiture calculator c = Celsius f = Fahrenheit")
choice = input("c or f: ").lower()
temp = 0

while True:
    choice = input("c or f: ").lower()
    
    if choice == "f":
        temp = float(input("enter tempiture: "))
        c = (temp - 32) * 5/9
        print(f"your temp in Celsius is {c:.0f}")

    elif choice == "c":
        temp = float(input("enter tempiture: "))
        f = (temp *9/5) + 32
        print(f"your temp in Fahrenheit is {f:.0f}")
    
    else:
        print("Not Valid Input")