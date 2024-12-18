#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> return_list(2, -1);

        for(int i = 0; i < nums.size(); i++) {
            for(int z = i + 1; z < nums.size(); z++) {
                if(nums[i] + nums[z] == target) {
                    return_list[0] = i;
                    return_list[1] = z;

                    return return_list;
                }
            }
        }

        return return_list;
    }
};