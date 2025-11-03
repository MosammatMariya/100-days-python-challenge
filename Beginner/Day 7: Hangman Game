import random

#put hangman into another python file and import it to main file

hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']
# Put Letter_list into another python file and import into main file
letter_list= [
        "penholder",
        "cathedral",
        "headboard",
        "carpenter",
        "probation",
        "carpenter",
        "scarecrow",
        "graveness",
        "electable",
        "judiciary",
        "dismantle",
        "subatomic",
        "dreamless",
        "sandstorm",
        "verbalize",
        "amplifier",
        "underfeed",
        "commodore",
        "transport",
        "residency",
        "camcorder",
        "unbounded",
        "rectangle",
        "unlocking",
        "comprised",
        "nintendo",
        "cursing",
        "deafmetal",
        "jurriaan",
        "arise",
        "vixen",
        "wheat",
        "press",
        "prude",
        "guide",
        "defog",
        "genre",
        "lived",
        "scale",
        "false",
        "twirl",
        "catty",
        "nifty",
        "haven",
        "pesky",
        "karma",
        "hedge",
        "arise",
        "music",
        "jolly",
        "alone",
        "bleak",
        "speed",
        "rigor",
        "noah",
        "balls",
        "star",
        "why",
        "bye",
        "shy",
        "lie",
        "hop",
        "fly",
        "one",
        "but",
        "nut",
        "fat",
        "mom",
        "dad",
        "pis",
        "kid",
        "who",
        "gem",
        "paf",
        "tag",
        "gap",
        "jam",
        "old",
        "owl",
        "art",
        "map",
        "baby",
        "eepy"
    ]

lives = 6

chosen=random.choice(letter_list)

placeholder=""
l=len(chosen)
for position in range(l):
    placeholder+='_'
print(placeholder)

over = False
correct = []

while not over:
  guess=input("Guess a letter: ").lower()
  if guess in chosen:
      print(" YOU ALREADY GUESSED IT!")


  display=" "

  for letter in chosen:
     if letter == guess :
        display += letter
        correct.append(guess)
     elif letter in correct:
        display += letter
     else:
        display += '_'

  print(display)

  if guess not in chosen:
    lives -= 1
    print ("You guessed wrong. Lives left out of 6: ",lives)


  if lives == 0:
    over = True
    print(f"******************************* It was {chosen}. YOU LOSE *****************************************")

  if '_' not in display:
    over = True
    print("******************************** YOU WIN ******************************************")

  print(hangman[lives])
