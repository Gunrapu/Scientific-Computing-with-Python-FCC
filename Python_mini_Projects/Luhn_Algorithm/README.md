# Credit Card Number Verification

This project verifies the validity of a credit card number using the Luhn algorithm.

## Overview

The Luhn algorithm, also known as the "modulus 10" or "mod 10" algorithm, is a simple checksum formula used to validate various identification numbers, including credit card numbers.

## Features

- Validates credit card numbers by applying the Luhn algorithm.
- Handles formatted card numbers (removes spaces and dashes).

## Getting Started
#### Prerequisites
- Python 3.x
#### Installation
No installation is required. Simply download or clone the repository to your local machine.

## Usage

1. Import the credit card verification module into your Python project.

        from credit_card_verification import verify_card_number

2. Provide a credit card number for validation:

        card_number = '4111-1111-4555-111'
        translated_card_number = card_number.replace('-', '')

        if verify_card_number(translated_card_number):
            print('VALID!')
        else:
            print('INVALID!')

## Example

    from credit_card_verification import verify_card_number

    def main():
        card_number = '4111-1111-4555-111'
        translated_card_number = card_number.replace('-', '')
   
        if verify_card_number(translated_card_number):
            print('VALID!')
        else:
            print('INVALID!')

    if __name__ == "__main__":
        main()

## Credits

- This project is part of my coursework for Freecodecamp and contributes to my certificate project.
- **Luhn Algorithm:** Developed by Hans Peter Luhn of IBM in 1954.