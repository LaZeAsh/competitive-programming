# Problem

Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Solution

Since the array given to us is not sorted the best time complexity we can get is O(n)

Traverse through the array and store the value of the highest and lowest and then find the difference of those

Since you cannot go in the future for the stock price whenever you find a new find the difference in the max and min prices

Find the difference between those prices and if this difference exceeds the max difference (initially set to 0) then define max difference as the difference between max - min

update max and min values to the new min value


Submission Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1479910738


