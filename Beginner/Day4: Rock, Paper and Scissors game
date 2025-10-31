import random
print("what will you choose ? Type 0 for rock, 1 for paper, 2 for scissors")
choice = int(input("Your choice: \n"))
rock="""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """
paper="""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """
scissors="""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
else:
    print(scissors)
computer_choice = random.randint(0, 2)
print("Computer chose : ", computer_choice)
if computer_choice == 0:
    print(rock)
if computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)
if choice == 0 and computer_choice == 0:
    print("Draw")
if choice == 1 and computer_choice == 0:
    print("You win")
if choice == 2 and computer_choice == 0:
    print("You lose")
if choice == 0 and computer_choice == 1:
    print("You win")
if choice == 1 and computer_choice == 1:
    print("Draw")
if choice == 2 and computer_choice == 1:
    print("You win")
if choice == 0 and computer_choice == 2:
    print("You win")
elif choice == 1 and computer_choice == 2:
    print("You lose")
elif choice == 2 and computer_choice == 2:
    print("You lose")
else:
    print("You typed an invalid number.you lose")
