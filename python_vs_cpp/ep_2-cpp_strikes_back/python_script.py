


# return_type functionName( arg1Type arg1, arg2Type arg2, ... , argNtype argN)
def variable_examples():
    char_var = 'b'
    short_var = 9000
    int_var = 20000
    
    float_var = 3.14
    double_var = 3.14
    ldouble_var = 3.14

    char_string = "it is a char string"
    string_var = "it is a string variable"

    bool_var   = True
    bool_var_2 = False

    print(int_var)
    print(double_var)
    print(char_string)
    print(bool_var)
    print(bool_var_2)


def if_else_example():
    small_value = 20000
    big_value = 30000
    if big_value > small_value:
        print(f'{big_value} is greater than {small_value}')
        small_value += big_value
    
    if big_value > small_value:
        print("What??")
    else:
        print("Exactly!")


def loop_example():
    for i in range(0,5):
        print(f'i = {i}')

    iNumber = 3
    while iNumber > 0:
        iNumber -= 1
        print(f'iNumber = {iNumber}')

# def function_name(arg1,arg2,..,argN)
def main():
    print("hard-coded msg")
    print("---- variable_examples ----")
    variable_examples()
    print("---- if_else_example ----")
    if_else_example()
    print("---- loop_example ----")
    loop_example()

    print("---- ----")
    
    user_input = input("Hi! Please, enter something:")
    print(f'You have entered |{user_input}|')

# Tip: remember or save it somewhere
if __name__ == "__main__":
    main()