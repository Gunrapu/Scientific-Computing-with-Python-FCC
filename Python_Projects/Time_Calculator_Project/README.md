# Time Calculator Project
## Overview

The `add_time` function calculates the time after adding a specified duration to a given starting time. It handles AM/PM notation and can optionally include the starting day of the week.

## Features

- **12-hour Format Handling:** Converts time between 12-hour AM/PM format and 24-hour format as needed.
- **Day Handling:** Optionally calculates and displays the day of the week after adding days to the start time.
- **Duration Calculation:** Adds the specified duration accurately, accounting for minutes rolling over to hours.
- **Multiple Day Support:** Supports calculations spanning multiple days and adjusts the day of the week accordingly.

## Function Signature

        def add_time(start, duration, start_day=''):
            # implementation

## Parameters

- **`start`**: The starting time in the format 'hh
AM' or 'hh
PM'.
- **`duration`**: The duration to add in the format 'hh
'.
- **`start_day`** (optional): The starting day of the week (e.g., 'Monday', 'Tuesday', etc.).

## Results

A string representing the resulting time after adding the duration. It includes:

- The new time in the 12-hour clock format.
- AM/PM notation.
- Optionally specifies days later and the day of the week.

## Examples
### Example 1:

        print(add_time('3:30 PM', '2:12', 'Monday')) 

output:

        5:42 PM, Monday (next day)

### Example 2:

        print(add_time('11:55 AM', '3:12'))

output:

        3:07 PM

## Tests

1. Calling add_time('3:30 PM', '2:12') should return '5:42 PM'.
2. Calling add_time('11:55 AM', '3:12') should return '3:07 PM'.
3. Expected time to end with '(next day)' when it is the next day.
4. Expected period to change from AM to PM at 12:00.
5. Calling add_time('2:59 AM', '24:00') should return '2:59 AM (next day)'.
6. Calling add_time('11:59 PM', '24:05') should return '12:04 AM (2 days later)'.
7. Calling add_time('8:16 PM', '466:02') should return '6:18 AM (20 days later)'.
8. Expected adding 0:00 to return the initial time.
9. Calling add_time('3:30 PM', '2:12', 'Monday')should return '5:42 PM, Monday'.
10. Calling add_time('2:59 AM', '24:00', 'saturDay') should return '2:59 AM, Sunday (next day)'.
11. Calling add_time('11:59 PM', '24:05', 'Wednesday') should return '12:04 AM, Friday (2 days later)'.
12. Calling add_time('8:16 PM', '466:02', 'tuesday') should return '6:18 AM, Monday (20 days later)'.

## Credits

This project is the certificate project from Freecodecamp.