## Problem Link

Link: https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/

## Solution

Thought process:

A number is given and you just have to return the largest number and there's practically no restrictions

Parity - Both numbers swapped have to be even or odd so can't sort least to greatest

Made an algorithm to iterate through array once and again inside it
If the number in the 1st iteration is bigger than the number in the 2nd iteration and if they are the same parity
(so if both even or both odd) then swap the number's place

Submission Link: https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/submissions/903840430/