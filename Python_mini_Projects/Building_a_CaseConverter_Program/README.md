# Convert PascalCase or camelCase to snake_case

This function converts PascalCase or camelCase strings to snake_case.

## Overview

The `convert_to_snake_case` function converts a PascalCase or camelCase string to snake_case by inserting underscores (_) before each uppercase letter and converting all letters to lowercase.

## Features

- Converts PascalCase or camelCase strings to snake_case.

## Getting Started
### Prerequisites
- Python 3.x
### Installation
No installation is required. Simply download or clone the repository to your local machine.

## Usage

1. Import the `convert_to_snake_case` function into your Python project.

        from snake_case_converter import convert_to_snake_case

2. Use the function to convert a PascalCase or camelCase string:

        snake_case_string = convert_to_snake_case('IAmAPascalCasedString')
        print(snake_case_string)  # Output: i_am_a_pascal_cased_string

## Example

        # Example usage of the convert_to_snake_case function

        def convert_to_snake_case(pascal_or_camel_cased_string):
            snake_cased_char_list = [
                '_' + char.lower() if char.isupper()
                else char
                for char in pascal_or_camel_cased_string
            ]
            return ''.join(snake_cased_char_list).strip('_')

        def main():
            print(convert_to_snake_case('IAmAPascalCasedString'))

        if __name__ == "__main__":
            main()

## Credits

This project is part of my coursework for Freecodecamp and contributes to my certificate project.