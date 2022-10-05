# A program that asks the user to enter a city, and returns various time info like sunrise and sunset.
# Throws an error if the user enters an invalid city
# @author Nishank Kuppa

# Astral is a python package for calculating the times of various aspects of the sun and phases of the moon.
# https://astral.readthedocs.io/en/stable/index.html

import datetime

from astral.geocoder import database, lookup
from astral.sun import sun

while True:
    try:
        # Ask the user what city they want time info on:
        userCity = input("What city do you want to look up? \n")

        # Look up the city and then print relevant information.
        city = lookup(userCity, database())
        print((
            f'Information for {city.name}/{city.region}\n'
            f'Timezone: {city.timezone}\n'
            f'Latitude: {city.latitude:.03f}; Longitude: {city.longitude:.03f}\n'
        ))

        # Return the dawn, sunrise, noon, sunset, and dusk times.
        s = sun(city.observer, date=datetime.date.today(), tzinfo=city.timezone)
        print((
            f'Dawn:    {s["dawn"]}\n'
            f'Sunrise: {s["sunrise"]}\n'
            f'Noon:    {s["noon"]}\n'
            f'Sunset:  {s["sunset"]}\n'
            f'Dusk:    {s["dusk"]}\n'
        ))
        break

    except KeyError:
        print("This is an invalid city, please try again.")




