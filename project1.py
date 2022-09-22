#!/usr/bin/env python3

"""Program that displays lists of locations based off of user input"""


def main():
    # list of vacation destinations based on the season of year
    fall_locations = ["Yellowstone", "Zion National Park", "The Berkshires"]
    spring_locations = ["Grand Canyon", "Madrid", "Maldives"]
    summer_locations = ["Bar Harbor", "San Diego", "Outer Banks"]
    winter_locations = ["Galapagos Islands",
                        "Costa Rica", "U.S. Virgin Islands"]

    print("\nReady for vacation? Hopefully I can help guide you to your dream destination!\n")

    # ask user for desired season and store in time_of_year variable
    season = input(
        "Please enter the season you would like to travel during:\n\tSpring, Summer, Fall, Winter\n> ")

    # lowercase user input
    season = season.lower()

    while True:
        # print list of locations depending on user input for the season
        if season == "spring":
            print("Here is a list of some of the best vacations during the Spring!\n")
            print(*spring_locations, sep=", ")
            break
        elif season == "summer":
            print("Here is a list of some of the best vacations during the Summer!\n")
            print(*summer_locations, sep=", ")
            break
        elif season == "fall":
            print("Here is a list of some of the best vacations during the Fall!\n")
            print(*fall_locations, sep=", ")
            break
        elif season == "winter":
            print("Here is a list of some of the best vacations during the Winter!\n")
            print(*winter_locations, sep=", ")
            break
        else:
            print("Please enter one of the following:\n\tSpring, Summer, Fall, Winter")
            break


if __name__ == "__main__":
    main()
