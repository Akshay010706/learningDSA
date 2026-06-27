#include <iostream>

using namespace std;

int main() {
    // Switch statement implementation
    int choice;
    cin >> choice;
    
    switch(choice) {
        case 1:
            cout << "Option 1 selected";
            break;
        case 2:
            cout << "Option 2 selected";
            break;
        default:
            cout << "Invalid option";
    }
    
    return 0;
}
