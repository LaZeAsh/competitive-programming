#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max = prices[0], min = prices[0], len = prices.size(), max_diff = 0;

        for (int i = 1; i < len; i++) {
            if(prices[i] < min) {
                if(max - min > max_diff) max_diff = max - min;
                min = prices[i];
                max = prices[i];
            }

            if(prices[i] > max) max = prices[i];
        }

        if(max - min > max_diff) max_diff = max - min;

        return max_diff;
    }
};

