from math import degrees, atan, sqrt, cos, sin, radians

def Cartesian_2_Polar(side_x, side_y):
    theta = atan(side_x/side_y)
    return degrees(theta)

def Polar_2_Cartesian(radius, theta):
    x = radius * cos(theta)
    y = radius * sin(theta)
    return x, y

menu = "Convert cartesian coordinates to polar coordinates\n" \
       "or polar coordinates to cartesian coordinates.\n\n" \
       "Enter 'C' to convert from polar to cartesian.\n" \
       "Enter 'P' to convert from cartesian to polar.\n" \
       "Enter 'Q' to quit\n"
print(menu)
decision = input("What would you like to do? ")


while decision.upper() != 'Q':
    if decision.upper() == 'P':
        print("To calculate polar coordinates from cartesian coordinates,\nwe must first find the lengths of all sides of our triangle.\n\nAssuming that the legs are x and y while the hypotenuse is r,")
        formula = input("which side would you like to calculate? (x, y or r) ")
        complete = False
        while not complete:
            if formula.lower() == 'r':
                side_x = float(input("Input the length of leg x: "))
                side_y = float(input("Input the length of leg y: "))
                side_r = sqrt(side_x**2 + side_y**2)
                theta = Cartesian_2_Polar(side_x, side_y)
                polar_coordinates = (side_r, theta)
                complete = True
            elif formula.lower() == 'y':
                side_x = float(input("Input the length of leg x: "))
                side_r = float(input("Input the length of the hypotneuse: "))
                side_y = sqrt(side_r**2 - side_x**2)
                theta = Cartesian_2_Polar(side_x, side_y)
                polar_coordinates = (side_r, theta)
                complete = True
            elif formula.lower() == 'x':
                side_y = float(input("Input the length of leg y: "))
                side_r = float(input("Input the length of the hypotneuse: "))
                side_x = sqrt(side_r**2 - side_y**2)
                theta = Cartesian_2_Polar(side_x, side_y)
                polar_coordinates = (side_r, theta)
                complete = True
            else:
                print("That is not a valid option!  Please try again!")
        print("Your polar coordinates are {}".format(polar_coordinates))
        print("What would you like to do now?")
        print(menu)
        decision = input("Please choose an option: ")
    
    elif decision.upper() == 'C':
        print("To convert polar coordinates from cartesian coordinates, \nplease enter your value for the radius and theta")
        theta = radians(float(input("Please enter theta in degrees: ")))
        radius = float(input("Please enter the radius of the circle: "))
        x, y = Polar_2_Cartesian(radius, theta)
        print("Your cartesian coordinates are ({}, {})".format(x, y))

    else:
        print("Sorry! That was not a valid answer. Please try again!")
        print(menu)
        decision = input("What would you like to do?")

print("Goodbye!")
