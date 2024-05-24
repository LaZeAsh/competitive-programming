## Problem

Ranking: 800

Problem Link: https://codeforces.com/problemset/problem/263/A

## Analysis

- Row is from top to bottom (1 - 5)
- Column is from left to right (1 - 5)
- OBJECTIVE: Locate the number 1 and move it to the center (where row 3 and column 3 intersect)

## Solution

- Make a 2D array to hold the values of the matrix
- Make a for loop inside a for loop
- Store the row and column value in variables (add + 1 since the arrays are 0 indexed)
- return absolute value or 3 - row + absolute value of 3 - column