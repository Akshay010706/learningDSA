#include <iostream>

using namespace std;

//void hlo();

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

// you can also declare a functiuon in starting and define in after main function int main()

//void hlo(){
//cout<<"hii";
//}