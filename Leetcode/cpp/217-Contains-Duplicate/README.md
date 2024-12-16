# Problem

Problem Link: https://leetcode.com/problems/contains-duplicate/

# Approach

Worst time complexity in this case is O(n)

Thinking of using a frequency array

If the value is 1 store it's frequency in first index of an array

When you see that the frequency is greater or equal to 1 terminate and return true

# Solution

For this problem I had to use unordered_sets in C++

Initially I thought it was like a map in javascript or like a dictionary in python

However, an unordered_set is to more so to check for frequencies of 1 (which is what we needed in this case)

Submission Link: https://leetcode.com/problems/contains-duplicate/submissions/1479925173

