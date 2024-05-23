## Problem Link

Link: https://leetcode.com/problems/backspace-string-compare/

## Solution

\# equals the removal of the hashtag and 1 character

Example: "a#bc" results in "bc"

First check if hashtags are even included in the 2 given inputs
If not then return false if they aren't equal (because the strings don't have to be manipulated)

Check the index of the hashtag and if it's 0 then replace only the index of the hashtag
If it's not 0 and it's greater or equal to 1 then find the part you have to change and replace it

Leetcode submission link: https://leetcode.com/problems/backspace-string-compare/submissions/903681284/
