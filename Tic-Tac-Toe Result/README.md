https://py.checkio.org/mission/x-o-referee/share/46411288d0dd63d1c24b3d004cb7e6ea/

You are given a result of a game and you must determine if the game ends in a win or a draw as well as who will be the winner. 
Make sure to return "X" if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D".

A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.

Input: A game result as a list of strings (unicode).

Output: "X", "O" or "D" as a string.

Example:

checkio([
    "X.O",
    "XX.",
    "XOO"]) == "X"

checkio([
    "OO.",
    "XOX",
    "XOX"]) == "O"

checkio([
    "OOX",
    "XXO",
    "OXX"]) == "D"
