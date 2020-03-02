'''
still erases some one or two of the solved values 2-25-2020

'''

from random import randint
import turtle
from turtle import *
import tkinter.font
from tkinter import *
import sys

import drawBoardLarger  # draws game board
import startingData   # gets 12 binary and matching hexadecimal numbers


screen = Screen()
screen.setup(width=1200, height=800, startx=10, starty=10)
index = []
eraseble = []
t = turtle.Turtle()
t.hideturtle()
turtle.speed(0)
drawBoardLarger
CList = startingData.startingData()
count1 = 0
for i in CList:
        indexEntry = [CList[count1][0], CList[count1][1]]
        index.append(indexEntry)   # index[0][0] = 0, type(index[0][0] = <class 'int'>)
        count1 +=1

matchCount = 0
pastGuesses = 0
listofPossibles = ['00', '01', '02', '03', '04', '10', '11', '12', '13', '14', '20', '21', '22', '23', '24', '30', '31', '32', '33', '34', '40', '41', '42', '43', '44']
thisGameListofPs = listofPossibles[:]


def erasableWrite(tortoise, name, font, align, reuse=None):
    # tracks place numbers and values so they can be removed and replaced
    eraser = turtle.Turtle() if reuse is None else reuse
    eraser.hideturtle()
    eraser.up()
    eraser.setposition(tortoise.position())
    eraser.write(name, font=font, align=align)
    return eraser

def printBoard():
    #  Puts place number in the board
    global t, eraseble
    counter = 0
    startX = -280
    startY = -295
    textValue = ''
    for i in range(5):
        for k in range(5):
            textValue = CList[counter][1]
            t.penup()
            t.goto(startX, startY)
            t.pendown()
            eraseble.append(erasableWrite(t, textValue, font=("New Times Roman", 18, "normal"), align="center"))
            startX += 140
            counter +=1
        startY += 140
        startX = -280

def getFirst():
    # gets the place number of the first guess to reveal the value
    textInput = screen.textinput("Concentration Game", "type your first choice")
    return textInput

def getSecond():
    # gets the place number for the second guess to reveal the value
    textInput = screen.textinput("Concentration Game", "type your second choice")
    return textInput

def validate(stringNumber):
    # checks to see if the place number is a valid guess
    global thisGameListofPs
    if stringNumber in thisGameListofPs:
        return stringNumber, False
    else:
        return "", True 


printBoard()  # calls the function and displays the place numbers

def flipCard(choice):
    #  takes the place number and replaces it with the value (0b or 0x)
    global gameTupleList, index, eraseble, CList
    gameTupleList = CList[:]
    firstInt = 0
    counti = 0
    count1 = 0
    textValue = ''
    for x in index:
        if x[1] == choice:
            firstInt = index[counti][0]
        counti +=1
    newEntry = (gameTupleList[firstInt])
    nextStep = (newEntry[0], newEntry[2], newEntry[1], newEntry[3])
    gameTupleList[firstInt] = nextStep
    counter = newEntry[0]
    counterX = counter % 5
    counterY = int(counter/5)
    startX = -280
    startY = -295
    startY += 140 * counterY
    startX += 140 * counterX
    t.penup()
    t.goto(startX, startY)
    print('eraseble 1 at counter {}'.format(counter))
    eraseble[counter].clear()
    textValue = nextStep[1]
    if len(textValue) <= 3:
        erasableWrite(t, textValue, font=("New Times Roman", 18, "normal"), align="center", reuse= eraseble[counter])
    else:
        erasableWrite(t, textValue, font=("New Times Roman", 14, "normal"), align="center", reuse= eraseble[counter])
    return nextStep

    
def gotAMatch():
    messagebox.showinfo('A Match!', 'Excellent : > )')
    
def notAMatch():
    messagebox.showinfo('NOT a match!', 'sorry : > (')

