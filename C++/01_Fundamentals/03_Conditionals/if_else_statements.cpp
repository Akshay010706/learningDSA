//if else statement
#include <iostream>

using namespace std;

int main() {
    //write an program that takes an input age and tells if it is greater than 18 or not
    int age;
    cin>>age;
    if (age>18)
    {
        cout<<"You are an Adult";
    }
    else if (age<10)
    {
        cout<<"you are not a adult0";
    }
    
    else{
        cout<<"you will be 18 in few years";


    //ternary operator
    //Condition ? Expresion1: Expresion2;
    18>16?cout<<"Akshay":cout<<"Varun"; 
    
    int num =9;
    num%2?cout<<"ODD":cout<<"EVEN";
    // 1 correspont to teue and 0 to false

    // in boolean 
    bool hungery = true;
    hungery?cout<<"i am hungery ":cout<<"i am not hungery";
    //or
    cout<<hungery?"yes":"No";


    }
    
    
    return 0;
}
