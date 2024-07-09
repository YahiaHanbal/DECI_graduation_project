# DECI_graduation_project
Digital Egypt Cubs Initiative graduation project level two.
## Features

- Text-based adventure game
- Randomly generated encounters with different monsters
- Choices that affect the player's score and game outcome
- Clean and modular code design
- No global variables used

## Project Details

This project incorporates several programming concepts learned during my studies, such as:

- Functions and encapsulation
- Control flow with loops and conditionals
- Input and output handling
- Use of data structures (lists)
- Randomization

## How to Play

1. Clone or download the repository.
2. Run the game script using Python.
3. Follow the prompts to make choices and navigate through the game world.
4. Enjoy the adventure and try to achieve the highest score!

## Code Structure

The main game logic is encapsulated within functions to avoid the use of global variables, ensuring clean and maintainable code. The primary functions include:

- `print_pause(*m)`: Prints messages with a delay.
- `ask_player(choice1, choice2, func1, func2)`: Prompts the player to make a choice and calls the appropriate function.
- `defend(way, is_rusty=True)`: Handles the defense actions of the player.
- `cave()`: Handles the events that occur when the player enters the cave.
- `field()`: Handles the events that occur when the player is in the field.
- `house()`: Handles the events that occur when the player approaches the house.
- `print_score()`: Prints the player's current score.
- `replay()`: Prompts the player to replay the game.
- `game()`: Initializes the game and starts the adventure.

