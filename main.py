"""
The main module at start of which the map is created based on the user input
with the film_chooser.py module.
"""

from time import sleep
import film_chooser as flmc


def slow(message):
    """
    Print text slowly creating an effect of printing machine.
    """
    for letter in message:
        print(letter, end='', flush=True)
        sleep(0.1)


def main():
    """
    Run the program and build a map.
    """
    year = int(input("Please enter a year you would like to have a map for: "))
    user_location_str = input(
        "Please enter your location(format: lat, long): ")
    user_location = (float(user_location_str.split(',')[0][1:]),
                     float(user_location_str.split(',')[1][:-1]))
    slow("Map is generating...\n")
    slow("Please wait...\n")
    film_list = flmc.read_file("small.list")
    one_year = flmc.one_year_films(year, film_list)
    coord_list = flmc.address_to_coordinates(one_year)
    closest_films = flmc.determine_ten_closest(coord_list, user_location)
    flmc.map_builder(closest_films, user_location, year)
    slow(f"Finished. Please have a look at the {year}_film_map.html\n")


if __name__ == "__main__":
    main()
