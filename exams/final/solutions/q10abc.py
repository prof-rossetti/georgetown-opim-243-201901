from rideshare import trip

#
# QUESTION 10-A
#

print("Your driver is " + trip["driver"]["first_name"])

#
# QUESTION 10-B
#

print(len(trip["stops"]))

#
# QUESTION 10-C
#

print(trip["stops"][0]["passenger"])
