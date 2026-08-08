# CSC2103 Algorithmic Problem-Solving Project

This repository contains three console-based Python programs developed for the CSC2103 Data Structures and Algorithms group project. Each program demonstrates a different algorithmic approach through manual implementation, user input, validation, and clearly formatted output.

## Selected Problems

| Problem | Algorithmic approach | Selected solution |
| --- | --- | --- |
| 1 | Greedy algorithm | Activity Selection Problem |
| 2 | Dynamic programming | 0/1 Knapsack Problem |
| 3 | Heuristic algorithm | Travelling Salesman Problem using the Nearest Neighbour heuristic |

## Problem 1: Activity Selection

The Activity Selection program finds the maximum number of non-overlapping activities that can be completed by one person or resource.

The program first sorts all activities by their finish times using a manually implemented selection sort. It then makes the greedy choice of selecting the activity that finishes earliest. Each remaining activity is selected only if its start time is at or after the finish time of the last selected activity.

The program displays:

- All activities sorted by finish time
- The selected non-overlapping activities
- The maximum number of activities that can be completed

## Problem 2: 0/1 Knapsack

The 0/1 Knapsack program selects items that produce the highest total value without exceeding the knapsack's weight capacity. Each item can be selected once or not selected at all.

The program uses dynamic programming to build a table of smaller subproblem results. For each item and capacity, it compares the value obtained by including the item with the value obtained by excluding it. It then works backwards through the completed table to identify the selected items.

The program displays:

- The completed dynamic-programming table
- The selected items and their weights and values
- The total selected weight
- The maximum obtainable value

## Problem 3: Travelling Salesman Problem

The Travelling Salesman program uses the Nearest Neighbour heuristic to find an efficient route that visits every city once and returns to the starting city.

Starting from the city chosen by the user, the algorithm repeatedly travels to the nearest unvisited city. After all cities have been visited, it returns to the starting city. This heuristic finds a route efficiently, but it does not always guarantee the shortest possible route. The result may also change when a different starting city is selected.

The program displays:

- Each travel step and its distance
- The complete route
- The total distance travelled

## Repository Files

| File | Purpose |
| --- | --- |
| `Problem1_activity_selection(1).py` | Greedy solution for the Activity Selection Problem |
| `Problem2_knapsack.py` | Dynamic-programming solution for the 0/1 Knapsack Problem |
| `Problem3_nearest_neighbour.py` | Nearest Neighbour heuristic for the Travelling Salesman Problem |
| `README.md` | Project overview and instructions |

## Requirements

- Python 3
- A terminal or an editor with a Python terminal, such as Visual Studio Code

No third-party packages are required.

## Running the Programs

1. Download or clone the repository.
2. Open the project folder in Visual Studio Code.
3. Open the integrated terminal.
4. Run the required program using one of the following commands:

```bash
python "Problem1_activity_selection(1).py"
python Problem2_knapsack.py
python Problem3_nearest_neighbour.py
```

On systems where `python` refers to Python 2, use `python3` instead.

## Sample Test Cases

### Activity Selection

Activities entered as `(start time, finish time)`:

```text
Activity 1: (1, 2)
Activity 2: (3, 4)
Activity 3: (0, 6)
Activity 4: (5, 7)
Activity 5: (8, 9)
Activity 6: (5, 9)
```

Expected result: Activities 1, 2, 4, and 5 are selected. The maximum number of activities is 4.

### 0/1 Knapsack

```text
Knapsack capacity: 5

Camera: weight 2, value 3
Laptop: weight 3, value 4
Book: weight 4, value 5
Tablet: weight 5, value 8
```

Expected result: The Tablet is selected. The total weight is 5 and the maximum value is 8.

### Travelling Salesman Problem

```text
Cities: A, B, C, D
Starting city: A

A-B: 10 km    A-C: 15 km    A-D: 20 km
B-C: 35 km    B-D: 25 km    C-D: 30 km
```

Expected route: `A -> B -> D -> C -> A`

Expected total distance: `80 km`

## Input Validation

The programs check the user's input before processing it:

- Activity counts, item counts, capacities, weights, and values must meet their required integer limits.
- Every activity's finish time must be greater than its start time.
- Item names and city names cannot be empty.
- City names must be unique.
- Distances must be positive numbers.
- The selected starting city must be one of the available cities.

Invalid input produces an explanatory message and asks the user to try again.

## Time and Space Complexity

| Program | Time complexity | Space complexity | Main reason |
| --- | --- | --- | --- |
| Activity Selection | `O(n^2)` | `O(n)` | Manual selection sort dominates the `O(n)` greedy selection pass |
| 0/1 Knapsack | `O(nC)` | `O(nC)` | A table is built for `n` items and capacity `C` |
| Nearest Neighbour TSP | `O(n^2)` | `O(n^2)` | Each city searches the remaining cities, and all distances are stored in a matrix |

## Limitations

- Activity Selection assumes that only one activity can take place at a time.
- The 0/1 Knapsack implementation uses positive integer weights, values, and capacity. Its memory usage increases as the capacity grows.
- The Nearest Neighbour program assumes positive, symmetric distances between every pair of cities.
- Nearest Neighbour is a heuristic, so its route may not be globally optimal.

## Implementation Notes

The core algorithms are implemented manually without sorting, graph, optimization, or machine-learning libraries. The code is divided into functions for input, processing, and output to keep each program readable, reusable, and easy to test.