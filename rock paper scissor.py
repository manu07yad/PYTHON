import random
# Rock Paper Scissors

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
            return False
        elif you == 's':
            return True
    elif comp == 'p':
        if you == 's':
            return False
        elif you == 'r':
            return True
    elif comp == 's':
        if you == 'r':
            return False
        elif you == 'p':
            return True



print("Comp Turn: Snake(s) Water(w) or Gun(g)? ")
randNo=random.randint(1,3)
print(randNo)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
if randNo == 3:
    comp = 's'

you = input("Player's Turn: Rock(r) Paper(p) or Scissor(s)? ")
a = gameWin(comp, you)

print(f"Computer Choice {comp}")
print(f"Your choise {you}")
if a == None:
    print("The game is a tie!")
elif a:
    print("Congratulations! You Win!")
else:
    print("You Lose! Try Next Time")