## Problem

Problem Link: https://leetcode.com/problems/valid-anagram/

## Solution 1

Anagram is when the characters of another word are the same when rearranged

1. Filter out test cases that do NOT have the same number of characters
2. If the other string does not contain character being iterated through then return false

(doesn't work exactly how it's intended)

## Solution 2 (implemented):

1. Sort both strings from a to z and then compare

Submission Link: https://leetcode.com/problems/valid-anagram/submissions/1210159812/
