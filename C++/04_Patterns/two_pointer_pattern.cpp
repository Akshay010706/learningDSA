#include <iostream>
#include <vector>
using namespace std;

// Two pointer pattern example - Find pair with sum
int main() {
    vector<int> arr = {1, 3, 5, 7, 9};
    int target = 10;
    
    int left = 0, right = arr.size() - 1;
    
    cout << "Finding pairs with sum = " << target << endl;
    while (left < right) {
        int sum = arr[left] + arr[right];
        if (sum == target) {
            cout << "Pair found: (" << arr[left] << ", " << arr[right] << ")" << endl;
            left++;
            right--;
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }
    
    return 0;
}
