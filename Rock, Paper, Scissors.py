import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
rps = [rock, paper, scissors]
print("Welcome to the Rock, Paper, Scissors game!")
user_input = int(input("What would you like to choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
if user_input == 0:
  print(rock)
elif user_input == 1:
  print(paper)
elif user_input == 2:
  print(scissors)
else:
  print("You typed an invalid number, you lose!")

print("Computer chose:")
computer_input = random.randint(0, 2)
print(rps[computer_input])
if user_input >= 3 or user_input < 0:
  print("You typed an invalid number, you lose!")
elif user_input == 0 and computer_input == 2:
    print("You win!")
elif computer_input == 0 and user_input == 2:
    print("You lose. Better luck next time!")
elif computer_input > user_input:
    print("You lose. Better luck next time!")
elif user_input > computer_input:
    print("You win!. Congratulations!")
elif computer_input == user_input:
    print("It's a draw")