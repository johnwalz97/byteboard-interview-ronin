"""
A library of functions for analyzing Pings.
"""

from position import Position


def get_average_speeds(pings):
    """
    Takes a list of Pings, and returns a dictionary of vehicle_ids to their
    corresponding average speeds.

    Assumes the list of Pings is already sorted chronologically by timestamp.
    """
    vehicles = get_pings_by_vehicle(pings)
    average_speeds = {}

    for vehicle in vehicles:
        vehicle_pings = vehicles[vehicle]

        total_distance = get_total_distance_traveled(vehicle_pings)

        # if the vehicle hasn't traveled, set its average speed to 0
        if len(vehicle_pings) <= 1:
            average_speeds[vehicle] = 0
            continue

        # The total travel time is just the timestamp of the last Ping
        # minus the timestamp of the first Ping
        total_time = vehicle_pings[-1].timestamp - vehicle_pings[0].timestamp

        # store this vehicle's average speed (total distance / total time)
        # in the dictionary
        average_speeds[vehicle] = total_distance / total_time

    return average_speeds


def get_pings_by_vehicle(pings):
    """
    Takes a list of Pings, and returns a dictionary of vehicle_ids to the
    list of Pings associated with that vehicle.

    Assumes the list of Pings is already sorted chronologically by timestamp,
    and maintains that sort order in the resulting dictionary.
    """
    vehicles = {}

    for ping in pings:
        if ping.vehicle_id not in vehicles:
            vehicles[ping.vehicle_id] = []

        vehicles[ping.vehicle_id].append(ping)

    return vehicles


def get_total_distance_traveled(pings):
    """
    Given a list of Pings for a single vehicle, determines the total
    distance traversed by that vehicle.

    Assumes the list of Pings is already sorted chronologically by timestamp.
    """
    total_distance = 0

    for i in range(1, len(pings)):
        current_position = pings[i].position
        previous_position = pings[i - 1].position
        distance = Position.get_distance(current_position, previous_position)
        total_distance += distance

    return total_distance


def check_for_damage(vehicle_pings):
    """
    Given a dictionary of vehicle_ids to their corresponding list of Pings,
    identifies vehicles that might need to be inspected, and returns a list
    of their vehicle_ids. More details can be found in the README.

    Please note that these are somewhat naive implementations. There are much better
    and smarter ways to calculate this but I didn't have time to implement them.
    """
    damaged_vehicles = set()

    acceleration_threshold = (
        2  # Threshold for detecting quick acceleration or deceleration
    )
    collision_distance_threshold = 1  # Threshold for detecting potential collisions
    timestamp_difference_threshold = 5  # Threshold for time difference between pings

    # Check for potential reckless driving or collisions with other objects
    for vehicle_id, pings in vehicle_pings.items():
        # look at a window of 3 pings at a time and calculate the accel/decel based on those
        # this will tell us if the operator drive recklessly or if the vehicle hit something
        for i in range(2, len(pings)):
            current_distance = Position.get_distance(
                pings[i].position, pings[i - 1].position
            ) # get distance between current and previous ping
            previous_distance = Position.get_distance(
                pings[i - 1].position, pings[i - 2].position
            ) # get distance between previous ping and the one before that

            # acceleration is the absolute difference between 2 distances
            if abs(current_distance - previous_distance) >= acceleration_threshold:
                damaged_vehicles.add(vehicle_id)
                break

    # Check for potential vehicle collisions
    for vehicle_id_1, pings_1 in vehicle_pings.items():
        # Check each vehicle against every other vehicle (except itself)
        for vehicle_id_2, pings_2 in vehicle_pings.items():
            if vehicle_id_1 == vehicle_id_2:
                continue

            i, j = 0, 0 # pointers i and j for traverse each vehicle's ping list
            while i < len(pings_1) and j < len(pings_2):
                timestamp_1 = pings_1[i].timestamp
                timestamp_2 = pings_2[j].timestamp

                # If the timestamps are within the threshold, check for a collision
                if abs(timestamp_1 - timestamp_2) <= timestamp_difference_threshold:
                    distance_between_vehicles = Position.get_distance(
                        pings_1[i].position,
                        pings_2[j].position,
                    )

                    if distance_between_vehicles <= collision_distance_threshold:
                        damaged_vehicles.add(vehicle_id_1)
                        damaged_vehicles.add(vehicle_id_2)

                # increment the pointer for the vehicle with the earlier timestamp
                if timestamp_1 <= timestamp_2:
                    i += 1
                else:
                    j += 1

    return damaged_vehicles
