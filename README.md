# Spiffing Tea

## Introduction
Spiffing Tea is a whimsical game where you play as a teacup collecting teabags and cookies, while dodging salt shakers. Eating salt reduces your lives, but eating cookies replenishes them. As you collect more teabags, the difficulty level increases. Put your reflexes to the test and see how long you can survive in this charming and addictive game.

## Gameplay
Made from scratch,this game is a pixelart game with art drawn or taken from icons8 and modified using pixelto library.

## Language and Frameworks
Main Language: Python
>Pygame

## Code

Spiffing Tea uses the Pygame library to create a game window and provide functionalities to create and control game characters, display graphics, play sounds, and handle user inputs.
Some notable parts of the code include:
- Button class: Defines a button object that can be clicked and perform an action when clicked. The interact() method of the class checks whether the button is clicked and performs the action associated with it.
- Bird and Item classes: Defines game characters. Bird represents the main character of the game, and Item represents items that the character can collect. Both classes contain attributes such as position, image, and velocity.
- item_sel(), item_create(), and item_update() functions: These functions define the probability of item generation and create and update the position of items on the screen. They take arguments such as item arrays, position arrays, and item types to create and update items.
- on_collision() function: Detects whether the character collides with an item on the screen and performs an action such as collecting the item or losing a life.
- spiffy_meter() function: Handles the logic of a tea meter that decreases over time and gives the character an ability to jump when full.
