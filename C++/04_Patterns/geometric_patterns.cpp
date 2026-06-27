#include <iostream>
using namespace std;

int main() {
    int n = 5;
    
    // Triangle pattern
    cout << "Triangle Pattern:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            cout << "* ";
        }
        cout << endl;
    }
    
    return 0;
}
