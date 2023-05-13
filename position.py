"""
A Position represents an x, y coordinate in a given warehouse.
"""

import math


class Position(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):
        if not isinstance(other, Position):
            return False

        return (self.x == other.x and self.y == other.y)

    @staticmethod
    def get_distance(position_1, position_2):
        """
        Determines the distance between two Positions
        Distance is calculated as the Euclidean distance in two dimensions
        https://en.wikipedia.org/wiki/Euclidean_distance
        """
        x_diff = abs(position_1.x - position_2.x)
        y_diff = abs(position_1.y - position_2.y)
        return math.sqrt(pow(x_diff, 2) + pow(y_diff, 2))
