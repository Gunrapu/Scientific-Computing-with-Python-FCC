# Probability Calculator Project
## Overview

This project simulates experiments involving drawing colored balls from a hat and calculates the probability of drawing a specific combination of balls. It includes two main components: the `Hat` class and the `experiment` function.

## Hat Class

The `Hat` class represents a collection of colored balls.

### Constructor

- ****init(balls):** Initializes the hat with colored balls. Accepts keyword arguments where the key is the color of the ball and the value is the number of balls of that color.

### Methods

- **draw(amount):** Draws a specified number of balls randomly from the hat. Returns a list of drawn balls.

### Features

- **Dynamic Initialization:** Accepts variable numbers of balls of different colors during object creation.

- **Random Drawing:** Allows drawing a specified number of balls randomly from the hat.

## experiment Function

The `experiment` function simulates multiple experiments of drawing balls from a hat and calculates the probability of drawing a specified combination of balls.

### Parameters

- **hat:** An instance of the `Hat` class representing the hat of balls.

- **expected_balls:** A dictionary specifying the expected number of balls for each color after drawing.

- **num_balls_drawn:** The number of balls to draw in each experiment.

- **num_experiments:** The number of experiments to run.

### Results

- **probability:** The probability of drawing the expected combination of balls, calculated as the ratio of successful experiments to the total number of experiments.

### Example Usage

        from hat_simulation import Hat, experiment

        # Create a hat with specific numbers of colored balls
        hat = Hat(red=5, blue=3, green=2)

        # Define the expected number of balls to draw
        expected_balls = {"red": 2, "green": 1}

        # Perform the experiment with the hat, expected balls, and number of draws
        num_draws = 3
        num_trials = 10000
        probability = experiment(hat, expected_balls, num_draws, num_trials)

        # Print the probability result
        print(f"Probability of drawing {expected_balls} from the hat in {num_draws} draws: {probability:.4f}")

## Tests

1. Creation of hat object should add correct contents.
2. The draw method in hat class should reduce number of items in contents.
3. The draw method should behave correctly when the number of balls to extract is bigger than the number of balls in the hat.
4. The experiment method should return a different probability.

## Credits

This project is the certificate project from Freecodecamp.