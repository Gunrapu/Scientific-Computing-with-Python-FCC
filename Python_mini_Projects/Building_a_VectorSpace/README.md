# Vector Operations in 2D and 3D Space

This project implements vector operations in 2D (R2Vector) and 3D (R3Vector) space, including addition, subtraction, scalar multiplication, dot product, and cross product for 3D vectors.

## Overview

The R2Vector and R3Vector classes provide a comprehensive suite of operations for vector arithmetic in two-dimensional and three-dimensional space. These operations are essential for various applications in physics, computer graphics, and engineering.

## Features

- **R2Vector Class:**

    - Vector norm calculation
    - Vector addition
    - Vector subtraction
    - Scalar multiplication
    - Dot product
    - Comparison operators (equality, inequality, less than, greater than)

- **R3Vector Class:**

    - Inherits all features of R2Vector
    - Cross product

## Getting Started
### Prerequisites
- Python 3.x
### Installation
No installation is required. Simply download or clone the repository to your local machine.

## Usage

1. Define vectors in 2D and 3D space:

        from vectors import R2Vector, R3Vector

        # 2D Vectors
        v1 = R2Vector(x=2, y=3)
        v2 = R2Vector(x=0.5, y=1.25)

        # 3D Vectors
        v3 = R3Vector(x=2, y=3, z=1)
        v4 = R3Vector(x=0.5, y=1.25, z=2)

2. Perform vector operations:

        # Addition
        v_add = v3 + v4

        # Subtraction
        v_sub = v3 - v4

        # Scalar multiplication
        v_mul_scalar = v3 * 2

        # Dot product
        v_dot = v3 * v4

        # Cross product (only for 3D vectors)
        v_cross = v3.cross(v4)

## Credits

This project is part of my coursework for Freecodecamp and contributes to my certificate project.