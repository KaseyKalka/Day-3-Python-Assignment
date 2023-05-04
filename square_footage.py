import math

def get_area():
    length = float(input("Please give me the length of your room in feet."))
    width = float(input("Please give me the width of your room in feet"))
    area = length*width

    return f"The area of your house is: {area} square feet."

def get_circumference():
    radius = float(input("Please give me the radius of your circle in inches."))
    circumference = format((2*math.pi*radius), ".2f")

    return f"The circumference of your circle is: {circumference} inches."