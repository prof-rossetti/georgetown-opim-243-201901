from rideshare import trip

#
# QUESTION 10-E
#

# SOLUTION

fares = [stop["fare"] for stop in trip["stops"]]

total_fare = sum(fares)

print("$" + str(total_fare))

# ALSO CORRECT

total_fare = 0

for stop in trip["stops"]:
    total_fare = total_fare + stop["fare"]

print("$" + str(total_fare))

# ALSO CORRECT

total_fare = 0

for i in range(0, len(trip["stops"])):
    total_fare = total_fare + trip["stops"][i]["fare"]

print("$" + str(total_fare))
