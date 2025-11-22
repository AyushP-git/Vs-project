print("Welcome to my Python program!")
miles = input("How many miles did you walk today")

try: 
    miles = float(miles)
except ValueError:
    print("please enter a valid number")
    exit()
weekly_miles = miles * 7
print(f"You are on track to walk {weekly_miles} miles this week.")