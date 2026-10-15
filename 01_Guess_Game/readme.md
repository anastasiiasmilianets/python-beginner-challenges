# Number Guessing Game

A simple command-line game where you choose the range and try to guess a randomly generated number, with hints after every guess.

## How it works

The program:
- Asks you to choose the upper limit of the range (e.g. 50 means the secret number is between 1 and 50)
- Picks a random secret number within that range
- Asks you to guess it
- Tells you if your guess was too high or too low, and gives you a hint
  (e.g. "Try a number higher than 42")
- Checks that your input is a valid number and asks again if it isn't
- Counts how many attempts it took you to win

## Run it

```
python number_guessing_game.py

```

## What I practiced

- Loops (`while True` with `break` and `continue`)
- Conditionals (`if/elif/else`)
- Input validation with `isdigit()`
- Converting types (`str` to `int`)
- Variables and counters
- f-strings for formatted output
- The `random` module
