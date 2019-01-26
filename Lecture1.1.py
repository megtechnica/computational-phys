from math import degrees, atan, sqrt, cos, sin, radians

class PythagoreanTheorem:
    def __init__(self, x_value, y_value, r_value):
        self.x_value = x_value
        self.y_value = y_value
        self.r_value = r_value
    def find_y(self, x_value, r_value):     # If we got an x and an r value, but no y
        PythagoreanTheorem.x_value = self.x_value
        PythagoreanTheorem.r_value = self.r_value
        PythagoreanTheorem.y_value = sqrt(r_value**2 - x_value**2)
        return y_value
    def find_x(self, y_value, r_value):
        PythagoreanTheorem.y_value = self.y_value
        PythagoreanTheorem.r_value = self.r_value
        PythagoreanTheorem.x_value = sqrt(r_value**2 - y_value**2)
        return x_value
    def find_r(self, x_value, y_value):
        PythagoreanTheorem.x_value = self.x_value
        PythagoreanTheorem.y_value = self.y_value
        PythagoreanTheorem.r_value = sqrt(x_value**2 + y_value**2)
        return r_value
    def __str___(self):
        print("x value is {},\ny value is {},\nand r value is {}.".format(x_value, y_value, r_value))    

class Convert_Cartesian_to_Polar:
    def __init__(self, x_value, y_value):
        self.x_value = x_value
        self.y_value = y_value
    def polar_conversion_calculator(self, x_value, y_value):
        theta = atan(self.y_value/self.x_value)
        theta = degrees(theta)      # atan() returns radians, converting to degrees
        return theta
    def __str__(self):
        print("The value of theta is {} in degrees.".format(theta))

class Convert_Polar_to_Cartesian:
    def __init__(self, r_value, theta):
        self.r_value = r_value
        self.theta = theta
    def cartesian_conversion_calcluator(self, r_value, theta):
        Convert_Polar_to_Cartesian.r_value = self.r_value
        Convert_Polar_to_Cartesian.theta = self.theta
        x = r_value * cos(theta)
        y = r_value * sin(theta)
        return x,y

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
                x_value = float(input("Input the length of leg x: "))
                y_value = float(input("Input the length of leg y: "))
                r_value = PythagoreanTheorem.find_r(x_value, y_value)
                theta = Convert_Cartesian_to_Polar.polar_conversion_calculator(x_value, y_value)
                polar_coordinates = (r_value, theta)
                complete = True
            elif formula.lower() == 'y':
                x_value = float(input("Input the length of leg x: "))
                r_value = float(input("Input the length of the hypotneuse: "))
                y_value = PythagoreanTheorem.find_y(x_value, r_value)
                theta = Convert_Cartesian_to_Polar.polar_conversion_calculator(x_value, y_value)
                complete = True
            elif formula.lower() == 'x':
                y_value = float(input("Input the length of leg y: "))
                r_value = float(input("Input the length of the hypotneuse: "))
                x_value = PythagoreanTheorem.find_x(y_value, r_value)
                theta = Convert_Cartesian_to_Polar.polar_conversion_calculator(x_value, y_value)
                polar_coordinates = (r_value, theta)
                complete = True
            else:
                print("That is not a valid option!  Please try again!")
        print("Your polar coordinates are {}".format(polar_coordinates))
    
    elif decision.upper() == 'C':
        print("To convert polar coordinates from cartesian coordinates, \nplease enter your value for the radius and theta")
        theta = radians(float(input("Please enter theta in degrees: ")))
        r_value = float(input("Please enter the radius of the circle: "))
        x, y = Convert_Polar_to_Cartesian.cartesian_conversion_calcluator(r_value, theta)
        print("Your cartesian coordinates are ({}, {})".format(x, y))

    else:
        print("Sorry! That was not a valid answer. Please try again!")
        print(menu)
        decision = input("What would you like to do?")

    print("What would you like to do now?")
    print(menu)
    decision = input("Please choose an option: ")

print("Goodbye!")
