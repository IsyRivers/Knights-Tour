import os
import time
import random
 
class KnightsTour:
    
    global ROWS 
    global COLS
    global RJUST
    RJUST = 3
    ROWS = 8
    COLS = 8

    def start(self):
        board = self.__createBoard()
        self.__showBoard(board)
        row = self.__getRow()
        col = self.__getCol()
        moveDirection = self.__moveDirection()

        start = time.time()
    
        self.__knightsTour(board, row, col, 1, moveDirection)

        finish = time.time()
        print(finish - start)

        self.__showBoard(board)
        self.__writeBoardToFile(board, row, col, finish)
        input()        

    
    def __createBoard(self):
        return self.__clearBoard()

    def __clearBoard(self):
        board = [[0 for row in range(ROWS)] for col in range(COLS)]
        return board

    def __getRow(self):
        correct = 1
        while(correct):
            row = int(input("Which row would you like to start in? "))
            if (row > 0 and row <= ROWS):
                correct = 0
        return row - 1
 
    def __getCol(self):
        correct = 1
        while(correct):
            col = int(input("Which column would you like to start in? "))
            if (col > 0 and col <= COLS):
                correct = 0
        return col - 1

    def __adjustRow(self, index, currRow):
        choice = { 2 : self.__addOne(currRow),
                     8 : self.__addOne(currRow),
                     1 : self.__subOne(currRow),
                     7 : self.__subOne(currRow),
                     4 : self.__addTwo(currRow),
                     6 : self.__addTwo(currRow),
                     3 : self.__subTwo(currRow),
                     5 : self.__subTwo(currRow)}
        return choice[index]

    def __adjustCol(self, index, currCol):
        choice = { 5 : self.__addOne(currCol),
                     6 : self.__addOne(currCol),
                     3 : self.__subOne(currCol),
                     4 : self.__subOne(currCol),
                     7 : self.__addTwo(currCol),
                     8 : self.__addTwo(currCol),
                     1 : self.__subTwo(currCol),
                     2 : self.__subTwo(currCol)}
        return choice[index]
    
    def __addOne(self, currentValue):
        return currentValue + 1

    def __subOne(self, currentValue):
        return currentValue - 1

    def __addTwo(self, currentValue):
        return currentValue + 2

    def __subTwo(self, currentValue):
        return currentValue - 2

    def __moveDirection(self, direction = [1, 2, 3, 4, 5, 6, 7, 8], shuffle = True):

        if shuffle == True:
            random.shuffle(direction)

        return direction

    def __printDirection(self, direction):
        for i in range(ROWS):
            print(direction[i])

    def __knightsTour(self, board, row, col, moveNum, moveDirection):
        if row < 0 or col < 0 or row >= ROWS or col >= COLS:
            return False

        if board[row][col] != 0:
            return False

        board[row][col] = moveNum

        if((moveNum <= ((ROWS * COLS) * .6)) and (moveNum % 3 == 0)):
            moveDirection = self.__moveDirection(moveDirection, True)
            #print(moveDirection)
            
        if moveNum >= ((ROWS * COLS) - 5):
            self.__showBoard(board) 

        if moveNum == ROWS * COLS:
            return True
        
        for i in range(0,8):
            if self.__knightsTour(board, self.__adjustRow(moveDirection[i], row), self.__adjustCol(moveDirection[i], col), moveNum + 1, moveDirection):
                return True       
        
        board[row][col] = 0
        return False

    def __printDash(self):
        print("   ", end = "")
        for i in range(ROWS):
            print("------", end = "")
        print()  

    def __showBoard(self, board):
        print("   ", end = "")
        for i in range(ROWS):
            print(str(i + 1).rjust(3),  end = "   ")
        print()    
        self.__printDash()

        #main board, row number, 1st col, 2nd col, ..., Nth col
        for i in range(ROWS):
            print(str(i + 1).rjust(RJUST), sep= " | ", end=""  ) #first Number
            print("| ", end = "") #row count seperator
            #prints row's col values
            for j in range(COLS):    
                print( str(board[i][j]).center(3), end = "" )#cell value
                print(" | ", end = "" )#seperator
            print()
            self.__printDash()

    def __writeBoardToFile(self, board, row, col, runTime):
        wFile = open('result.txt', 'a')
        wFile.write('Row = ' + str(row + 1) + ', Col = ' + str(col + 1) + '\n')
        wFile.write('Calculate Time (sec): ' + str(runTime)+ '\n')
        wFile.write('Calculate Time (min): ' + str(runTime/60) + '\n')
        
        wFile.write('   ')
        for i in range(ROWS):
            wFile.write(str(i + 1).rjust(3))
            wFile.write("   ")
        wFile.write('\n')

        wFile.write("   ")
        for i in range(ROWS):
            wFile.write("------")
        wFile.write('\n')

        for i in range(ROWS):
            wFile.write(str(i + 1).rjust(RJUST))
            wFile.write('|')
            #prints row's col values
            for j in range(COLS):    
                wFile.write( str(board[i][j]).center(3))#cell value
                wFile.write(' | ')#seperator
            wFile.write('\n')

            wFile.write("   ")
            for i in range(ROWS):
                wFile.write("------")
            wFile.write('\n')
        wFile.write('\n')
        wFile.close() 
