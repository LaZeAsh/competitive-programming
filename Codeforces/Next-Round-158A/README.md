## Problem

Ranking: 800

Problem Link: https://codeforces.com/problemset/problem/158/A

## Analysis

- Value of n tells us how many scores there are (n = 8 means 8 integers)
- Value of k tells us what placement to look at and what value to compare to
- This is not 0 indexed

## Solution

- Get values of n and k
- Put all of the values in an array
- Check if the value of k is a "positive" (aka nonzero value)
- if its nonzero iterate forward in the array and increment counter whenever the iterate value is equal to the value at k
- if its zero iterate backwards until you get a nonzero value set counter to index + 1 (as arrays are zero indexed)
- return counter