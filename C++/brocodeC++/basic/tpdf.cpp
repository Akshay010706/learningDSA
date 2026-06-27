#include <iostream>

//typedf - reserved keyword used to create an additional name 
//  (alias ) for another data type
//   new identifier for an existing type
// helps with readability and reduces typos

#include <vector>

//gave a new identifier to an existing data type
//name convesion allways end with _t
// typedef std::vector<std::pair<std::string, int >>pairlist_t;

typedef std::string text_t;
typedef int number_t;


// using (using keyword)
using text_t = std::string;
using number_t = int;

int main() {
    text_t firstname = "Akshay";
    number_t age = 20;

    std::cout<<firstname<<'\n';
    std::cout<<age<<'\n';
    
    return 0;
}

// typedf is been replaced by 'using' (works better with templates)