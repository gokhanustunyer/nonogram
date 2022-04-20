from tkinter import *
import numpy as np
import random


class Game:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("800x700")
        self.window.title("Adını Bilmediğim Japon Oyunu")
        self.window.resizable(False,False)
        self.sit = 'square'
        self.point = 0
        self.squares = 0

        self.soul = 5
        self.game_size = 10

        soulLabel = Label(text=f"{self.soul}  ",font="arial 40 bold")
        soulLabel.pack()
        soulLabel.place(x=50,y=50)

        # SITUATION BUTTONS

        sitButtonSQ = Button(text="SQUARE",font="arial 15 bold",width=7,command= lambda x = 'square':self.changeSit(x))
        sitButtonSQ.pack()
        sitButtonX = Button(text="X",font="arial 15 bold",width=4,command= lambda x = 'X':self.changeSit(x))
        sitButtonX.pack()
        sitButtonSQ.place(x=10)
        sitButtonX.place(x=120)

        # CREATE A MATRIX FOR CONTROL THE GAME
        self.controlMatrix = np.array([0]*(self.game_size**2)).reshape(self.game_size,self.game_size)

        # PLANT RANDOM SQUARES FROM CONTROL MATRIX
        self.plantSquares()

        # PLACE INFORMATIONS
        self.placeInfo()

        # CREATE BUTTONS
        for x in range(self.game_size):
            for y in range(self.game_size):
                button = Button(text="",width=3,font="arial 20 bold",bg="white")
                if self.sit == 'square':
                    button['command'] = lambda x = x,y=y,b = button:self.place(x,y,b)
                else:
                    button['command'] = lambda x = x,y=y,b = button:self.place(x,y,b)
                button.place(x=200+y*60,y=150+x*55)

    def placeInfo(self):
        self.valuesY = []
        for x in range(self.game_size):
            self.values = []
            count = 0
            for y in range(self.game_size):
                if self.controlMatrix[y][x] == 1:
                    count += 1
                else:
                    if count != 0:
                        self.values.append(count)
                    count = 0
                if y == self.game_size-1:
                    if self.controlMatrix[y][x] == 1:
                        self.values.append(count)
            self.valuesY.append(self.values)

        self.valuesX = []
        for x in range(self.game_size):
            self.values = []
            count = 0
            for y in range(self.game_size):
                if self.controlMatrix[x][y] == 1:
                    count +=1
                else:
                    if count != 0:
                        self.values.append(count)
                    count = 0
                if y == self.game_size-1:
                    if self.controlMatrix[x][y] == 1:
                        self.values.append(count)
            self.valuesX.append(self.values)

        self.placeLabels()



    def placeLabels(self):
        # PLACE FOR AXIS Y
        for i in range(len(self.valuesY)):
            for j in range(len(self.valuesY[i])):
                labelY = Label(text=self.valuesY[i][j],font='Consolas 12 bold')
                labelY.pack()
                labelY.place(x=i*60+225,y=j*30)

        # PLACE FOR AXIS X
        for i in range(len(self.valuesX)):
            for j in range(len(self.valuesX[i])):
                labelX = Label(text=self.valuesX[i][j],font='Consolas 12 bold')
                labelX.pack()
                labelX.place(x=j*30,y=165+i*55)

    def changeSit(self,char):
        self.sit = char

    def place(self,x,y,button):
        if self.sit == 'square':
            button.config(bg="gray10")
        else:
            button.config(text="X")

        self.isSquare(x,y,button)

        soulLabel = Label(text=f"{self.soul}  ",font="arial 40 bold")
        soulLabel.pack()
        soulLabel.place(x=50,y=50)
        
        self.checkGameOver()
        self.checkWon()

    def checkGameOver(self):
        if self.soul == 0:
            canvas = Canvas(self.window,width=800,height=700)
            canvas.pack()

            gameOverLabel = Label(text="GAME OVER",font="Consolas 50 bold",fg="red")
            gameOverLabel.pack()
            gameOverLabel.place(x=240,y=300)

    def checkWon(self):
        if self.point == self.squares:
            canvas = Canvas(self.window,width=800,height=700)
            canvas.pack()

            gameOverLabel = Label(text="YOU WON",font="Consolas 50 bold",fg="green")
            gameOverLabel.pack()
            gameOverLabel.place(x=240,y=300)

    def isSquare(self,x,y,button):

        if self.sit == 'square':
            if self.controlMatrix[x][y] == 0:
                self.soul -= 1
                button.config(bg="white")
            else:
                self.point += 1
                button['command'] = []
                self.controlMatrix[x][y] = 0
        else:
            if self.controlMatrix[x][y] == 1:
                self.soul -= 1
                button.config(text="")
            else:
                button['command'] = []


    def plantSquares(self):
        self.limit = random.randint(60,100)
        for square in range(self.limit):
            x = random.randint(0,self.game_size-1)
            y = random.randint(0,self.game_size-1)

            self.controlMatrix[x][y] = 1

        self.getSquareNum()
    
    def getSquareNum(self):
        for i in self.controlMatrix:
            for j in i:
                if j != 0:
                    self.squares += 1

g1 = Game()
g1.window.mainloop()