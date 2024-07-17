# Random Password Generator

This script generates random passwords based on specified criteria such as length, number of numeric characters, special characters, uppercase letters, and lowercase letters.

## Overview

The `generate_password` function uses the `secrets` module to generate a random password that meets specified constraints. It ensures that the password includes the required number of numeric characters, special characters, uppercase letters, and lowercase letters by checking against regular expressions.

## Features

- Generates random passwords with customizable length.
- Ensures password complexity by including numeric characters, special characters, uppercase letters, and lowercase letters.
- Uses Python's `secrets` module for secure randomization.

## Getting Started
### Prerequisites
- Python 3.x
### Installation
No installation is required. Simply download or clone the repository to your local machine.
## Usage

1. Run the script to generate a random password:

        python generate_password.py

## Example

        # Example usage of the generate_password function

        import re
        import secrets
        import string

        def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

            # Define the possible characters for the password
            letters = string.ascii_letters
            digits = string.digits
            symbols = string.punctuation

            # Combine all characters
            all_characters = letters + digits + symbols

            while True:
                password = ''
                # Generate password
                for _ in range(length):
                    password += secrets.choice(all_characters)
        
                constraints = [
                    (nums, r'\d'),
                    (special_chars, fr'[{symbols}]'),
                    (uppercase, r'[A-Z]'),
                    (lowercase, r'[a-z]')
                ]

                # Check constraints        
                if all(
                    constraint <= len(re.findall(pattern, password))
                    for constraint, pattern in constraints
                ):
                    break
    
            return password
    
    if __name__ == '__main__':
        new_password = generate_password()
        print('Generated password:', new_password)

## Credits

This project is part of my coursework for Freecodecamp and contributes to my certificate project.