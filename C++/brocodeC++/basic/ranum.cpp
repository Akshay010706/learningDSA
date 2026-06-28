#include <iostream>
#include <ctime>

using namespace std;

int main() {
    // pseudo-random = Not truly random burt close
    srand(time(NULL));//NULL OR 0 FOR CURRENT TIME
    int num = (rand()%6)+1;
    //gives number between 0 to 6

    cout<<num;
    
    return 0;
}