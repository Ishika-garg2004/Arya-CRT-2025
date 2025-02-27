'''Q2.Explain how Python handles type conversion between different data types, such as between integers and floats or between strings and lists.
Ans.Python handles type conversion in two main ways: implicit type conversion and explicit type conversion.

1.Implicit Type Conversion:
Python automatically converts one data type to another when it makes sense to do so, without the need for explicit instructions from the programmer.'''
'''Example: Integer to Float
When performing arithmetic operations between integers and floats, Python automatically converts the integer to a float.'''
x = 10    
y = 3.5   
result = x + y  
print(result)   
print(type(result))  

Output: 13.5
Output: <class 'float'>

'''2. Explicit Type Conversion:
When Python does not perform automatic conversion, we can manually convert data types using built-in functions.'''

'''Common Type Conversion Functions:
int(): Converts a value to an integer.
float(): Converts a value to a floating-point number.
str(): Converts a value to a string.
list(): Converts a value to a list.
tuple(): Converts a value to a tuple.
set(): Converts a value to a set.
dict(): Converts a value to a dictionary (if given a compatible input).
Example: Converting Float to Integer'''
a = 5.9
b = int(a)  
print(b)  


#Example: Converting String to Integer
num_str = "123"
num_int = int(num_str)  
print(num_int + 10)  

#(If the string contains non-numeric characters, int() will raise a ValueError.)

#Example: Converting String to List
s = "hello"
lst = list(s)  
print(lst)  


#Example: Converting List to String
lst = ['h', 'e', 'l', 'l', 'o']
s = "".join(lst)  
print(s)  


'''3. Type Conversion Limitations and Errors
Trying to convert an incompatible type will result in an error.
Example: Converting a string with letters to an integer will fail.'''
s = "abc"
print(int(s))  

#Floating-point numbers may lose precision when converted to integers.

#Q3.Take a number and use the += operator to increase its value by 10. 
num = 5  
num += 10 
print(num)  
Output: 15

#Q4.Write a Python program to check if a given year is a leap year or not. 
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#Q5.Write a program that asks the user to enter their marks and displays their
#  grade: • 90-100: A 80-89: B 70-79: C 60-69: D Below 60: F 
marks = int(input("Enter your marks: "))
if 90 <= marks <= 100:
    grade = "A"
elif 80 <= marks < 90:
    grade = "B"
elif 70 <= marks < 80:
    grade = "C"
elif 60 <= marks < 70:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")
