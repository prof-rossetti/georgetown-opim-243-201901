from rideshare import trip

#
# QUESTION 10-F
#

# FUNCTION DEFINITION

def driver_promo(driver):
    if driver["avg_rating"] > 4.5:
        message = "DRIVER HAS GOOD RATING: " + str(driver["avg_rating"])
    else:
        message = "DRIVER HAS LOTS OF TRIPS: " + str(driver["total_rides"])

    return message

# FUNCTION INVOCATION

my_driver = trip["driver"]
print(driver_promo(my_driver))

other_driver = {"first_name": "___", "last_name": "____", "avg_rating": 4.9, "total_rides": 30}
print(driver_promo(other_driver)) #>
