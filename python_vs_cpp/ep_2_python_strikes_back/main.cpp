#include <iostream>
#include <string>
#include <list>
#include <stdio.h>
#include <fstream>
#include <cstring>

typedef std::list<std::string> StringList_t;

StringList_t read_file(std::string filename) {
    StringList_t buffer;
    if (filename.empty()) {
        return buffer;
    }
    //we open a file
    FILE* read_file_obj = fopen(filename.c_str(), "r");
    if (nullptr == read_file_obj) {
        std::cout << "Sorry, but " << filename 
        << " can't be opened" << std::endl;
        return buffer;
    }

    const int buffer_size = 256;
    char char_buffer[buffer_size];
    while( fgets(char_buffer, buffer_size, read_file_obj) != NULL) {
        std::string str_buffer(char_buffer);
        buffer.push_back(str_buffer);
    }

    //we close the file
    if (nullptr != read_file_obj) {
        fclose(read_file_obj);
    }

    return buffer;
}

void write_file(std::string filename, 
                StringList_t data_to_write) 
{
    if (filename.empty()) {
        return;
    }
    FILE* write_file_obj = fopen(filename.c_str(), "w");
    if (nullptr == write_file_obj) {
        std::cout << "Sorry, but filename " 
                << filename << " can't be opened"
                << std::endl;
    }

    for (std::string line : data_to_write) {
        int returned_code = fputs( line.c_str() , write_file_obj );
        if (returned_code < 0 ) {
            std::cout << "Oops! " << filename 
                        << " can't take this line : " 
                        << line 
                        << std::endl;
        }
    }

    if (nullptr != write_file_obj) {
        fclose(write_file_obj);
    }
}


StringList_t read_file_v2(std::string filename) {
    StringList_t buffer;
    if (filename.empty()) {
        return buffer;
    }
    std::ifstream read_file_obj(filename);
    
    const int buffer_size = 256;
    char char_buffer[buffer_size];

    if (read_file_obj.is_open()) {
        while (read_file_obj.good()) {
            memset(char_buffer, 0 , buffer_size);
            read_file_obj.getline(char_buffer, buffer_size);
            buffer.push_back( std::string(char_buffer) );
        }
    }
    return buffer;
}

void write_file_v2(std::string filename, 
                StringList_t data_to_write)
{
    if (filename.empty()) {
        return;
    } 
    std::ofstream write_file_obj(filename, std::ofstream::out);
    if ( write_file_obj.is_open()) {
        for( std::string line : data_to_write) {
            write_file_obj << line ;
        }
    }
    write_file_obj.close();
}

int main(int argc, char* argv[]) {
    StringList_t content;
    // content = read_file("Makefile");
    // for (std::string line : content ) {
    //     std::cout << line;
    // }

    // write_file("Makefile.cpp_edition", content);

    content = read_file_v2("Makefile");
    for (std::string line : content ) {
        std::cout << line << std::endl;
    }
    write_file_v2("Makefile.cpp_edition_v2", content);

    return 0;
}