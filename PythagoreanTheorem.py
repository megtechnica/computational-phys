# instead of creating a class for calculating the missing side of the
# triangle, it may be best to make each of them a function.
from math import *

# find_r function
def find_r(x_value, y_value):
    r_value = sqrt(x_value**2 + y_value**2)
    return r_value

# find_y function
def find_y(x_value, r_value):
    y_value = sqrt(r_value**2 - x_value**2)
    return y_value

# find_x function
def find_x(y_value, r_value):
    x_value = sqrt(r_value**2 - y_value**2)
    return x_value

# outputs values to a file to be accessed by other python files
def output_to_file(x_value, y_value, r_value):
    triangle_legs = "{}, {}, {}\n".format(x_value, y_value, r_value)
    file = open("Legs of Triangles", "a")
    file.write(triangle_legs)
    file.close()

def menu():

    menu = "Find the missing side of your triangle using the Pythagorean Theorem!\n\n\t\tx^2 + y^2 = r^2\n\nEnter 'x' to find leg x.\nEnter 'y' to find leg y. \nEnter 'r' to find the hypotenuse.\nEnter 'q' to quit.\n\nWhat would you like to do?"
    complete = False
    decision = ''
    while decision != 'q':
        print(menu)
        decision = input("Enter your selection here: ")
        decision = decision.lower()
        if decision == 'r':
            x_value = float(input("Input the length of leg x: "))
            y_value = float(input("Input the length of leg y: "))
            r_value = find_r(x_value, y_value)
            output_to_file(x_value, y_value, r_value)
        elif decision == 'y':
            x_value = float(input("Input the length of leg x: "))
            r_value = float(input("Input the length of the hypotneuse: "))
            y_value = find_y(x_value, r_value)
            output_to_file(x_value, y_value, r_value)
        elif decision == 'x':
            y_value = float(input("Input the length of leg y: "))
            r_value = float(input("Input the length of the hypotneuse: "))
            x_value = find_x(y_value, r_value)
            output_to_file(x_value, y_value, r_value)
        elif decision == 'q':
            print("Goodbye!")
            break
        else:
            print("Whoopsies!  Looks like that was an invalid option!  Please enter another value!")
            decision = input("Enter your selection here: ")
    
    
try:
    menu()
except ValueError:
    print("\n\tYou've taken the square root of a negative number,\n\treturning an imaginary number. Please try again!\n")
    menu()

