"""
This file is the entrypoint into the codebase. It runs some simple print
tests that you can use to help verify that your code is working correctly.

If you have time, add some tests of your own to ensure the code works
correctly.
"""

from warehouse_server import WarehouseServer
import ping_analytics


def main():
    print("~~~ Loading runner.py ~~~\n")
    print_intro("Warehouse Tracking")

    # Initialize the warehouse server
    warehouse_server = WarehouseServer()
    warehouse_server.load_pings("warehouse_pings.csv")
    print("~~~ WarehouseServer is initialized. ~~~\n")

    # Run Task 1 tests
    print("\n~~~ Task 1 ~~~\n")
    print_all_pings(warehouse_server)

    # Run Task 2 tests
    print("\n~~~ Task 2 ~~~\n")
    print_average_speeds(warehouse_server)

    # Run Task 3 tests
    print("\n~~~ Task 3 ~~~\n")
    print_check_for_damage(warehouse_server)

    # If you have time, add some tests of your own to ensure the code works
    # correctly.


def print_intro(codebaseTitle):
    """
    Prints a brief intro to the codebase.
    """
    print("Welcome to the " + codebaseTitle + " codebase!")
    print("Start by reading through the README file for your instructions,")
    print("then familiarize yourself with the rest of the files in the codebase.")
    print("When you're ready, start tackling the TODOs in the codebase.\n")


def print_all_pings(warehouse_server):
    """
    Prints out all Pings in the WarehouseServer.

    If everything's working right (and you haven't edited warehouse_pings.csv),
    all of the Pings' (x, y) coordinates should be whole numbers, and Vehicle A's
    Pings should be as follows:
        A: (0, 0)
        A: (0, 1)
        A: (0, 1)
        A: (0, 1)
        A: (0, 2)
        A: (0, 4)
        A: (0, 6)
        A: (0, 8)
        A: (0, 8)
        A: (0, 8)
    
    The other vehicles (B, C, and M) should also all have at least one Ping.
    """
    print("Pings in warehouse server: ")

    for ping in warehouse_server.all_pings:
        print(ping.vehicle_id + ": " + str(ping.position))
    print()


def print_average_speeds(warehouse_server):
    """
    Prints the result of calling get_average_speeds().

    If this is working right, Vehicle A's average speed should be 0.44 repeating.
    """
    average_speeds = ping_analytics.get_average_speeds(warehouse_server.all_pings)
    print("Average Speeds:", average_speeds)


def print_check_for_damage(warehouse_server):
    """
    Prints the result of calling check_for_damage().

    What the output of this one contains is totally up to you.
    """
    pings_by_vehicle = ping_analytics.get_pings_by_vehicle(warehouse_server.all_pings)
    potentially_damaged = ping_analytics.check_for_damage(pings_by_vehicle)
    
    print("Vehicles possibly damaged: ")
    for vehicle in potentially_damaged:
        print("\t " + vehicle)
    print()


if __name__ == "__main__":
    main()