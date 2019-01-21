# import your nonsense from the appropriate place
from math import degrees, atan, sqrt, cos, sin, radians

# define the function to convert cartesian coordinates to polar coordinates
def Cartesian_2_Polar(side_x, side_y):
    theta = atan(side_x/side_y)
    return degrees(theta)

# define the function to convert polar coordinates to cartesians coordinates
def Polar_2_Cartesian(radius, theta):
    x = radius * cos(theta)
    y = radius * sin(theta)
    return x, y

# define the menu, because we use this more than once
menu = "Convert cartesian coordinates to polar coordinates\n" \
       "or polar coordinates to cartesian coordinates.\n\n" \
       "Enter 'C' to convert from polar to cartesian.\n" \
       "Enter 'P' to convert from cartesian to polar.\n" \
       "Enter 'Q' to quit\n"

# start doing the stuff
print(menu)
decision = input("What would you like to do? ")

# while loop begins
while decision.upper() != 'Q':
    if decision.upper() == 'P':
        # if they would like to convert from cartesian to polar
        print("To calculate polar coordinates from cartesian coordinates,\nwe must first find the lengths of all sides of our triangle.\n\nAssuming that the legs are x and y while the hypotenuse is r,")
        formula = input("which side would you like to calculate? (x, y or r) ")\
        # set a sentinal value for the loop
        complete = False
        while not complete:
            # to find the hypotenuse 
            if formula.lower() == 'r':
                side_x = float(input("Input the length of leg x: "))
                side_y = float(input("Input the length of leg y: "))
                side_r = sqrt(side_x**2 + side_y**2)
                theta = Cartesian_2_Polar(side_x, side_y)
                polar_coordinates = (side_r, theta)
                complete = True
            # to find side y
            elif formula.lower() == 'y':
                side_x = float(input("Input the length of leg x: "))
                side_r = float(input("Input the length of the hypotneuse: "))
                side_y = sqrt(side_r**2 - side_x**2)
                theta = Cartesian_2_Polar(side_x, side_y)
                polar_coordinates = (side_r, theta)
                complete = True
            # to find side x
            elif formula.lower() == 'x':
                side_y = float(input("Input the length of leg y: "))
                side_r = float(input("Input the length of the hypotneuse: "))
                side_x = sqrt(side_r**2 - side_y**2)
                theta = Cartesian_2_Polar(side_x, side_y)
                polar_coordinates = (side_r, theta)
                complete = True
            # starts again if you goof
            else:
                print("That is not a valid option!  Please try again!")
        # prints coordinates and displays the menu again
        print("Your polar coordinates are {}".format(polar_coordinates))
        print("What would you like to do now?")
        print(menu)
        decision = input("Please choose an option: ")
    
    # convert from polar to cartesian
    elif decision.upper() == 'C':
        print("To convert polar coordinates from cartesian coordinates, \nplease enter your value for the radius and theta")
        theta = radians(float(input("Please enter theta in degrees: ")))
        radius = float(input("Please enter the radius of the circle: "))
        x, y = Polar_2_Cartesian(radius, theta)
        # prints the results and asks you if you want to begin again
        print("Your cartesian coordinates are ({}, {})".format(x, y))
        print("What would you like to do now?")
        print(menu)
        decision = input("Please choose an option: ")

    else:
        # catches unintended values
        print("Sorry! That was not a valid answer. Please try again!")
        print(menu)
        decision = input("What would you like to do?")
# when decision == 'Q'
print("Goodbye!")
