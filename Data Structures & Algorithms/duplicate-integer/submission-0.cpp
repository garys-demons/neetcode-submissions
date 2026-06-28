class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> indices;

        for(int i = 0; i < nums.size(); i++){
            indices[nums[i]] = i;
        }

        for(int i = 0; i < nums.size(); i++){
            if(indices.count(nums[i]) && indices[nums[i]] != i){
                return true;
            }
        }

        return false;
    }
};