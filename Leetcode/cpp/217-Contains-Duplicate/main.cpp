#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> frequency;
        for (int i = 0; i < nums.size(); i++) { // Since the size value is stored we don't need to make a variable
            if(frequency.find(nums[i]) == frequency.end()) frequency.insert(nums[i]);
            else return true;
        }
        return false;
    }
};