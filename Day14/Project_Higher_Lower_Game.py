import art
import game_data
import random
from replit import clear

def gen_random_num():
  return random.randint(0,len(game_data.data))
#print(gen_random_num())
#The higher is the new A_random_num

A_account_num=gen_random_num()
B_account_num=gen_random_num()

keep_winning=True
user_score=0

while A_account_num==B_account_num:
  A_account_num=gen_random_num()
  B_account_num=gen_random_num()

#LOOP START
while keep_winning:
  print(art.logo)
  A_score=game_data.data[A_account_num]['follower_count']
  B_score=game_data.data[B_account_num]['follower_count']
  A_name=game_data.data[A_account_num]['name']
  B_name=game_data.data[B_account_num]['name']
  A_desc=game_data.data[A_account_num]['description']
  B_desc=game_data.data[B_account_num]['description']
  A_country=game_data.data[A_account_num]['country']
  B_country=game_data.data[B_account_num]['country']

  #print(A_score,B_score) 
  
  if user_score>0:
    print(f"You're right! Current score: {user_score}.")

  print(f"Compare A: {A_name}, a {A_desc}, from {A_country}.")
  
  print(art.vs)

  print(f"Against B: {B_name}, a {B_desc}, from {B_country}.")
  user_choice=input("Who has more followers? Type 'A' or 'B': ")
  
  if user_choice=='A' and A_score>B_score:
    user_score+=1
    B_account_num=gen_random_num()
    while A_account_num==B_account_num:
      B_account_num=gen_random_num()
    clear()
  elif user_choice=='B' and A_score<B_score:
    user_score+=1
    A_account_num=B_account_num
    B_account_num=gen_random_num()
    while A_account_num==B_account_num:
      B_account_num=gen_random_num()
    clear()
  else:
    keep_winning=False
    clear()
    
print(art.logo)
print(f"Sorry, that's wrong. Final score: {user_score}")