# Program name:Assignment 8
# Author: Terran Stone
# Description: Tic Tac Tow Game
# Date Created/Modified 11/16/2024
# Notes:
import time
print(time.ctime())

from graphics import *


def player_one_x(win, center):
    #This creates the character that player one will be using.
    offset = 0.25  
    line1 = Line(Point(center.x - offset, center.y - offset), Point(center.x + offset, center.y + offset)).draw(win)
    line2 = Line(Point(center.x - offset, center.y + offset), Point(center.x + offset, center.y - offset)).draw(win)
    line1.setWidth(3)
    line2.setWidth(3)
    line1.setFill("orange")
    line2.setFill("orange")
    
def player_two_circle(win, center):
    #This creates the character that player two will be using.
    circle = Circle(center, 0.3)
    circle.setOutline("green")
    circle.setWidth(4)
    circle.draw(win)
    
def square_center(row, col):
    #This calculates the center of each square on the grid.
    return Point(col + .5, row + .5)

def square_selection(click):
    #This gets the row and column of the clicked square.
    col = int(click.x)
    row = int(click.y)
    return row, col

def full_not_full(spaces):
    #This checks if all squares on the grid are filled.
    for row in spaces:
        if None in row:
            return False
    else:
        return True

def winning(spaces):
    #This checks for a winner.
    for i in range(3):
        if spaces[i][0] == spaces[i][1] == spaces[i][2] and spaces[i][0] is not None:
            return spaces[i][0]
        if spaces[0][i] == spaces[1][i] == spaces[2][i] and spaces[0][i] is not None:
            return spaces[0][i]
    
    if spaces[0][0] == spaces[1][1] == spaces[2][2] and spaces[0][0] is not None:
        return spaces[0][0]
    if spaces[0][2] == spaces[1][1] == spaces[2][0] and spaces[0][2] is not None:
        return spaces[0][2]
    return None
        
        
    
def main():
    #This creates the graphical user interface.
    win = GraphWin("Tic Tac Toe", 900, 750)
    win.setCoords(-.5, -.5, 3.5, 3.5)
    win.setBackground("black")
    message = Text(Point(1.5,-.2), "")
    message.setFill("white")
    message.draw(win)
    
    spaces = [[None, None, None,], #This initialized the 3x3 grid into a list of spaces to be called on later
              [None, None, None,], 
              [None, None, None,]]
    
    
    
    for i in range(1, 4): #This creates the 3x3 game board
        for j in range(1, 4):
            square = Rectangle(Point(j-1, 3-i), Point(j-1+1, 3-i+1))
            square.setOutline("cyan")
            square.setFill("#3e3e3e")
            square.draw(win)
    
    for i in range(9): #This tells the program how many total times turn there will be
        if i % 2 == 0: #This initializes player 1 and insures that player 1 will always go first.
            message.setText("Player 1 (X): Choose your square ") 
            player_one_click = win.getMouse()
            row, col = square_selection(player_one_click)
            if spaces[row][col] is None:
                center = square_center(row, col)
                player_one_x(win, center)
                spaces[row][col] = "X"
                winner = winning(spaces)
                if winner:
                    message.setText("Player 1 wins! Click the window to quit.")
                    break   
                
        else: #player 2 is initialized 
            message.setText("Player 2 (O): Choose your square ")
            player_two_click = win.getMouse()
            row, col = square_selection(player_two_click)
            if spaces[row][col] is None:
                center = square_center(row, col)
                player_two_circle(win, center)
                spaces[row][col] = "O"
                winner = winning(spaces)
                if winner:
                    message.setText("Player 2 wins! Click the window to quit.")
                    break
        
    if not winner: #Game is over when all spaces are taken and there is no winner.
        message.setText("Game over, it's a draw!")
        
    win.getMouse()
    win.close()
if __name__ == "__main__":
    main()
