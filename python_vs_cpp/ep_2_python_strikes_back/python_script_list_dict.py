def list_example():
    list_of_ints = [ 1, 15,-10, 20]
    for elem in list_of_ints:
        print(elem)
    print(list_of_ints)
    list_of_strings = [ "abc", "def"]
    list_of_strings.append("xyz")
    print(list_of_strings)
    list_of_strings.remove("def")
    print(list_of_strings)


def dictionary_example():
    # variable = { key : value , key2: value2, etc. }
    different_info = { 10 : "string_value" 
    , False : "another_string"
    , "key_string" : 3.14 }

    # print(different_info)

    code_per_line = { 1: "include" ,
                        5: "success" , 
                        10 : "return" }
    code_per_line[15] = "Another line"
    print(code_per_line)
    
    return_val = code_per_line.get( 10 )
    print (return_val)

    code_per_line.pop(10)
    code_per_line.pop(1)
    print(code_per_line)


# def function_name(arg1,arg2,..,argN)
def main():
    # list_example()
    dictionary_example()

# Tip: remember or save it somewhere
if __name__ == "__main__":
    main()