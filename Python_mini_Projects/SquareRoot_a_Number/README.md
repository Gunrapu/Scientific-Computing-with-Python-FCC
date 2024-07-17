# Square Root Calculation using Bisection Method

This function calculates the square root of a number using the Bisection Method.

## Overview

The `square_root_bisection` function uses the Bisection Method to approximate the square root of a given number. It iteratively narrows down the range where the square of a midpoint is closest to the target square, within a specified tolerance.

## Features

- Calculates square roots using the Bisection Method.
- Handles positive numbers, zero, and raises an error for negative numbers.

## Getting Started
### Prerequisites
- Python 3.x
### Installation
No installation is required. Simply download or clone the repository to your local machine.

## Usage

1. Import the `square_root_bisection` function into your Python project.

        from square_root_bisection import square_root_bisection

2. Use the function to calculate the square root of a number.

        N = 16
        square_root_bisection(N)

## Example

        # Example usage of the square_root_bisection function

        def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
            if square_target < 0:
                raise ValueError('Square root of negative number is not defined in real numbers')
            if square_target == 1:
                root = 1
                print(f'The square root of {square_target} is 1')
            elif square_target == 0:
                root = 0
                print(f'The square root of {square_target} is 0')
            else:
                low = 0
                high = max(1, square_target)
                root = None
        
                for _ in range(max_iterations):
                    mid = (low + high) / 2
                    square_mid = mid**2

                    if abs(square_mid - square_target) < tolerance:
                        root = mid
                        break

                    elif square_mid < square_target:
                        low = mid
                    else:
                        high = mid

                if root is None:
                    print(f"Failed to converge within {max_iterations} iterations.")
                else:   
                    print(f'The square root of {square_target} is approximately {root}')
    
            return root

    if __name__ == "__main__":
        N = 16
        square_root_bisection(N)

## Credits

This project is part of my coursework for Freecodecamp and contributes to my certificate project.