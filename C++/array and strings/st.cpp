#include <iostream>

using namespace std;

int main() {
    string s = "Akshay";
    int len = s.size();
    s[len-1]='z';

    //string methods 
    s.length();
    //empty() method returns a boolean value if a string is empty or not 
    s.empty();
    //clear a string 
    s.clear();

    //append a string at the end of a string 
    s.append("@gmail.com");//--Akshay@gmail.com

    //character at a given position in a string 
    s.at(0);

    //insert a charcter at given position
    s.insert(0,"@");//- @Akshay

    //find in the string (return index )
    cout<<s.find(' ');

    //erase a portion of a string
    s.erase(0,3);//erase the first 3 character of my string 




    return 0;
}