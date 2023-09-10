import math
# remove the unnecessary int() conversions when calculating total_area and number_cans because math.ceil() already returns an integer.


height = int(input("Enter the Height of the room\n"))
width = int(input("Enter the width of your room\n"))
coverage = 5

# defining the function
def paint_cans(height, width, coverage):
    total_area = (height*width)
    number_cans = (total_area/coverage)
    round_cans = math.ceil(number_cans)
    print(f"You will require {round_cans} number of cans in total")


# Calling the function
paint_cans(height, width, coverage)
