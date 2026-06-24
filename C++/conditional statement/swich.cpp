#include <iostream>

using namespace std;

int main() {
    int day;
    cin>>day;
    switch (day)
    {
    case 1:
        cout<<"Monday";
        break;
//add other days in diffrent case
    default:
    cout<<"invalid";
        break;
    }
    
    return 0;
}