# Number Guessing Game

A simple command-line game where you try to guess a randomly generated number
between 1 and 100, with hints after every guess.

## How it works

The program:
- Picks a random secret number between 1 and 100
- Asks you to guess it
- Tells you if your guess was too high or too low, and gives you a hint
  (e.g. "Try a number higher than 42")
- Counts how many attempts it took you to win

## Run it

```
python number_guessing_game.py

```

## What I practiced

- Loops (`while True` with `break`)
- Conditionals (`if/elif/else`)
- Variables and counters
- f-strings for formatted output
- The `random` module