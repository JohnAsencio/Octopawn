# Octopawn solver
### John Asencio

### What is Octopawn?
Octopawn is a 4x4 variant of Hexapawn https://en.wikipedia.org/wiki/HexapawnLinks, where White pawns are represented by P and Black prawns are represented by p. 

### What I did
I implemented a negamax algorithm that solves octopawn and returns the final gameboard and either 1 (side on move wins) or -1 (side on move loses)

### How it went
At first I was confused on how to get started. I did not know where to start. I had to make sure I understood the logic of the game very thoroughly. Once I started my negamax, my logic seemed right, however I kept running into problems. It was all coming from the moves function. It was very hard to find, because I was looking at the wrong spots. It was also very hard to find said bugs because it was hard to test for specific cases. Once I figured out all the bugs the program ran just fine! It was just mostly figuring out the logistics of the game and then testing my game functions to see if the game was doing what it was supposed to do. 

## How to run
python octopawn.py