# Task List

You may do these tasks in any order, but take note that they are listed in the order your team has prioritized completing them.

Reminder that you are NOT expected to complete all tasks. You are expected to write clean, readable code. Remember to add comments explaining what you were working on if you run out of time in the middle of a task.


## Task 1

The csv file **warehouse_pings.csv** contains all of the pings received by the three Access Points in the warehouse. This data needs to be ingested for analysis. In **warehouse_server.py**, implement the method with the prototype:

**load_pings(file_name)**

This method ingests data from the csv file and stores the information in  `self.all_pings` as a list of `Ping` objects. You will find **triangulator.py** essential for this task.

In the **warehouse_pings.csv** file, the following is guaranteed:

  1. Each line contains one Access Point's record of one ping.
      * A record contains the following comma-separated values, in order:
          - The id of the vehicle which generated the ping
          - The timestamp of the ping
          - The distance from the ping to the Access Point
          - The name of the Access Point (AP1, AP2, or AP3)
  2. There are three consecutive lines per ping; one for each Access Point.
      * The three lines are always in order: AP1,  AP2, then AP3.
  3. Pings are listed in order, sorted first by vehicle, then by timestamp.
  4. There are no extraneous lines.


## Task 2

Our client would like us to provide the average speed of each vehicle in the warehouse. We've implemented **get_average_speeds()** in **ping_analytics.py** to provide this information, but it relies on two helper functions that we have yet to implement.
First, implement the function with the prototype:

**get_pings_by_vehicle(pings)**

This function should take a list of `Pings` and split them into a dictionary containing `vehicle_ids` as keys and the list of `Pings` associated with each vehicle as values. You can assume the List of `Pings` is sorted by timestamp, and you should maintain that sort order in your resulting dictionary.

Second, implement the function with the prototype:
**get_total_distance_traveled(pings)**
This function should take the list of `Pings` associated with a single vehicle and return the total distance traveled by that vehicle. You can assume the list of `Pings` is already sorted chronologically by timestamp.

That should be enough to get our **get_average_speeds()** function into working order!


## Task 3

We want to be as proactive as possible in providing maintenance and repairs to our warehouse vehicles, especially those which may have been damaged. In **ping_analytics.py**, implement the function with the prototype:

**check_for_damage(vehicle_pings)**

This function should identify a list of vehicles that might need to be inspected. Examples of behavior that might warrant an inspection include vehicles which have been driven aggressively (quick acceleration and deceleration) or when vehicles collide with one another. You can use any heuristics you like, but are encouraged to make sure your decisions are well documented and your code is appropriately decomposed.

