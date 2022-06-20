# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


if (size=="S"):
    if (add_pepperoni=="Y"):
        if (extra_cheese=="Y"):
            total_bill=18
        else:
            total_bill=17
    elif (add_pepperoni=="N"):
        if (extra_cheese=="Y"):
            total_bill=16
        else:
            total_bill=15
elif (size=="M"):
    if (add_pepperoni=="Y"):
        if (extra_cheese=="Y"):
            total_bill=24
        else:
            total_bill=23
    elif (add_pepperoni=="N"):
        if (extra_cheese=="Y"):
            total_bill=21
        else:
            total_bill=20
elif (size=="L"):
    if (add_pepperoni=="Y"):
        if (extra_cheese=="Y"):
            total_bill=29
        else:
            total_bill=28
    elif (add_pepperoni=="N"):
        if (extra_cheese=="Y"):
            total_bill=26
        else:
            total_bill=25

print(f"Your final bill is: ${total_bill}.")