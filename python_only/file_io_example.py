#an example how to work with files
def read_file(filename):
    buffer = []
    if filename is None or filename == "":
        return buffer
    # we open a file
    file_obj = open(filename,"r")
    # we read the content into list
    buffer = file_obj.readlines()
    # we need to close the file
    file_obj.close()
    # we return read data
    return buffer

def read_file_improved(filename):
    buffer = []
    if filename is None or filename == "":
        return buffer
    with open(filename,'r') as file_obj:
        buffer = file_obj.readlines()
        return buffer


#a function to write to a file
def write_file(filename,data_to_write):
    if filename is None or filename == "":
        return
    # we open a file to write (and override the content)
    write_file_obj = open(filename,'w')
    # we write a list of (data/values)
    write_file_obj.writelines(data_to_write)
    #we close the file
    write_file_obj.close()


def write_file_improved(filename, data_to_write):
    if filename is None or filename == "":
        return
    with open(filename,'w') as file_obj:
        file_obj.writelines(data_to_write)



if __name__ == "__main__":
    content = read_file("random_text_file.txt")
    print("-----------")
    print(content)
    print("-----------")
    for line in content:
        print(line)
    print("-----------")
    write_file("random_output_text_file.txt", content)
    print("writing is done")
    print("-----------")
    content = read_file_improved("random_text_file.txt")
    print(content)
    print("-----------")
    write_file_improved("random_output_text_file_2.txt", content)
    print("writing is done")

    


