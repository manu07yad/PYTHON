def game(a,b):
    if (a=='s' and b=='p'):
        return("PLAYER 1 IS WINNER")
    elif(a=='p' and b=='s'):
        return("PLAYER 2 IS WINNER")
    if (a=='p'and b=='k'):
        return ("PLAYER 2 IS WINNER")
    elif (a=='k'and b=='p'):
        return ("PLAYER 1 IS WINNER")
    if (a=='s'and b=='k'):
        return ("PLAYER 1 IS WINNER")
    elif (a=='k'and b=='s'):
        return("PLAYER 2 IS WINNER") 
    if ((a=='k'and b=='k') or (a=='p' and  b=='p') or (a=='s' and b=='s')):
        return("TIE")
    else:
        return ("Wrong Choice")



a= input("Player 1: Choose stone(s) ,paper(p), scissor(k) : ")
b= input("Player 2: Choose stone(s) ,paper(p), scissor(k) : ")
c= game(a,b)
print(c)