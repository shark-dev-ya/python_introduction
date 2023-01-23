# import <module or package> name
import json  #  in C we are using #include <header>
# from <package name> import <what exactly we want to import>


json_content = { "key1" : "string" , "key_for_int" : 192, "key_for_float" : 3.14 }
json_content["array"] = ["string1", "string2", "string3" ]
json_content["complex-array"] = [
    { "sub_key1" : "value11" },
    { "sub_key2" : "value22" }
]

simplified_json_string = json.dumps(json_content) # simplified
json_string_with_newline = json.dumps(json_content,indent=0) # add only new line
json_pretty_format = json.dumps(json_content, indent=4)

print("------simplified_json_string : ------")
print(simplified_json_string)
print("------json_string_with_newline:------")
print(json_string_with_newline)
print("------json_pretty_format:------")
print(json_pretty_format)

json_dict = {}
with open("input_file.json") as json_fd:
    #1st option is to read the string and then convert:
    file_content_raw = json_fd.read()
    json_dict = json.loads(file_content_raw)

print("------json_dict:------")
print(json_dict)
print("------json_dict:------")

if "key1" in json_dict:
    print("Yeah!")

# with open("input_file.json") as json_fd:
#     # 2nd option : is to delegate json to read a file and construct dict
#     json_another_dict = json.load(json_fd)
#     print("------json_another_dict:------")
#     print(json_another_dict)
#     print("------json_another_dict:------")

