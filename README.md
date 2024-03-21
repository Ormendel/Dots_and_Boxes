# SquareGame
The game's idea goes to 2 pupils who have learnt with me while I was a teenager.

## How to decide who wins?
* One goal of the game is to tell the score of each player in every turn.
* The player with the most squares has won.
<p align="center">
  <img src="https://www.wikihow.com/images/thumb/9/9a/Play-Dots-and-Boxes-Step-1.jpg/v4-460px-Play-Dots-and-Boxes-Step-1.jpg.webp" alt="Scores_goal1">
</p>

However implementing this will be a problem, because of edge cases.
** One of them (and the most popular) is when player1 makes a move and creates a rectangle.
** When the score's algorithm takes place we need to check each edge and determine for each square if it's indeed of player1.
** If one of the squares (square is a cell in a 2D matrix) is of player2, we can't add #squares in the rectangle to player1 's score.

* In the 2nd version, the player who makes the **first** square/rectangle wins the game

<p align="center">
  <img src="(https://media1.tenor.com/m/O2ZgbQ--_XUAAAAC/spongebob-squarepants-spongebob.gif)" alt="Goal2">
</p>


  


