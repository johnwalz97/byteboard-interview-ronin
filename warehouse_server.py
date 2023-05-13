"""
This server stores the Pings from all of the vehicles in the warehouse. 
It loads in Pings from a csv file, which is compiled from the periodic
pings received by the warehouse's three Access Points.
"""

import csv

from triangulator import triangulate


class Ping:
    def __init__(self, vehicle_id, timestamp, position):
        self.vehicle_id = vehicle_id
        self.timestamp = timestamp
        self.position = position


class WarehouseServer(object):
    def __init__(self):
        self.all_pings = []

    def load_pings(self, file_name):
        """
        Loads in all of the Pings from a csv file, and stores them in all_pings,
        making use of the triangulator.triangulate() function.

        This method is intended to be used with the csv file that contains the
        compilation of pings recieved by the warehouse's three Access Points
        (warehouse_pings.csv). In that file, the following is guaranteed:
         - Each line contains one Access Point's record of one ping.
             - A record contains the following comma-separated values, in order:
                  1. The id of the vehicle which generated the ping
                  2. The timestamp of the ping
                  3. The distance from the ping to the Access Point
                  4. The name of the Access Point (AP1, AP2, or AP3)
         - There are three consecutive lines per Ping; one for each Access Point.
             - The three lines are always in order: AP1, AP2, then AP3.
         - Pings are listed in order, sorted first by vehicle, then by timestamp.
         - There are no extraneous lines.
        """
        with open(file_name, "r") as csvfile:
            csvreader = csv.reader(csvfile)

            for row in csvreader:
                vehicle_id = row[0]
                timestamp = int(row[1])
                distance_from_AP1 = float(row[2]) if row[3] == "AP1" else None
                distance_from_AP2 = (
                    float(csvreader.__next__()[2]) if row[3] == "AP1" else None
                )
                distance_from_AP3 = (
                    float(csvreader.__next__()[2]) if row[3] == "AP1" else None
                )

                if distance_from_AP1 and distance_from_AP2 and distance_from_AP3:
                    position = triangulate(
                        distance_from_AP1, distance_from_AP2, distance_from_AP3
                    )
                    ping = Ping(vehicle_id, timestamp, position)
                    self.all_pings.append(ping)
