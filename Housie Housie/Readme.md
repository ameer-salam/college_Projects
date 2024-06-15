# Housie Housie Number Display

A Python-based number display system for the Housie Housie game, developed to enhance the visibility of the game during events by projecting the numbers on a screen.

## Problem Statement

During the flagship event "Samarthya 2024" organized by SSIT, we faced a challenge in managing the Housie Housie game. Traditionally, the picked numbers were manually placed on a board for the audience to see. This manual process was cumbersome and inefficient, especially for large audiences. To solve this, I developed a Python application that allows the organizers to input the picked number, confirm it, and display it dynamically on a projector. The application also includes an undo feature to correct any mistakes.

## About Housie Housie

Housie Housie, also known as Bingo, is a popular game where players mark off numbers on a card as they are randomly called out. The aim is to mark off a specific pattern on the card before other players. This game is often played in large gatherings, requiring clear and efficient number management.

## Features

- **Dynamic Number Display**: Enter a number and confirm it to mark it on the screen.
- **Undo/Redo Functionality**: Easily correct mistakes with undo (Ctrl+Z) and redo (Ctrl+Y) actions.
- **Resizable Window**: The application window can be resized and maximized for better visibility.
- **Customizable Grid**: Numbers from 1 to 90 are displayed in a 10x9 grid.

## How to Use

1. Run the script using Python.
2. Enter the number in the input box and press `Enter`.
3. Confirm the number when prompted.
4. Use `Ctrl+Z` to undo and `Ctrl+Y` to redo if needed.

## Installation

Ensure you have Python and Pygame installed. You can install Pygame using pip:

```bash
pip install pygame
