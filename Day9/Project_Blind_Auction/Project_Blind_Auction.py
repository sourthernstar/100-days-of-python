from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.

def bidding():
    print(art.logo)
    print("Welcome to the secret autcion program.")
    bidder_table={}
    keep_adding=True
    while keep_adding:
        name=input("What is your name?: ")
        bid=float(input("What's your bid?: "))
        bidder_table[name]=bid
        other_bidder=input("Are there any other bidders? Type 'yes' or 'no'? ")
        if other_bidder=="yes":
            keep_adding=True
            clear()
        elif other_bidder=="no":
            keep_adding=False
    highest_bid=0
    key=""
    for bidders in bidder_table:
        if bidder_table[bidders]>highest_bid:
            highest_bid=bidder_table[bidders]
            key=bidders
    print(f"The winner is {key} with a bid of {highest_bid}.")

bidding()