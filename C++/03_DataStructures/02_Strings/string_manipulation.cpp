#include <iostream>
#include <string>
using namespace std;

int main() {
    // String manipulation
    string str = "Hello";
    
    // Substring
    cout << "Substring (0, 3): " << str.substr(0, 3) << endl;
    
    // Find
    int pos = str.find('l');
    cout << "Position of 'l': " << pos << endl;
    
    // Replace
    str.replace(0, 2, "JJ");
    cout << "After replacement: " << str << endl;
    
    return 0;
}
