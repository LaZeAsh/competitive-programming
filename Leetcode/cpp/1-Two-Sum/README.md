# Problem

Problem Link: 

Classic 2 Sum Problem, if 2 indices of an array add up to the target then return those 2 indices. There's always going to be a solution

# Approach

The solution I had in mind was O(n^2), make 2 for loops 1 nested within the other and if 2 indices of the list adds up to the target then define those values in the return list and return the list.

Optimized Solution:

Using a hashmap store value and it's indice in a key value format. While iterating to make these saves calculate the difference between the target and nums[i] if this value is in the map then return the indice of that value and the i value you're currently on.

Otherwise define that value in the key and it's indice as it's value and continue iterating

This is O(n)

Submission Link: https://leetcode.com/problems/two-sum/submissions/1481878131
