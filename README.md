# Integer Line Puzzle
Two players are presented with a line of 100 positive integers. Both players can see every element of the line. The purpose of this program is to test my proposed solution.
## The Game
* Players take turn choosing integers to remove from either side of the line to add to their sum.
* Player 1 goes first.
* Player 2 is free to choose from whichever side they please.
* The player with the largest sum at the end wins. If both players have the same sum they tie.
* **Determine a non-losing strategy for player 1.**
## My Proposed Solution
![equation](https://latex.codecogs.com/svg.latex?%5Ctext%7BLet%20%7D%20L%20%5Ctext%7B%20be%20the%20line%20of%20integers.%20If%20%7D%5Cnewline%20%5Csum_%7Bi%3D1%7D%5En%28-1%29%5E%7Bi+1%7DL_i%5Cgeq0%2C%20%5Ctext%7B%20where%20%7Dn%5Ctext%7B%20is%20the%20current%20size%20of%20the%20line%20and%20%7DL_i%5Ctext%7B%20is%20the%20line%20element%20at%20index%20%7Di%2C%5Cnewline%20%5Ctext%7BThen%20player%201%20should%20choose%20the%20line%20element%20on%20the%20left%2C%20otherwise%20the%20element%20on%20the%20right.%7D)