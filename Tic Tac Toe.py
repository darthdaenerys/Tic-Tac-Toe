import numpy as np
import cv2
import random

# Main game class
class TicTacToe:
    def __init__(self):
        # define parameters
        self.windowwidth=1000
        self.windowheight=630
        self.firstMove=True
        self.mygame=np.zeros([self.windowheight,self.windowwidth,3],dtype=np.uint8)
        self.bgcolour=(70,16,33)
        self.Ocolour=(231,75,229)
        self.Oradius=50
        self.Xcolour=(219,206,60)
        self.gridcolour=(31,217,180)
        self.thickness=7
        self.player1=0
        self.player2=0
        self.wincolor=(67,130,240)
        self.moveHLcolor=(53,188,50)
        self.gamestate=[
            [' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' ']
        ]
        self.player1move=True
        if self.firstMove:
            bg=cv2.blur(self.mygame,(18,18))
            cv2.putText(bg,'Welcome to Tac Tac Toe',(300,310),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            cv2.imshow('Tic Tac Toe',bg)
            cv2.waitKey(1200)
            self.selection1=random.choice(['X','O'])
            self.firstMove=False
        self.selection2=None

        # create the game board
        if self.selection1=='X':
            cv2.rectangle(self.mygame,(670,400),(800,530),self.moveHLcolor,9)
            self.selection2='O'
        else:
            cv2.rectangle(self.mygame,(820,400),(950,530),self.moveHLcolor,9)
            self.selection2='X'

    def shader(self):
        self.mygame=np.zeros([self.windowheight,self.windowwidth,3],dtype=np.uint8)
        self.mygame[:,:]=self.bgcolour
        cv2.line(self.mygame,(210,30),(210,600),self.gridcolour,self.thickness)
        cv2.line(self.mygame,(420,30),(420,600),self.gridcolour,self.thickness)
        cv2.line(self.mygame,(30,210),(600,210),self.gridcolour,self.thickness)
        cv2.line(self.mygame,(30,420),(600,420),self.gridcolour,self.thickness)
        cv2.rectangle(self.mygame,(670,400),(800,530),(23,13,4),2)
        cv2.rectangle(self.mygame,(820,400),(950,530),(23,13,4),2)
        cv2.circle(self.mygame,(735,465),45,self.Ocolour,self.thickness) # O
        cv2.line(self.mygame,(850,430),(920,500),self.Xcolour,self.thickness) # X
        cv2.line(self.mygame,(920,430),(850,500),self.Xcolour,self.thickness) # X
        cv2.putText(self.mygame,f'Player {self.selection1}',(640,100),cv2.FONT_HERSHEY_COMPLEX,1, (255,255,255),2)
        cv2.putText(self.mygame,f'Player {self.selection2}',(840,100),cv2.FONT_HERSHEY_COMPLEX,1, (255,255,255),2)
        cv2.line(self.mygame,(810,80),(810,180),(255,255,255),4)
        cv2.line(self.mygame,(640,120),(980,120),(255,255,255),4)
        cv2.putText(self.mygame,str(self.player1),(700,160),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
        cv2.putText(self.mygame,str(self.player2),(900,160),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

    def isGameOver(self):
        if self.isWinner():
            return True
        for i in range(3):
            for j in range(3):
                if self.gamestate[i][j]==' ':
                    return False
        cv2.imshow('Tic Tac Toe',self.mygame)
        cv2.waitKey(500)
        return True

    # is somebody winner
    def isWinner(self):
        # horizontal
        if self.gamestate[0][0]==self.gamestate[0][1] and self.gamestate[0][1]==self.gamestate[0][2] and self.gamestate[0][0]!=' ':
            if self.selection1==self.gamestate[0][0]:
                self.player1+=1
                self.player1move=True
            else:
                self.player2+=1
                self.player1move=False
            for _ in range(105-50,525+50,2):
                cv2.line(self.mygame,(105-50,105),(_,105), self.wincolor,16)
                cv2.imshow('Tic Tac Toe',self.mygame)
                cv2.waitKey(1)
            cv2.waitKey(400)
            return True
        if self.gamestate[1][0]==self.gamestate[1][1] and self.gamestate[1][1]==self.gamestate[1][2] and self.gamestate[1][1]!=' ':
            if self.selection1==self.gamestate[1][1]:
                self.player1+=1
                self.player1move=True
            else:
                self.player2+=1
                self.player1move=False
            for _ in range(105-50,525+50,2):
                cv2.line(self.mygame,(105-50,315),(_,315), self.wincolor,16)
                cv2.imshow('Tic Tac Toe',self.mygame)
                cv2.waitKey(1)
            cv2.waitKey(400)
            return True
        if self.gamestate[2][0]==self.gamestate[2][1] and self.gamestate[2][1]==self.gamestate[2][2] and self.gamestate[2][2]!=' ':
            if self.selection1==self.gamestate[2][2]:
                self.player1+=1
                self.player1move=True
            else:
                self.player2+=1
                self.player1move=False
            for _ in range(105-50,525+50,2):
                cv2.line(self.mygame,(105-50,525),(_,525), self.wincolor,16)
                cv2.imshow('Tic Tac Toe',self.mygame)
                cv2.waitKey(1)
            cv2.waitKey(400)
            return True

        # vertical
        if self.gamestate[0][0]==self.gamestate[1][0] and self.gamestate[1][0]==self.gamestate[2][0] and self.gamestate[0][0]!=' ':
            if self.selection1==self.gamestate[0][0]:
                self.player1+=1
                self.player1move=True
            else:
                self.player2+=1
                self.player1move=False
            for _ in range(105-50,525+50,2):
                cv2.line(self.mygame,(105,105-50),(105,_), self.wincolor,16)
                cv2.imshow('Tic Tac Toe',self.mygame)
                cv2.waitKey(1)
            cv2.waitKey(400)
            return True
        if self.gamestate[0][1]==self.gamestate[1][1] and self.gamestate[1][1]==self.gamestate[2][1] and self.gamestate[1][1]!=' ':
            if self.selection1==self.gamestate[1][1]:
                self.player1+=1
                self.player1move=True
            else:
                self.player2+=1
                self.player1move=False
            for _ in range(105-50,525+50,2):
                cv2.line(self.mygame,(315,105-50),(315,_), self.wincolor,16)
                cv2.imshow('Tic Tac Toe',self.mygame)
                cv2.waitKey(1)
            cv2.waitKey(400)
            return True
        if self.gamestate[0][2]==self.gamestate[1][2] and self.gamestate[1][2]==self.gamestate[2][2] and self.gamestate[2][2]!=' ':
            if self.selection1==self.gamestate[2][2]:
                self.player1+=1
                self.player1move=True
            else:
                self.player2+=1
                self.player1move=False
            for _ in range(105-50,525+50,2):
                cv2.line(self.mygame,(525,105-50),(525,_), self.wincolor,16)
                cv2.imshow('Tic Tac Toe',self.mygame)
                cv2.waitKey(1)
            cv2.waitKey(400)
            return True
                
        # diagonals
        if self.gamestate[0][0]==self.gamestate[1][1] and self.gamestate[1][1]==self.gamestate[1][1]==self.gamestate[2][2] and self.gamestate[0][0]!=' ':
            if self.selection1==self.gamestate[0][0]:
                self.player1+=1
                self.player1move=True
            else:
                self.player2+=1
                self.player1move=False
            for _ in range(105-50,525+50,2):
                cv2.line(self.mygame,(_,_),(_,_), self.wincolor,16)
                cv2.imshow('Tic Tac Toe',self.mygame)
                cv2.waitKey(1)
            cv2.waitKey(400)
            return True
        if self.gamestate[2][0]==self.gamestate[1][1] and self.gamestate[1][1]==self.gamestate[0][2] and self.gamestate[1][1]!=' ':
            if self.selection1==self.gamestate[1][1]:
                self.player1+=1
                self.player1move=True
            else:
                self.player2+=1
                self.player1move=False
            for _ in range(105-50,525+50,2):
                cv2.line(self.mygame,(_,525+105-_),(_,525+105-_), self.wincolor,16)
                cv2.imshow('Tic Tac Toe',self.mygame)
                cv2.waitKey(1)
            cv2.waitKey(400)
            return True

    # the display move function
    def displayMove(self):
        for i in range(3):
            for j in range(3):
                if self.gamestate[i][j]=='O':
                    cv2.circle(self.mygame,(105+210*j,105+210*i),self.Oradius,self.Ocolour,self.thickness)
                elif self.gamestate[i][j]=='X':
                    cv2.line(self.mygame,(50+210*j,50+210*i),(160+210*j,160+210*i),self.Xcolour,self.thickness)
                    cv2.line(self.mygame,(160+210*j,50+210*i),(50+210*j,160+210*i),self.Xcolour,self.thickness)

    # reset the game
    def resetgame(self):
        self.mygame[:,:]=self.bgcolour
        cv2.line(self.mygame,(210,30),(210,600),self.gridcolour,self.thickness)
        cv2.line(self.mygame,(420,30),(420,600),self.gridcolour,self.thickness)
        cv2.line(self.mygame,(30,210),(600,210),self.gridcolour,self.thickness)
        cv2.line(self.mygame,(30,420),(600,420),self.gridcolour,self.thickness)
        cv2.rectangle(self.mygame,(670,400),(800,530),(23,13,4),2)
        cv2.rectangle(self.mygame,(820,400),(950,530),(23,13,4),2)
        cv2.circle(self.mygame,(735,465),45,self.Ocolour,self.thickness) # O
        cv2.line(self.mygame,(850,430),(920,500),self.Xcolour,self.thickness) # X
        cv2.line(self.mygame,(920,430),(850,500),self.Xcolour,self.thickness) # X
        for i in range(3):
            for j in range(3):
                self.gamestate[i][j]=' '

# define mouse callback function
def mouseCall(event,xpos,ypos,*args):
    if cv2.EVENT_LBUTTONDOWN==event:
        sel=None
        if game.player1move:
            sel=game.selection1
        else:
            sel=game.selection2
        if xpos<210 and xpos>0:
            if ypos>0 and ypos<210 and game.gamestate[0][0]==' ':
                game.gamestate[0][0]=sel
                game.player1move=not(game.player1move)
            elif ypos>210 and ypos<420 and game.gamestate[1][0]==' ':
                game.gamestate[1][0]=sel
                game.player1move=not(game.player1move)
            elif ypos>420 and ypos<630 and game.gamestate[2][0]==' ':
                game.gamestate[2][0]=sel
                game.player1move=not(game.player1move)
        elif xpos>210 and xpos<420:
            if ypos>0 and ypos<210 and game.gamestate[0][1]==' ':
                game.gamestate[0][1]=sel
                game.player1move=not(game.player1move)
            elif ypos>210 and ypos<420 and game.gamestate[1][1]==' ':
                game.gamestate[1][1]=sel
                game.player1move=not(game.player1move)
            elif ypos>420 and ypos<630 and game.gamestate[2][1]==' ':
                game.gamestate[2][1]=sel
                game.player1move=not(game.player1move)
        elif xpos>420 and xpos<630:
            if ypos>0 and ypos<210 and game.gamestate[0][2]==' ':
                game.gamestate[0][2]=sel
                game.player1move=not(game.player1move)
            elif ypos>210 and ypos<420 and game.gamestate[1][2]==' ':
                game.gamestate[1][2]=sel
                game.player1move=not(game.player1move)
            elif ypos>420 and ypos<630 and game.gamestate[2][2]==' ':
                game.gamestate[2][2]=sel
                game.player1move=not(game.player1move)

# Create the window
cv2.namedWindow('Tic Tac Toe')

# set mouse callback function
cv2.setMouseCallback('Tic Tac Toe',mouseCall)

game=TicTacToe()

# start program loop
while True:
    cv2.imshow('Tic Tac Toe',game.mygame)
    game.shader()
    if game.player1move:
        if game.selection2=='X':
            cv2.rectangle(game.mygame,(670,400),(800,530),game.moveHLcolor,9)
        else:
            cv2.rectangle(game.mygame,(820,400),(950,530),game.moveHLcolor,9)
    else:
        if game.selection1=='X':
            cv2.rectangle(game.mygame,(670,400),(800,530),game.moveHLcolor,9)
        else:
            cv2.rectangle(game.mygame,(820,400),(950,530),game.moveHLcolor,9)
    game.displayMove()
    if game.isGameOver():
        game.resetgame()
    if cv2.waitKey(1) & 0xff==ord('q'):
        bg=cv2.blur(game.mygame,(18,18))
        cv2.putText(bg,'THANKS FOR PLAYING',(330,310),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
        cv2.imshow('Tic Tac Toe',bg)
        cv2.waitKey(1000)
        break
cv2.destroyAllWindows()