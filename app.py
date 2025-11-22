#welcome message
print("Welcome to my Python program!")
#user input 
miles = input("How many miles did you walk today")
#Convert
try: 
    miles = float(miles)
except ValueError:
    print("please enter a valid number")
    exit()
# estimate calculation
weekly_miles = miles * 7
#Output results
print(f"You are on track to walk {weekly_miles} miles this week.")