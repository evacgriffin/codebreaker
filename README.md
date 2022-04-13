# Codebreaker
#### Video Demo:  <https://youtu.be/n6caeG9RUJc>
#### Overview:
For this project, I used pygame in Python to create a digital version of the board game
[Mastermind](https://en.wikipedia.org/wiki/Mastermind_(board_game)).
The goal is to guess the randomly generated four-color code within
the selected number of guesses. After each guess, the game displays a hint. Using
deduction and process of elimination, the player uses the hints to arrive at the
correct answer.

#### Specifics:
The code consists of the following color options: red, yellow, green, blue, black, or
white. The game randomly selects four colors from this list to generate the code.
The hints are displayed as small dots, either black or white. A black dot means 
that the player has guessed a correct color that is in the correct position. A white
dot means that the player has guessed a correct color in an incorrect position.

There are three difficulties: easy, normal, or hard. In easy and normal difficulty, the
player has 12 attempts to guess the correct code. Hard difficulty allows the player to only 
guess 8 times. While each color can only appear in the correct code once in 
easy difficulty, the code can include multiple instances of the same color in normal and
hard difficulties.

Here are some possible game examples:

Easy difficulty - 12 guesses - correct code: RED, GREEN, BLACK, BLUE

Normal difficulty - 12 guesses - correct code: YELLOW, YELLOW, YELLOW, WHITE

Hard difficulty - 8 guesses - correct code: GREEN, RED, GREEN, BLACK

#### Walkthrough
When the program is started, the player first sees the Main Menu. Here, he or she can click 
the "Rules" button to review the game rules. In Main Menu, one of three difficulties
can be selected. The default is "Normal". When the "Start" button is clicked, a new 
game begins. Music switches from the menu music to the gameplay music. The gameplay
music consists of 4 songs that run on a loop. Depending on the chosen difficulty, the
player is presented with a board that either contains 12 or 8 rows for guesses. These
rows are initially empty. On the left edge of the screen, the gutter is displayed. 
Here, the player can select a color pin to fill into an empty guess slot (or change a
slot's color before hitting "Submit"). The "Submit" button is disabled until the player
fills in all four slots for the current guess. When the player clicks "Submit", the game
evaluates the guess and displays the appropriate hint. Throughout the game, the "Pause"
button can be clicked at any time. Here, the player can review the rules, resume the
current game, or reset the game and return to the main menu. If the player guesses the
correct code within the number of available turns, he or she wins the game. If the
player runs out of turns before guessing the correct code, the game is lost. Once the
player wins or loses, the game displays the outcome and the correct code. The player
now has the option to restart the game with the same difficulty or return to the main 
menu.

#### Implementation:
This game was implemented using pygame. However, for learning purposes, I wrote the main
object classes from scratch. The code is implemented using a state manager that switches
between gameplay and menu states. I created classes for the different menus, buttons, rules
display, and other clickable objects like the slots and pins on the "board". I also
added music to the game, which is handled using the mixer and sound functionality of 
pygame.

Initially, I wrote a working version of this game without using a state manager, but 
the logic flow quickly became too complex. To make the code more efficient and
allow for easier additions and changes to the code in the future, I switched to using
the state manager.

#### Future Additions:
In the future, I plan on adding the following features to this project: A timer that
keeps track of how long it takes a player to guess the code, a leaderboard, a tutorial,
different visual themes (different colors, or even pictures instead of solid colors),
more difficulties, and either a web version or mobile version to allow my 
family and friends to easily play the game on their devices.

#### Files:
The sound folder includes the sound files used for the game.

main.py - Initializes the game window, defines some global game variables, runs the
main game loop

manager.py - State manager, handles the game state stack

state.py - Handles hover, select, and click functionality

menu.py - All other menu objects inherit from this class, handles basic drawing of the
menu rectangle/display

main_menu.py - Loads and plays the menu music, defines header, subtitle, radio buttons 
to select difficulty, Rules button, and Start button

rules.py - Displays the rules for the game and the "Back" button

radio_button.py - Defines radio buttons, ensures that only one radio button from the
radio group is selected at a time

button.py - Defines push buttons

gameplay.py - Draws the game board, initializes turns, slots, and pins, loads and plays
the gameplay music (4 songs repeated on a loop), sets number of rounds depending on 
chosen difficulty, generates random game code, enables and disables the "Submit" button,
displays all previous hints, checks if game was won or lost

pause_menu.py - Displays the pause menu and its buttons

pin.py - Class that defines game pins (pins are the colored circles located in the gutter)

slot.py - Class that defines game slots (empty circles that are filled in with colors
by the player)

turn.py - Handles each turn by enabling the slots for the current turn, locking in the
player's guess, checking the correctness of the guess, creating the hint, and disabling
the slots for the current turn (to ensure players cannot change previous guesses)

end_game.py - Displays the "end-game" message box, correct code, and buttons to
reset or restart the game