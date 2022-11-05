import random 

# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

def game():
    start=int(input("Whad do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors: "))
    if start == 0:
        start = rock
        print ("User choose:", rock)
    if start == 1:
        start = paper
        print("User choose:", paper)
    if start == 2:
        start = scissors
        print("User choose:", scissors)
    game_items = [rock, paper, scissors]
    computer = random.choice(game_items)
    print ("Computer choose:",computer)
    if (start == rock and computer == scissors) or (start == scissors and computer == paper) \
    or (start == paper and computer == rock):
        print ("You win")
    elif (start == rock and computer == rock) or (start == scissors and computer == scissors) \
        or (start == paper and computer == paper):
        print ("It's a tie!")
    else:
        print("Computer Win")

game()