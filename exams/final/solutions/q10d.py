from rideshare import trip

#
# QUESTION 10-D
#

# SOLUTION

for stop in trip["stops"]:
    print(stop["destination"])

# ALSO CORRECT

[print(stop["destination"]) for stop in trip["stops"]]

# ALSO CORRECT

stop_count = len(trip["stops"])

for i in range(0, stop_count):
    print(trip["stops"][i]["destination"])

# ALSO CORRECT

i = 0
stop_count = len(trip["stops"])

while i < stop_count:
    print(trip["stops"][i]["destination"])
    i = i + 1
