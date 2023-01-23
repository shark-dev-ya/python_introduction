def list_example():
    # variable_name = [ enumerate elements ]
    list_v1 = [ 1 ,2 , 3.14 , "four" , "five" ]
    print(list_v1)
    list_v1.append(True)
    print(list_v1)
    list_v1.pop(2) # The index goes from 0!
    print(list_v1)
    list_v1.remove("five")
    print(list_v1)
    list_v2 = []
    print(list_v2)
    list_v2.append("one")
    list_v2.append("two")
    print(list_v2)
    list_total = list_v1 + list_v2
    print(list_total)
    print(list_v1)
    print(list_v2)

def dict_example():
    # variable_name = { key : value , key : value }
    dict_v1 = { "key1":"value1" , "key2": 15, 15 : "Value_15"}
    print(dict_v1)
    for key_elem in dict_v1:
        print(f'key_elem = {key_elem} contains { dict_v1[key_elem] }')
    dict_v1["my_new_key"] = "my_new_value"
    print(dict_v1)

    if "key2" in dict_v1:
        print("This key is already existing!")
    
    if "my_old_key" not in dict_v1:
        print("Oh! my_old_key was removed from dict_v1")

    dict_v1.pop(15)
    print(dict_v1)

    for key_elem, value_elem in dict_v1.items():
        print(f' key_elem {key_elem} contains {value_elem}')
    

if __name__ == "__main__":
    list_example()
    dict_example()
