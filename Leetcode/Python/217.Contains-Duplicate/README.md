## Problem

Problem Link: https://leetcode.com/problems/contains-duplicate/

## Solution

This seems like a  pretty easy problem I can encounter this 2 ways, a loop within a loop which I don't really want to do as even though I am not familiar with the concept of time complexity I believe this wouldn't be the most effective solution

Approach:

Sort the list least to greatest or greatest to least using sort function and then if any of the values are the same then
return True

Make an if statement to see if the i value is the length of the list - 1 return false because there's no more values to compare to

Submission Link: https://leetcode.com/problems/contains-duplicate/submissions/904158748/