def read_file(filename):
    buffer = []
    if filename is None or filename == "":
        return buffer
    with open(filename,'r') as read_file_obj:
        buffer = read_file_obj.readlines()
        return buffer

def write_file(filename,data_to_write):
    if filename is None or filename == "":
        return
    with open(filename, mode="w") as write_file_obj:
        write_file_obj.writelines(data_to_write)

# def function_name(arg1,arg2,..,argN)
def main():
    content = read_file("Makefile")
    for line in content:
        print(line, end='')
    print()
    write_file("Makefile.python_edition", content)


# Tip: remember or save it somewhere
if __name__ == "__main__":
    main()