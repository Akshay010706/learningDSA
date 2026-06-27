#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

// LeetCode Problem 217: Contains Duplicate
bool containsDuplicate(vector<int>& nums) {
    unordered_set<int> seen;
    for (int num : nums) {
        if (seen.find(num) != seen.end()) {
            return true;
        }
        seen.insert(num);
    }
    return false;
}

int main() {
    vector<int> nums = {1, 2, 3, 1};
    cout << (containsDuplicate(nums) ? "Contains duplicate" : "No duplicates") << endl;
    
    return 0;
}
