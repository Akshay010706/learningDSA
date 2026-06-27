#include <iostream>
#include <vector>
using namespace std;

// LeetCode Problem 238: Product of Array Except Self
vector<int> productExceptSelf(vector<int>& nums) {
    int n = nums.size();
    vector<int> result(n, 1);
    
    // Calculate prefix products
    int prefix = 1;
    for (int i = 0; i < n; i++) {
        result[i] = prefix;
        prefix *= nums[i];
    }
    
    // Calculate suffix products and multiply
    int suffix = 1;
    for (int i = n - 1; i >= 0; i--) {
        result[i] *= suffix;
        suffix *= nums[i];
    }
    
    return result;
}

int main() {
    vector<int> nums = {1, 2, 3, 4};
    vector<int> result = productExceptSelf(nums);
    
    cout << "Result: ";
    for (int x : result) {
        cout << x << " ";
    }
    cout << endl;
    
    return 0;
}
