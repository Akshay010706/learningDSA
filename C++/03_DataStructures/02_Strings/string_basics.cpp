#include <iostream>
#include <string>
using namespace std;

int main() {
    // String basics
    string str = "Hello World";
    
    cout << "String: " << str << endl;
    cout << "Length: " << str.length() << endl;
    cout << "Character at index 0: " << str[0] << endl;
    
    // String concatenation
    string str2 = " from C++";
    string result = str + str2;
    cout << "Concatenated: " << result << endl;
    
    return 0;
}
