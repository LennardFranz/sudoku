import numpy as np
from sudoku_examples import *


def rule_checker (x,y,N, matrix):
    sudoku = matrix
    for i in range(9):
        if sudoku[i][y] == N:
            return False
    for j in range(9):
        if sudoku[x][j] == N:
            return False
    x_box = x//3
    y_box = y//3
    for i in range((x_box*3), (x_box*3)+3):
        for j in range((y_box*3), (y_box*3)+3):
            if sudoku[i][j] == N:
                return False
    return True

def solve(matrix):
    sudoku = matrix
    for i in range(9):
        for j in range(9): #starting in the upper left corner of the sudoku with an empty space
            if sudoku[i][j] == 0:
                for n in range(1, 10):
                    if rule_checker(i, j, n, sudoku) == True:
                        sudoku[i][j] = n #inserting the smallest valid number
                        #print(np.matrix(sudoku))
                        solve(sudoku) #recursively calling solve
                        sudoku[i][j] = 0

                        #backtracking constrain
                        #if the puzzle isnt completly solvable with this iteration the next
                        #valid number (line 43-45) in this space is tried.
                return
    global solution
    solution = np.matrix(sudoku)

def human_solve(matrix):
    sudoku = matrix
    for i in range(9):
        for j in range(9):
            possibility = 0
            if sudoku[i][j] == 0: #looking for all empty spaces
                for N in range(1,10):
                    bool = rule_checker(i,j,N, sudoku)
                    if bool == True:     #checking for all valid numbers in emtpy space
                        possibility += 1 #count all valid numbers in empty space
                        N_solve = N      #save valid number for solving
            if possibility == 1:         #in all spaces where only one number is possible N_solve is inserted
                sudoku[i][j] = N_solve
                human_solve(sudoku)            #recursively calling the function
                #after inserting N_solve in line 56 now new
                solution = np.matrix(sudoku)
                return solution



#solve(matrix = sudoku)
#print(solution)

print(human_solve(matrix = sudoku))



















