# Arithmetic Arranger

A brief description of what this project does and who it's for

## Overview

The arithmetic_arranger function takes a list of arithmetic problems and returns a formatted string displaying the problems vertically and side-by-side. Optionally, it can also display the answers.

## Features

- Validates input for correctness.
- Supports addition and subtraction operations.
- Formats up to five arithmetic problems side-by-side.
- Optionally shows the answers.

## Usage
### Function Signature

        def arithmetic_arranger(problems, show_answers=False):
            # implementation

### Parameters

- problems: A list of strings, where each string represents an arithmetic problem (e.g., "32 + 698").
- show_answers: A boolean flag (default False) to optionally display the answers along with the problems.

## Example

        print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

This will output:

           32      3801      45      123
        + 698    -    2    + 43    +  49
        -----    ------    ----    -----

## Error Handling

The function raises ValueError in the following cases:

- More than five problems are provided.
- The operator is not '+' or '-'.
- Operands contain non-digit characters.
- Operands are more than four digits long.

## Tests
        1. arithmetic_arranger(["3801 - 2", "123 + 49"]) should return   3801      123\n-    2    +  49\n------    -----
        2. arithmetic_arranger(["1 + 2", "1 - 9380"]) should return   1         1\n+ 2    - 9380\n---    ------
        3. arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]) should return     3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----
        4. arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]) should return   11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------
        5. arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]) should return 'Error: Too many problems.'
        6. arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]) should return "Error: Operator must be '+' or '-'."
        7. arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]) should return 'Error: Numbers cannot be more than four digits.'
        8. arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]) should return 'Error: Numbers must only contain digits.'
        9. arithmetic_arranger(["3 + 855", "988 + 40"], True) should return     3      988\n+ 855    +  40\n-----    -----\n  858     1028
        10. arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True) should return    32         1      45      123      988\n- 698    - 3801    + 43    +  49    +  40\n-----    ------    ----    -----    -----\n -666     -3800      88      172     1028

## Credits

This project is the certificate project from Freecodecamp.