def nextLoop():
    global choice1, choice2, matchCount, CList, thisGameListofPs, gameTupleList, index, eraseble, pastGuesses 
    while matchCount <= 11:
        notValid = True
        while notValid:
            choice1 = getFirst()
            choice1, notValid = validate(choice1)
        card1 = flipCard(choice1)
        notValid = True
        while notValid:
            choice2 = getSecond()
            choice2, notValid = validate(choice2)
        card2 = flipCard(choice2)
        pastGuesses +=1
        if (card1[3] == 1000) or (card2[3] == 1000):
            countLOP = 0
            for n in thisGameListofPs:
                if n == choice1:
                    del thisGameListofPs[countLOP]
                countLOP +=1
            countLOP = 0
            for n in thisGameListofPs:
                if n == choice2:
                    del thisGameListofPs[countLOP]
                countLOP +=1
            if card1[3] == 1000:
                one2M = card2[3]
                cardDone = card2[0]
                for n in CList:
                    if n[3] == card2[3] and n[0] != card2[0]:
                            removePossible = n[1]
            else:
                one2M = card1[3]
                cardDone = card2[0]
                for n in CList:
                    if n[3] == card1[3] and n[0] != card1[0]:
                            removePossible = n[1]
            counter = 0
            for n in CList:
                if  one2M == n[3] and n[0] != cardDone:
                    print('eraseble 2 at n[0] {}'.format(n[0]))
                    eraseble[n[0]].clear()
                    textValue = n[2]
                    counterX = n[0] % 5
                    counterY = int(n[0]/5)
                    startX = -280
                    startY = -295
                    startY += 140 * counterY
                    startX += 140 * counterX
                    t.penup()
                    t.goto(startX, startY)
                    if len(textValue) <= 3:
                        erasableWrite(t, textValue, font=("New Times Roman", 18, "norl"), align="center", reuse= eraseble[counter])
                    else:
                        erasableWrite(t, textValue, font=("New Times Roman", 14, "normal"), align="center", reuse= eraseble[counter])
                    countLOP = 0
                    for m in thisGameListofPs:
                        if m == removePossible:
                            del thisGameListofPs[countLOP]
                            countLOP +=1
                        else:
                            countLOP +=1
                    counter +=1
            gotAMatch()
            matchCount += 1
            CList = gameTupleList[:]
        elif (card1[3] == card2[3]):
            countLOP = 0
            for n in thisGameListofPs:
                if n == choice1:
                    del thisGameListofPs[countLOP]
                countLOP +=1
            countLOP = 0
            for n in thisGameListofPs:
                if n == choice2:
                    del thisGameListofPs[countLOP]
                countLOP +=1
            gotAMatch()
            matchCount += 1
            CList = gameTupleList[:]
        else:
            notAMatch()
            listReset = [choice1, choice2]
            counter = 0
            for a in listReset:
                gameTupleList = CList[:]
                for item in index:
                    if item[1] == a:
                        counter = item[0]
                counterX = counter % 5
                counterY = int(counter/5)
                startX = -280
                startY = -295
                startY += 140 * counterY
                startX += 140 * counterX
                t.penup()
                t.goto(startX, startY)
                print('eraseble 3 at counter {}'.format(counter))
                eraseble[counter].clear()
                textValue = gameTupleList[counter][1]
                erasableWrite(t, textValue, font=("New Times Roman", 18, "normal"), align="center", reuse=eraseble[counter])

    messageFinal = 'In only ' + str(pastGuesses) +' guesses!'
    messagebox.showinfo('Congratulations! You solved the game!', messageFinal)
    continueGame = screen.textinput("Play Again? Yes or No", "Type y or n")
    if continueGame.lower() == 'n':
        screen.bye()
        sys.exit()
        
    elif continueGame.lower() == 'y':
        turtle.clearscreen()
        CList = startingData.startingData()
        thisGameListofPs = listofPossibles[:]
        drawBoardLarger
        eraseble = []
        printBoard()
        pastGuesses = 0
        matchCount = 0
        nextLoop()

nextLoop()

mainloop()
