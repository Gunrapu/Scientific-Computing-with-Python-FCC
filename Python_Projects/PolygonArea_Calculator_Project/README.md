# Polygon Area Calculator Project
## Overview

This project includes two classes, Rectangle and Square, for representing geometric shapes.

## Rectangle Class

The `Rectangle` class represents a rectangle with specified width and height.

### Constructor

- **init(width, height):** Initializes a rectangle with the given width and height.

### Methods

- **set_width(width):** Sets a new width for the rectangle.

- **set_height(height):** Sets a new height for the rectangle.

- **get_area():** Calculates and returns the area of the rectangle (**`width * height`**).

- **get_perimeter():** Calculates and returns the perimeter of the rectangle (**`2 * (width + height)`**).

- **get_diagonal():** Calculates and returns the diagonal length of the rectangle using the Pythagorean theorem.

- **get_picture():** Returns a string representation of the rectangle as a picture made of asterisks (**`*`**). Returns "Too big for picture." if either dimension is greater than 50.

### Features

- **Dimension Management:** Allows setting and retrieving width and height.

- **Geometric Calculations:** Computes area, perimeter, and diagonal length of the rectangle.

- **Visual Representation:** Generates a visual depiction of the rectangle as a string of asterisks.

### Example Usage

        rect = Rectangle(10, 5)
        print(rect.get_area())      # Output: 50
        rect.set_height(3)
        print(rect.get_perimeter()) # Output: 26
        print(rect)                 # Output: Rectangle(width=10, height=3)
        print(rect.get_picture())   # Output: **********
                                    #         **********
                                    #         **********

## Square Class

The `Square` class extends the `Rectangle` class to represent a square.

### Constructor

- **init(side):** Initializes a square with equal side lengths.

### Methods

- **set_side(side):** Sets a new side length for the square.

- **set_width(side):** Sets a new width (side length) for the square.

- **set_height(side):** Sets a new height (side length) for the square.

### Features

- **Square Specific Methods:** Includes methods for setting side lengths.

- **Inherited Methods:** Inherits methods for geometric calculations and visual representation from the `Rectangle` class.

### Example Usage

        sq = Square(9)
        print(sq.get_area())        # Output: 81
        sq.set_side(4)
        print(sq.get_diagonal())    # Output: 4.0
        print(sq)                   # Output: Square(side=4)
        print(sq.get_picture())     # Output: ****
                                    #         ****
                                    #         ****
                                    #         ****

## Tests

1. The Square class should be a subclass of the Rectangle class.
2. The Square class should be a distinct class from the Rectangle class.
3. A square object should be an instance of the Square class and the Rectangle class.
4. The string representation of Rectangle(3, 6) should be Rectangle(width=3, height=6).
5. The string representation of Square(5) should be Square(side=5).
6. Rectangle(3, 6).get_area() should return 18.
7. Square(5).get_area() should return 25.
8. Rectangle(3, 6).get_perimeter() should return 18.
9. Square(5).get_perimeter() should return 20.
10. Rectangle(3, 6).get_diagonal() should return 6.708203932499369.
11. Square(5).get_diagonal() should return 7.0710678118654755.
12. An instance of the Rectangle class should have a different string representation after setting new values.
13. An instance of the Square class should have a different string representation after setting new values by using .set_side().
14. An instance of the Square class should have a different string representation after setting new values by using .set_width() or set_height().
15. The .get_picture() method should return a different string representation of a Rectangle instance.
16. The .get_picture() method should return a different string representation of a Square instance.
17. The .get_picture() method should return the string Too big for picture. if the width or height attributes are larger than 50.
18. Rectangle(15,10).get_amount_inside(Square(5)) should return 6.
19. Rectangle(4,8).get_amount_inside(Rectangle(3, 6)) should return 1.
20. Rectangle(2,3).get_amount_inside(Rectangle(3, 6)) should return 0.

## Credits

This project is the certificate project from Freecodecamp.