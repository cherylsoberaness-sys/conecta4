# Connect4 (Python)

A console-based implementation of the classic **Connect Four** game written in Python.

This project focuses on practicing **object-oriented design**, **game state management**, and **rule-based move evaluation** using an oracle system.

---

## Overview

Connect Four is a two-player game where players take turns dropping pieces into a vertical board. The goal is to connect **three pieces in a row** vertically, horizontally, or diagonally.

This implementation runs in the terminal and supports:

- Computer vs Computer
- Computer vs Human

Computer players use an **oracle-based system** to analyze the board before choosing a move.

Human players can also **request help from the oracle** to see the classification of each column before deciding where to play.

---

## Features

- Console-based Connect Four gameplay
- Computer vs Computer and Computer vs Human modes
- Rule-based AI move evaluation using an oracle
- Human players can request oracle recommendations during gameplay
- Board visualization using `BeautifulTable`
- ASCII game title using `PyFiglet`
- Automated tests using `pytest`
- Modular object-oriented architecture

---

## Oracle Decision System

The AI uses an **oracle** to evaluate each column before making a move.

Instead of choosing randomly, the oracle simulates possible outcomes and classifies each column according to its consequences.


## Technologies Used

- Python
- Pytest
- BeautifulTable
- PyFiglet

---

## Learning Goals

This project was developed as a learning exercise to practice:

- Object-oriented design
- Separation of responsibilities
- Game state management
- Simulation of future game states
- Rule-based decision systems
- Automated testing with pytest

---

## Future Improvements

Possible improvements include:

- Implementing a deeper AI strategy 
- Improving difficulty levels
- Enhancing board visualization
- Adding a graphical interface
