#this is to clear the screen for better visibility
from IPython.display import clear_output
#this is importing a random fuction which will be used for generating random number to select which player 
#will play first
import random
#our intial board will empty
intial_board = [['-','-','-'],['-','-','-'],['-','-','-']]

#our main fuction which will begin the game
def welcome():
    chance = random.randint(1,2)#generating random number
    print "welcome players"
    displayBoard(intial_board)
    while(finalCheck(intial_board)):#check whether board is empty or not
        if chance == 1:
            player1Input()
        else:
            player2Input()
        
        if(finalCheck(intial_board)):#same check again
            if chance == 1:
                player2Input()
            else:
                player1Input()
        else:#it is the win logic
            if(((intial_board[0][0]=='X') and (intial_board[0][1]=='X') and (intial_board[0][2]=='X') or
              (intial_board[1][0]=='X') and (intial_board[1][1]=='X') and (intial_board[1][2]=='X')  or
              (intial_board[2][0]=='X') and (intial_board[2][1]=='X') and (intial_board[2][2]=='X')  or 
              (intial_board[0][0]=='X') and (intial_board[1][0]=='X') and (intial_board[2][0]=='X')  or
              (intial_board[0][1]=='X') and (intial_board[1][1]=='X') and (intial_board[2][1]=='X')  or
              (intial_board[0][2]=='X') and (intial_board[1][2]=='X') and (intial_board[2][2]=='X')  or
              (intial_board[0][2]=='X') and (intial_board[1][1]=='X') and (intial_board[2][0]=='X')  or
              (intial_board[0][0]=='X') and (intial_board[1][1]=='X') and (intial_board[2][2]=='X')) and
              ((intial_board[0][0]=='O')and (intial_board[0][1]=='O') and (intial_board[0][2]=='O')  or
              (intial_board[1][0]=='O') and (intial_board[1][1]=='O') and (intial_board[1][2]=='O')  or
              (intial_board[2][0]=='O') and (intial_board[2][1]=='O') and (intial_board[2][2]=='O')  or 
              (intial_board[0][0]=='O') and (intial_board[1][0]=='O') and (intial_board[2][0]=='O')  or
              (intial_board[0][1]=='O') and (intial_board[1][1]=='O') and (intial_board[2][1]=='O')  or
              (intial_board[0][2]=='O') and (intial_board[1][2]=='O') and (intial_board[2][2]=='O')  or
              (intial_board[0][2]=='O') and (intial_board[1][1]=='O') and (intial_board[2][0]=='O')  or
              (intial_board[0][0]=='O') and (intial_board[1][1]=='O') and (intial_board[2][2]=='O'))):
                    print "it is a draw!!!!"
                    break
            elif((intial_board[0][0]=='X') and (intial_board[0][1]=='X') and (intial_board[0][2]=='X') or
              (intial_board[1][0]=='X') and (intial_board[1][1]=='X') and (intial_board[1][2]=='X')  or
              (intial_board[2][0]=='X') and (intial_board[2][1]=='X') and (intial_board[2][2]=='X')  or 
              (intial_board[0][0]=='X') and (intial_board[1][0]=='X') and (intial_board[2][0]=='X')  or
              (intial_board[0][1]=='X') and (intial_board[1][1]=='X') and (intial_board[2][1]=='X')  or
              (intial_board[0][2]=='X') and (intial_board[1][2]=='X') and (intial_board[2][2]=='X')  or
              (intial_board[0][2]=='X') and (intial_board[1][1]=='X') and (intial_board[2][0]=='X')  or
              (intial_board[0][0]=='X') and (intial_board[1][1]=='X') and (intial_board[2][2]=='X')):
                    print "hurrahhhhhhhh palyer 1 wins!!!!!!!"
                    break
            elif((intial_board[0][0]=='O') and (intial_board[0][1]=='O') and (intial_board[0][2]=='O') or
              (intial_board[1][0]=='O') and (intial_board[1][1]=='O') and (intial_board[1][2]=='O')    or
              (intial_board[2][0]=='O') and (intial_board[2][1]=='O') and (intial_board[2][2]=='O')    or 
              (intial_board[0][0]=='O') and (intial_board[1][0]=='O') and (intial_board[2][0]=='O')    or
              (intial_board[0][1]=='O') and (intial_board[1][1]=='O') and (intial_board[2][1]=='O')    or
              (intial_board[0][2]=='O') and (intial_board[1][2]=='O') and (intial_board[2][2]=='O')    or
              (intial_board[0][2]=='O') and (intial_board[1][1]=='O') and (intial_board[2][0]=='O')    or
              (intial_board[0][0]=='O') and (intial_board[1][1]=='O') and (intial_board[2][2]=='O')):
                print "huraaaahhh player 2 wins!!!!!!!"
                break
            else:
                continue
    else:
        print "Its a draw!!!!!"
          

      
        
    

def displayBoard(list):#display our board
    clear_output()
    for i in range(len(list)):
        for j in range(len(list)):
            print "  " + list[i][j],
        print
    print
displayBoard(intial_board)

def player1(x1,y1):#to take player1 input
    try:
        if intial_board[x1-1][y1-1] != '-':
            print "sorry this position is already filled try again"
            player1Input()
        else:
            intial_board[x1-1][y1-1] = 'X'
            displayBoard(intial_board)
    except:
        print "guess you have entered wrong position check and enter again"
        player1Input()
        return False
def player1Input():#if he misses something then it will help us to take again
    print "player 1 enter you position in terms of x and y coordinate "
    x1=(raw_input("Enter x coordinate"))
    y1=(raw_input("Enter y coordinate"))
  
    if ((x1=='') or (y1=='')):
        print "please enter coordinate to proceed further"
        player1Input()
    else:
        x1 = int(x1)
        y1 = int(y1)
        player1(x1,y1)


def player2(x2,y2):#same for player2
    try:
        if intial_board[x2-1][y2-1] != '-':
            print "sorry this position is already filled try again"
            player2Input()
        else:
            intial_board[x2-1][y2-1] = 'O'
            displayBoard(intial_board)
    except:
        print "guess you have entered wrong position check and enter again"
        player2Input()
        return False

def player2Input():
    print "player 2 enter you position in terms of x and y coordinate "
    x2=(raw_input("Enter x coordinate"))
    y2=(raw_input("Enter y coordinate"))
 
    if ((x2=='') or (y2=='')):
        print "please enter coordinate to proceed further"
        player2Input()
    else:
        x2 = int(x2)
        y2 = int(y2)
        player2(x2,y2)
    
def finalCheck(final_board):#this will check whether our board has some empty space or it is filled
    for i in range(len(final_board)):
        if '-' in final_board[i]:
            return True
        else:
            continue
    return False


    
    
t= True
while(t):
    welcome()
    print "do you wanna play again(Y/N)"
    ch = str(raw_input("Enter you choice"))
    while ch == '':
        print "please enter correct choice"
        ch = str(raw_input("Enter you choice"))
    ch = ch.upper()
    if(ch == 'Y'):
        intial_board = [['-','-','-'],['-','-','-'],['-','-','-']]
        t= True
    else:
        print "Thank you see you soon!"
        t=False
    



    