#include <iostream>

using namespace std;

//global variable
int x = 1;

// Function overloading - same function name, different parameters
int add(int a, int b) {
    return a + b;
}

//a and b becomes pointer it stores the address of where the variable is stores
double add(double a, double b) {
    return a + b;
}

int add(int a, int b, int c) {
    return a + b + c;
}

int main() {
    cout << add(5, 3) << endl;           // calls int version
    cout << add(5.5, 3.2) << endl;       // calls double version
    cout << add(5, 3, 2) << endl;        // calls int, int, int version
    int x = 6;
    cout<<x; // 9
    cout<<::x;//1
    
    return 0;
}
