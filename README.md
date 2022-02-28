# Hilo
Hilo game designed for CSE210

Hilo is a game in which the player guesses if the next card drawn by the dealer will be higher or lower than the previous one. Points are won or lost based on whether or not the player guessed correctly.

Rules
Hilo is played according to the following rules.

The player starts the game with 300 points.
Individual cards are represented as a number from 1 to 13.
The current card is displayed.
The player guesses if the next one will be higher or lower.
The the next card is displayed.
The player earns 100 points if they guessed correctly.
The player loses 75 points if they guessed incorrectly.
If a player reaches 0 points the game is over.
If a player has more than 0 points they decide if they want to keep playing.
If a player decides not to play again the game is over.


Design:

1-13 Cards. Could be class?
	Draw card method.
	52 card, 4 of each value
	once drawn goes in "dicard" and cannot be drawn again.
	Resets on new game.
	Could be done as a list, list of lists, or dict. (Could use pop for lists)

Player class
	Keeps track of points
	Resets on new game
	
Game function
	Higher order function, determine outcome with inner functions,
	has ways to end game when no draw.
	ends game when points reach 0 or below
	while True loop that breaks when either two previous conditions are met.
	Gets input from player if higher or lower
	Determines points
	Awards points depending on the outcome of the player's choice.
	
main function
	start game,
	restart game, 
	exit game
	run game