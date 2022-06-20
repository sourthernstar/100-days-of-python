# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


name_group=name1.lower()+name2.lower()

first=name_group.count('t')+name_group.count('r')+name_group.count('u')+name_group.count('e')
last=name_group.count('l')+name_group.count('o')+name_group.count('v')+name_group.count('e')

total_score=first*10+last

if (total_score>90 or total_score<10):
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif (40<total_score<50):
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")