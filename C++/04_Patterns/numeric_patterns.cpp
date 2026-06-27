#include <iostream>
using namespace std;

int main() {
    int n = 5;
    
    // Numeric pattern
    cout << "Numeric Pattern:" << endl;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            cout << j << " ";
        }
        cout << endl;
    }
    
    return 0;
}
