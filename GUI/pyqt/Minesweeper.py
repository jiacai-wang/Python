import sys
import numpy as np
import random
from PySide2 import QtCore, QtGui, QtWidgets


class Box:

    def __init__(self, isMine):
        self.isMine = isMine
        self.isShown = False
        # Mine cound in surrounding Boxes,
        # with -1 meaning itself is Mine.
        self.surrounding = 0

    def Clicked(self):
        if self.isMine:
            return True
        else:
            return False


def setMines(Map, count):
    # totalBox = Map.size
    width = Map.shape[0]
    height = Map.shape[1]

    while count:
        box = Map[random.randint(0, width-1), random.randint(0, height-1)]
        if box.isMine == False:
            box.isMine = True
            # box.surrounding = -1
            count = count - 1

    for i in range(Map.shape[0]):
        for j in range(Map.shape[1]):
            calcSurrounding(Map, i, j)
            print(Map[i, j].surrounding, end="  ")
        print()
    print()


def calcSurrounding(Map, i, j):
    if Map[i, j].isMine:
        Map[i, j].surrounding = '*'
    else:
        # calculating surrounding mines.
        # careful not to cross the boarder!!!
        # temporarily no elegant way :(
        count = 0

        count = count + (Map[i-1, j-1].isMine if i-1 >= 0 and j-1 >= 0 else 0)
        count = count + (Map[i-1, j].isMine if i-1 >= 0 else 0)
        count = count + (Map[i-1, j+1].isMine if i-1 >=
                         0 and j+1 <= Map.shape[1]-1 else 0)
        count = count + (Map[i, j-1].isMine if j-1 >= 0 else 0)
        count = count + (Map[i, j+1].isMine if j+1 <= Map.shape[1]-1 else 0)
        count = count + (Map[i+1, j-1].isMine if i+1 <=
                         Map.shape[0]-1 and j-1 >= 0 else 0)
        count = count + (Map[i+1, j].isMine if i+1 <= Map.shape[0]-1 else 0)
        count = count + (Map[i+1, j+1].isMine if i+1 <=
                         Map.shape[0]-1 and j+1 <= Map.shape[1]-1 else 0)

        Map[i, j].surrounding = count


def clickBox(Map, i, j):
    if Map[i, j].isShown == False:
        Map[i, j].isShown = True
    else:
        return False
    if Map[i, j].surrounding == '*':
        return True
    elif Map[i, j].surrounding == 0:
        if i-1 >= 0:
            clickBox(Map, i-1, j)
            if j-1 >= 0:
                clickBox(Map, i-1, j-1)
            if j+1 <= Map.shape[1]-1:
                clickBox(Map, i-1, j+1)
        if j-1 >= 0:
            clickBox(Map, i, j-1)
        if j+1 <= Map.shape[1]-1:
            clickBox(Map, i, j+1)
        if i+1 <= Map.shape[0]-1:
            clickBox(Map, i+1, j)
            if j-1 >= 0:
                clickBox(Map, i+1, j-1)
            if j+1 <= Map.shape[1]-1:
                clickBox(Map, i+1, j+1)
    return False


def printMap(Map):
    width = Map.shape[1]
    height = Map.shape[0]
    for i in range(height):
        for j in range(width):
            if Map[i, j].isShown:
                print(Map[i, j].surrounding, end="  ")
            else:
                print("-", end="  ")
        print()
    print()


if __name__ == '__main__':

    width = 10
    height = 10
    mines = 20
    Map = np.array([[Box(False) for i in range(width)] for j in range(height)])
    setMines(Map, mines)

    while True:
        printMap(Map)
        i, j = map(int, input("which to dig: i j\n").split())
        if clickBox(Map, i, j):
            print("Boom!!!")
            continue
        else:
            print(Map[i, j].surrounding)
            print("lucky.")
