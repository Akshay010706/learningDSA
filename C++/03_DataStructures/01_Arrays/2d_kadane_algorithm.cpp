#include <iostream>
#include <vector>
#include <climits>
using namespace std;

// Kadane's Algorithm - Maximum subarray sum (2D)
int maxSumSubmatrix(vector<vector<int>>& matrix) {
    int rows = matrix.size();
    int cols = matrix[0].size();
    int maxSum = INT_MIN;
    
    for (int left = 0; left < cols; left++) {
        vector<int> temp(rows, 0);
        
        for (int right = left; right < cols; right++) {
            for (int i = 0; i < rows; i++) {
                temp[i] += matrix[i][right];
            }
            
            // Apply Kadane's algorithm on temp
            int sum = 0;
            int maxSum_1d = INT_MIN;
            for (int num : temp) {
                sum = max(num, sum + num);
                maxSum_1d = max(maxSum_1d, sum);
            }
            
            maxSum = max(maxSum, maxSum_1d);
        }
    }
    
    return maxSum;
}

int main() {
    vector<vector<int>> matrix = {{1, 2, -1}, {-3, -4, 5}, {5, -8, 9}};
    cout << "Maximum submatrix sum: " << maxSumSubmatrix(matrix) << endl;
    
    return 0;
}
