"""
A Ping represents a vehicle's position at a given timestamp.
"""

from position import Position


class Ping(object):

    def __init__(self, vehicle_id, position, timestamp):
        self.vehicle_id = vehicle_id # ID of the vehicle that created this ping
        self.position = position # (x, y) position of the ping
        self.timestamp = timestamp # Timestamp of the ping, in seconds since epoch

    def __str__(self):
        return str(self.position) + " @ " + str(self.timestamp)
