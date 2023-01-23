#include <iostream>
#include <string>
#include <list>
#include <map>

void list_example() {
    std::list<int> list_of_ints = {  1, 15,-10, 20 };
    //for each loop:
    for(int elem : list_of_ints) {
        std::cout << elem << std::endl;
    }
    // the C style with iterators.  ( C language and old C++ standard (up to C++03))
    for( std::list<int>::iterator it = list_of_ints.begin();
         it != list_of_ints.end();
         ++it ) 
    {
        int elem = *it;
        std::cout << elem << std::endl;
    }


    std::list<std::string> list_of_strings = { "abc" , "def" };
    list_of_strings.push_back( std::string( "xyz"));
    
    for(std::string elem : list_of_strings) {
        std::cout << " "<< elem ;
    }
    std::cout << std::endl;

    //list_of_strings.erase();
    for (auto it = list_of_strings.begin() ;
             it != list_of_strings.end(); 
             ++it ) 
    {
        if ( *it == "def" ) {
            list_of_strings.erase(it);
            break;
        }
    }
    list_of_strings.push_back( std::string( "def"));
    list_of_strings.remove("def");

    for(std::string elem : list_of_strings) {
        std::cout << " "<< elem ;
    }
    std::cout << std::endl;

}

void dictionary_map_example() {
    // std::map< type for key , type for value>
    std::map<int, std::string> code_per_line = {
        { 1 , "include"},
        { 5 , "success"},
        { 10 , "return"},
    };
    code_per_line[15] = "Another line";

    for (auto entry : code_per_line) {
        // entry stores a Pair of key and value
        // key is "first" and "value" is second.
        std::cout << "key : " << entry.first 
                << " and value = " << entry.second << std::endl;
    }

    auto returnIt = code_per_line.find( 10 );
    if ( returnIt != code_per_line.end() ) {
        //we have found an element.
        std::cout << "returnIt contains : " 
        << returnIt->first << " and " << returnIt->second << std::endl;
    }

    code_per_line.erase( /*iterator*/ returnIt);

    code_per_line.erase(1);
    
    for (auto entry : code_per_line) {
        // entry stores a Pair of key and value
        // key is "first" and "value" is second.
        std::cout << "key : " << entry.first 
                << " and value = " << entry.second << std::endl;
    }
    
}


int main(int argc, char* argv[]) {
    //list_example();
    dictionary_map_example();
    return 0;
}