# CSC2103: Algorithmic Problem Solving

**Three classic problems. Three different ways to solve them.**

This repository contains three Python command-line programs built for our CSC2103 Data Structures and Algorithms group project. Each explores a different problem-solving strategy: making a greedy choice, building on smaller solutions, or finding a practical route when the perfect one is harder to calculate.

The algorithms are implemented manually, with user input, validation, and step-by-step results. No third-party packages are needed.

## What's inside?

| Problem | Approach | The goal |
| --- | --- | --- |
| **Activity Selection** | Greedy algorithm | Fit as many non-overlapping activities as possible into a schedule |
| **0/1 Knapsack** | Dynamic programming | Maximise the value of selected items without exceeding a weight limit |
| **Travelling Salesman** | Nearest Neighbour heuristic | Find a short round trip through a set of cities |

### 01. Activity Selection

Say you have several activities that overlap. Which ones should you choose to fit in the most?

The program sorts activities by finish time using a **manually implemented selection sort**. It then works through the list, choosing an activity whenever it starts at or after the previous selection has finished. The result shows the sorted activities, the ones selected, and how many fit.

This is a **greedy algorithm**: choosing the earliest finishing activity leaves as much room as possible for what comes next.

### 02. 0/1 Knapsack

You have a bag with limited capacity and a collection of items, each with a weight and value. The challenge is finding the most valuable combination. You either take an item or leave it. There's no splitting it.

The program uses **dynamic programming** to compare those two choices for each item and available capacity. It builds a table of results, then traces backwards to reveal the chosen items, their total weight, and the maximum value.

### 03. Travelling Salesman

What's a reasonably short route that visits every city once and gets you back to where you started?

This version uses the **Nearest Neighbour heuristic**. From the chosen starting city, it repeatedly visits the closest unvisited city before returning home. You can follow every leg of the journey and see the final route and distance.

It's quick to calculate, but **the shortest-looking next step doesn't always produce the shortest overall tour**. Changing the starting city can change the result, too.

## Run the programs

All you need is **Python 3** and a terminal. Download or clone the repository, open its folder, and run whichever problem you'd like to try:

```bash
python "Problem1_activity_selection(1).py"
python Problem2_knapsack.py
python Problem3_nearest_neighbour.py
```

On systems where `python` points to Python 2, use `python3` instead. Each program prompts you for its inputs and asks you to correct invalid entries.

## Example test cases

<details>
<summary><strong>Activity Selection</strong></summary>

Enter these activities as `(start, finish)`:

```text
1: (1, 2)    2: (3, 4)    3: (0, 6)
4: (5, 7)    5: (8, 9)    6: (5, 9)
```

**Expected:** Activities 1, 2, 4, and 5. Maximum: **4 activities**.

</details>

<details>
<summary><strong>0/1 Knapsack</strong></summary>

Set the capacity to `5`:

| Item | Weight | Value |
| --- | ---: | ---: |
| Camera | 2 | 3 |
| Laptop | 3 | 4 |
| Book | 4 | 5 |
| Tablet | 5 | 8 |

**Expected:** Tablet selected. Total weight: **5**. Maximum value: **8**.

</details>

<details>
<summary><strong>Travelling Salesman</strong></summary>

Use cities `A, B, C, D`, starting at `A`, with these symmetric distances in kilometres:

```text
A-B: 10    A-C: 15    A-D: 20
B-C: 35    B-D: 25    C-D: 30
```

**Expected:** `A -> B -> D -> C -> A`, covering **80 km**.

</details>

## Complexity and trade-offs

| Problem | Time | Space | Why |
| --- | --- | --- | --- |
| Activity Selection | `O(n²)` | `O(n)` | Manual selection sort takes the most time |
| 0/1 Knapsack | `O(nC)` | `O(nC)` | Stores results for `n` items and capacities up to `C` |
| Nearest Neighbour TSP | `O(n²)` | `O(n²)` | Checks remaining cities and stores a distance matrix |

The knapsack approach finds the best combination for the given integer inputs, but its table grows with the capacity. Nearest Neighbour is faster to work through than exhaustive route search, though it **doesn't guarantee the globally shortest route**.

## A few implementation notes

- The code uses **Python 3** without external sorting, graph, or optimisation libraries.
- Functions separate input handling, algorithm logic, and output.
- Input checks cover valid counts and capacities, activity times, item details, unique non-empty city names, positive distances, and the selected starting city.
- Activity Selection assumes one activity at a time; Knapsack uses positive integer weights and values; TSP assumes complete, symmetric distances between cities.

The focus of this project is understanding **why** each approach works, what it produces, and where its limits are.