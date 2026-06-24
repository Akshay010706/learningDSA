#include <iostream>

using namespace std;
//type of function 
// void -> which does not return anything
void printname(){
    cout<<"Akshay";
}
//return
int su(int n1,int n2){
    int n3 = n1 + n2;
    return n3;
}
//or 
void sm(int n1, int n2){
    int n3 = n1 + n2;
    cout<<n3;
}
//parametrised
void pname(string name){
    cout<<"hey "<<name;

}
//non parameterised

//pass by value --not the value exactly goes throw the fuction but a copy of the no matter what you change in that value outside the function it wil remain the same
void dosomething(int num){
    num +=10;
    cout<<num;
    //here it will print num +10 but other the function the num will remain the same

}


//pass by refrence -- when you what to make changes in the original value
//use & to it then it takes the address of the value 

//for array it is allways pass by refrence
void dosomething(int &num){
    num +=10;
    cout<<num;
}    


int main() {
    printname();
    string n;
    cin>>n;
    pname(n);

    //inbuild function 
    //min(n1,n2)
    //max(n1,n2)
    
    return 0;
}