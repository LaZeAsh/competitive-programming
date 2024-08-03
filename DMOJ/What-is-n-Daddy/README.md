## Problem

Problem Link: https://dmoj.ca/problem/ccc10j1

Submission Link: https://dmoj.ca/submission/6530727

Problem Difficulty: 3p

## Analysis 

We want to write code that can figure out how many ways it's possible to represent the input digit with our FINGERS.

How many FINGERS does one person have on ONE hand? 5.

That was my original oversight for this problem which caused me to waste a lot of time.

## Solution

The solution is pretty simple after you realize that

I made a for loop which calculates the remainder value of the input value and all the values from 0 to the input value provided. Everytime the remainder was less than the x value it meant that the combo had already been used.

For example: we don't want to count 5, 2 and 2, 5 as 2 but rather 1

This alongside a condition where if we get the remainder as greater than 5 to skip because we only have 5 FINGERS solves this problem.

Took longer than I'd like to admit