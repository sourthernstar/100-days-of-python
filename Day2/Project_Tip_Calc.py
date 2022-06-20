print("Welcome to the tip calculator!")
bill=float(input("What was the total bill?"))
tip=float(input("How much tip would you like to give? 10, 12,or 15?"))
num_of_people=float(input("How many people to spill the bill?"))

payment=round((bill/num_of_people)*(1+tip/100),2)

print(f"Each person should pay {payment}")