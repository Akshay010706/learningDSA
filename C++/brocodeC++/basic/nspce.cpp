#include <iostream>
//Namespce - provides a solution for preventing name conflicts in largeprojects , each entity needs a unique name .
//A namespace allows for identically named entities as long as the namespaces are diffrent

namespace first{
    int x =1;
}
namespace second{
    int x = 2;
}

int main() {
    int x =0;
    std::cout<<x;//0
    std::cout<<first::x;//1
    std::cout<<second::x;//2

    //using namespace second
    //std::cout<<x;//2


    //we can use
    //using namespace std 
    //to not use std:: evrytime we define string , cout , cin 
    //but this std ( standard ) namespace has many entities
    //hence we can use spercific name space 

    //like 
    // using std::cout;
    //using std::cin;
    //using std::string;
    
    return 0;
}