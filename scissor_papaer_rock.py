import random

def game(comp, player):
    if comp==player:
        return None

    elif comp == "scissor":
        if player == "paper":
            return False
        elif player == "rock":
            return True
    
    elif comp == "paper":
        if player == "rock":
            return False
        elif player == "scissor":
            return True

    elif comp == "rock":
        if player == "scissor":
            return False
        elif player == "paper":
            return True
        


a = random.randint(1,3)
if a==1:
    comp = "scissor"
elif a==2:
    comp = "paper"
elif a==3:
    comp = "rock"

player = input("your turn: ")

print(f"computer turn: {comp}")

result = game(comp, player)

if result==None:
    print("the game is tie !!")

elif result==True:
    print("congrates !! you win the game")
else:
    print("hahaha !! you lose the game")