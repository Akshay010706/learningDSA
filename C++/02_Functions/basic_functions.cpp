#include <iostream>

using namespace std;

// Function declaration
void greet(string name) {
    cout << "Hello " << name << endl;
}

int add(int a, int b) {
    return a + b;
}

int main() {
    // Function calls
    greet("Akshay");
    cout << "Sum: " << add(5, 3) << endl;
    
    return 0;
}
