## Problem Link

Link: https://leetcode.com/problems/roman-to-integer/ 

## Solution

Thought Process - 

This would generally be an easy problem as you could just turn the string
into an array and copy iterate through all of the values and add the value
of each Roman Numeral to an array

Since IX = 9 and not 11 it will be a bit more challenging as we have to account for greater value afterwards

To solve this I made it so if the previous value is smaller then subtract
from the previous value (twice) because it's being added once

Leetcode submission link: https://leetcode.com/problems/roman-to-integer/submissions/902971654/