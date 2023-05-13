"""
A small library whose sole purpose is to determine the location of a Ping,
given that Ping's distance from the three different Access Points set up
around the warehouse.
"""

import math
from position import Position

AP1_LOCATION = Position(5, 8)
AP2_LOCATION = Position(4, 12)
AP3_LOCATION = Position(10, 6)


def triangulate(distance_from_AP1, distance_from_AP2, distance_from_AP3):
    """
    Given the distance from each of the three Access Points, respectively,
    finds the one location that satisfies those distances.
    
    This is technically trilateration, not triangulation, but people are
    more familiar with the term triangulation, and I say: why not give the
    people what they want?
    
    I don't recommend spending any time trying to understand the complex
    code in this calculation, which is derived from the math in this answer:
    https://stackoverflow.com/a/9754358
    """
    x_matrix = get_coordination_matrix(AP1_LOCATION, AP2_LOCATION)
    i = get_dot_product(x_matrix, AP3_LOCATION) - get_dot_product(x_matrix, AP1_LOCATION)

    y_matrix = get_coordination_matrix(AP1_LOCATION, AP3_LOCATION, Position(i*x_matrix.x, i*x_matrix.y))
    j = get_dot_product(y_matrix, AP3_LOCATION) - get_dot_product(y_matrix, AP1_LOCATION)

    d = get_complex_distance(AP2_LOCATION, AP1_LOCATION)
    
    offset_x = (distance_from_AP1**2 - distance_from_AP2**2 + d**2) / (2*d)
    offset_y = ((distance_from_AP1**2 - distance_from_AP3**2 + i**2 + j**2) / (2*j)) - ((i*offset_x)/j)
    
    true_x = AP1_LOCATION.x + (offset_x * x_matrix.x) + (offset_y * y_matrix.x)
    true_y = AP1_LOCATION.y + (offset_x * x_matrix.y) + (offset_y * y_matrix.y)
    
    return Position(round(true_x), round(true_y))


def get_complex_distance(position_1, position_2, position_3=Position(0,0)):
    x_diff = abs(position_1.x - position_2.x - position_3.x)
    y_diff = abs(position_1.y - position_2.y - position_3.y) 
    return math.sqrt(pow(x_diff, 2) + pow(y_diff, 2))

def get_coordination_matrix(position_1, position_2, position_3=Position(0,0)):
    xCoord = (position_2.x - position_1.x - position_3.x) / get_complex_distance(position_2, position_1, position_3)
    yCoord = (position_2.y - position_1.y - position_3.y) / get_complex_distance(position_2, position_1, position_3)
    return Position(xCoord, yCoord)

def get_dot_product(position_1, position_2):
    return (position_1.x * position_2.x) + (position_1.y * position_2.y)