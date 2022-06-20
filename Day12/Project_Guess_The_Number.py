#Number Guessing Game Objectives:
# Include an ASCII art logo. V
# Allow the player to submit a guess for a number between 1 and 100. V
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

logo="""
  ________                            .__                   ________                       
 /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____  
/   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ 
\    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/ 
 \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >
        \/            \/     \/     \/        \//_____/           \/     \/      \/     \/ 
"""
print(logo)
print("Welcome to the Number Guessing Game!")

print("I'm thinking about a number between 1 to 100.")
random_num = random.randint(1,100)
print(random_num)

diff = input("Choose a difficulty! Type 'easy' or 'hard': ")
attempts=0
used_attempts=1

if diff=="easy":
  attempts=10
elif diff=="hard":
  attempts=5

while attempts!=0:
  guess = int(input("Make a guess: "))
  if guess!= random_num:
    if guess<random_num:
      print("Too low.")
    elif guess>random_num:
      print("Too high.")
    attempts-=1
    used_attempts+=1
    print(f"Guess again. You have {attempts} attempts left.")
  elif guess==random_num:
    print(f"You've made the right guess! It takes you only {used_attempts} attempts!")
    break

if attempts==0:
  print("You have run out of guesses. Game over QQ.")
