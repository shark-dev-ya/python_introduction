BUILD_DIR := build

py_script: python_script.py
	@python3 python_script.py

cpp_app: build_cpp_app
	@./$(BUILD_DIR)/cpp_app

# c++ app*
build_cpp_app: main.cpp
	@mkdir -p $(BUILD_DIR)
	@g++ -std=c++17 -o $(BUILD_DIR)/cpp_app main.cpp

clean:
	@rm -rf $(BUILD_DIR)