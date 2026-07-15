# Should I Walk, Bike, or Drive?

A simple command-line tool that recommends the best way to get somewhere 
based on on the weather, the distance to travel, and the availability of a vehicle.

## How it works
The program asks for:
- Distance in miles
- Whether it's raining
- Whether you have a bike, car, or rideshare app

Based on your answers, it suggests walking, biking, or taking a car/rideshare — 
with fallback logic if your first option isn't available (e.g. no bike → car instead).

## Run it
python should_i_walk_bike_drive.py

## What I practiced
- Nested conditionals (if/elif/else)
- Boolean logic (and/or/not)
- Loops with continue/break
- User input handling
- Designing fallback logic so every branch has a "plan B", not just a dead end