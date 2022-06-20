#Write your code below this line 👇

def prime_checker(number):
    if (number==2)or(number==3)or(number==5)or(number==7)or(number==11)or(number==13)or(number==17)or(number==19)or(number==23)or(number==29)or(number==31)or(number==37)or(number==41)or(number==43)or(number==47)or(number==53)or(number==59)or(number==61)or(number==67)or(number==71)or(number==73)or(number==79)or(number==83)or(number==89)or(number==97):
        print("It's a prime number.")
    else:
        print("It's not a prime number.")



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
