# Shortest Path Finder in a Graph

This script finds the shortest path from a starting node to a target node in a graph using Dijkstra's algorithm.

## Overview

The `shortest_path` function calculates the shortest path from a starting node to a target node in a graph represented as an adjacency list. It uses Dijkstra's algorithm, which iteratively selects the node with the smallest distance from the start, updates distances to its neighbors, and tracks the path taken.

## Features

- Finds the shortest path using Dijkstra's algorithm.
- Outputs the shortest distance and path from a starting node to a target node.

## Getting Started
### Prerequisites
- Python 3.x
### Installation
No installation is required. Simply download or clone the repository to your local machine.

## Usage

1. Import the `shortest_path` function into your Python project.

        from shortest_path import shortest_path


2. Use the function to find the shortest path from a starting node to a target node in your graph.

        my_graph = {
            'A': [('B', 5), ('C', 3), ('E', 11)],
            'B': [('A', 5), ('C', 1), ('F', 2)],
            'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
            'D': [('C', 1), ('E', 9), ('F', 3)],
            'E': [('A', 11), ('C', 5), ('D', 9)],
            'F': [('B', 2), ('D', 3)]
        }

        shortest_path(my_graph, 'A', 'F')

## Credits

- This project is part of my coursework for Freecodecamp and contributes to my certificate project.
- **Dijkstra's Algorithm:** Used for finding the shortest path in graphs.