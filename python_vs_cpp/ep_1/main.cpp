#include <iostream>
#include <string>

// return_type functionName( arg1Type arg1, arg2Type arg2, ... , argNtype argN)
void variable_examples() 
{
    char char_var = 'b';
    short short_var = 9000;
    int int_var = 20000;
    //more integer types

    float float_var = 3.14f;
    double double_var = 3.14;
    long double ldouble_var = 3.14;

    const char *char_string = "it is a char string";
    std::string string_var = "it is a string variable";

    bool bool_var   = true;
    bool bool_var_2 = false;

    std::cout << int_var << std::endl;
    std::cout << double_var << std::endl;
    std::cout << char_string << std::endl;
    std::cout << bool_var << std::endl;
    std::cout << bool_var_2 << std::endl;
}

void if_else_example()
{
int small_value = 20000;
int big_value = 30000;

    if (big_value > small_value) {
        std::cout << big_value << " is greater than " 
                  << small_value << std::endl;
        small_value += big_value;
    }

    if (big_value > small_value) {
        std::cout << "What??" << std::endl;
    } else {
        std::cout << "Exactly!" << std::endl;
    }

}

void loop_example() 
{
    //for(initial value;condition;change value)
    for (int i = 0; i < 5; ++i) { // [0:5)
        std::cout << "i = " << i << std::endl;
    }

    int iNumber = 3;
    while( iNumber > 0 ) {
        iNumber -= 1;
        std::cout << "iNumber = " << iNumber << std::endl;
    }
}

// return_type functionName( arg1Type arg1, arg2Type arg2, ... , argNtype argN)
int main(int argc, char* argv[]) {

    std::cout << "hard-coded msg" << std::endl;

    std::cout << "---- variable_examples ----" << std::endl;
    variable_examples();
    std::cout << "---- if_else_example ----" << std::endl;
    if_else_example();
    std::cout << "---- loop_example ----" << std::endl;
    loop_example();

    std::cout << "---- ----" << std::endl;

    std::string user_input;
    std::cout << "Hi! Please, enter something:";
    std::cin  >> user_input;
    std::cout << "You have entered |"<< user_input << "|" << std::endl;

    return 0;
}