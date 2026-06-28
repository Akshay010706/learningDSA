#include <iostream>
#include <vector>
using namespace std;

int main() {
    // Basic array operations
    vector<int> arr = {1, 2, 3, 4, 5};

    //s stores number of element in the array
    int s = sizeof(arr)/sizeof(arr[0]);
    //or
    //int s = sizeof(arr)/sizeof(arr[int]);
    
    // Print array using foreach loop
    cout << "Array elements: ";
    for (int x : arr) {
        cout << x << " ";
    }
    cout << endl;
    
    // Modify element
    arr[2] = 10;
    cout << "After modification: " << arr[2] << endl;
    
    // Size of array
    cout << "Size: " << arr.size() << endl;
    
    return 0;
}
