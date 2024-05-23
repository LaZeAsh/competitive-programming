## Problem Link

Link: https://leetcode.com/problems/palindrome-number/ 
## Solution

There was a few obvious conditions I decided to account for

if a number was less than 0 immediately return false

if a number is a single digit number it's automatically a palindrome

To solve the rest of the cases what I did was checked if the first digit
was the same as the last number then 2nd number with 2nd last number etc.

If they were all the same then it returned True but if at any point they
weren't false was returned

## Areas of Improvement

Currently I am going through all numbers from front to back after all the
numbers have been checked I still keep iterating to every single digit

I could implement a solution that stops when the number has been confirmed
and not go through every single digit

Leetcode submission link: https://leetcode.com/problems/palindrome-number/submissions/902980682/