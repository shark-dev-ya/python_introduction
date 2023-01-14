# to define a variable, you are using the syntax:
# variable_name = <value>

int_number = 10
int_number_2 = int_number + 100

float_number = -57.34

string_variable = "it is my string variable"

string_other_variable = 'it is my other string variable'

my_long_variable = """ it was quite long time ago
when i have decided to learn software development
   and watch Netflix sometimes
and grow up
"""

my_boolean_variable = True
other_boolean_variable = False

print(int_number)
print(int_number_2)

print(float_number)

print(string_variable)
print(string_other_variable)

print(my_long_variable)

print(my_boolean_variable)
print(other_boolean_variable)

# what about redefine a variable? or reassign it?

my_custom_input = 999
print(my_custom_input)
# assume, that something changed in the code.
my_custom_input = "Now it is a string!"
print(my_custom_input)


### 
int_number = int_number_2 - 5
int_number = int_number_2 * 5
int_number = int_number_2 / 5
int_number = int_number_2 + 5

int_number = 2
int_number_2 = 5
print( int_number ** int_number_2 )  # will print 32 ( 2^5 )

### If and else

# if <condition> :
if int_number < int_number_2 :
    print( "int_number is less than int_number_2" )
    third_int_number = 3
else:
    print("or not!")

if int_number < int_number_2:
    print("gotcha!")
    if float_number > 0:
        print("yep!")
    print("line after if statement")


# loops
# in C++ we have a format: for( variable definition (start value) ; condition to execute a loop; change value )

for iterate_value in range(1, 5): # [1:5)
    print(iterate_value)

print(int_number)  # it is equal to 2
while int_number > 0:
    print(int_number)
    int_number -= 1  # it is equal to  -> int_number = int_number - 1

# in C++ : return_type functionName( typeOfArg1 arg1, typeOfArg2 arg2,...)
def calculate_two_numbers(value_1, value_2 = 3):
    result = value_1 * value_2
    return result

print("_________________________")
print( calculate_two_numbers(10) )
print( calculate_two_numbers(10,5) )
print( calculate_two_numbers("10") )
print("_________________________")


# we can define variables
# we can use if / else
# we can use loops (for, while)
# we can define a function and call it.

input_from_user = input("Hi! Please, write anything here:")
print( input_from_user)

print( "some text with {} and {}. Yes!".format(int_number, float_number) )

print( f'other string with {int_number} and other {int_number_2}')