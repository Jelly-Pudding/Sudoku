# Overview

A sudoku solver that uses backtracking. Backtracking is a recursive algorithm that prunes the search for a solution down significantly. It is much faster than sheer brute-force
as whole branches can be eliminated off the basis of whether a given move is valid, or whether a given move leads to an impossible to solve board configuration further down the line. 

The sudoku.py script stores the sudoku class. The sudoku class creates the board as a three-dimensional list, and it can check whether the current board configuration obeys the rules
of the game.

The gui.py script allows one to edit a blank board of sudoku. When the board has been filled out, it also allows one to see the backtracking process in action.

## Controls ##

When the gui.py script is running, one can edit the board by hovering their mouse over the desired square and clicking a number on their keyboard. Alternatively, one can also click
on the square until the desired number is reached. When the board has been configured appropriately, the enter key will allow one to see the backtracking process in real time over the
GUI board. 
