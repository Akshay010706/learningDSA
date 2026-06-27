#include <iostream>
#include <string>
using namespace std;

int main() {
    // String pattern matching
    string text = "ABABDABACD";
    string pattern = "ABAD";
    
    // Simple pattern search
    size_t pos = text.find(pattern);
    if (pos != string::npos) {
        cout << "Pattern found at position: " << pos << endl;
    } else {
        cout << "Pattern not found" << endl;
    }
    
    return 0;
}
