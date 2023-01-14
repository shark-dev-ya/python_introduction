
py_script: python_script.py
	@python3 python_script.py

cpp_app: build_cpp_app
	@./cpp_app

# c++ app*
build_cpp_app: main.cpp
	@g++ -std=c++17 -o cpp_app main.cpp

clean:
	rm -rf cpp_app