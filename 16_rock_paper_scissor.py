import random
ROCK = "r"
PAPER = "p"
SCISSOR = "s"
dict = {ROCK: "🪨", PAPER: "📃", SCISSOR: "✂️"}
choices = tuple(dict.keys())

def generate():
    # choices2 = (char for char in choices if char != ch)
    gen = random.choice(choices)
    return gen

def get_user_choice():
    while True:
        user = input("Rock, Paper, or Scissor? (r/p/s): ").lower()
        if user in choices:
            return user
        else:
            print("invalid choice")
            
def display():
    print("You chose:\t", dict[user])
    print("Computer chose:\t", dict[comp])

def compare():
    if user == comp:
        print("Tie!")
    elif (
     (user == ROCK and comp == SCISSOR) or 
     (user == PAPER and comp == ROCK) or 
     (user == SCISSOR and comp == PAPER)):
        print("You win!")
    else:
        print("You lose.")

while True:
    user = get_user_choice()

    comp = generate()

    display()
    compare()
    cont = input("continue? (y/n): ").lower()
    if cont == "y" or cont=="a":
        continue
    else:
        print("thanks")
        break
