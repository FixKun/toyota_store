"""Main script with menu and stuff"""

import re
from helpers.queries import (
    get_cars_prices,
    get_cars_by_price_range,
    get_colours,
    get_engines,
    get_gearboxes,
    get_models,
    save_car
)
from cars.car import CarBase


def main():
    """
    Menu for getting and adding cars
    """
    while True:
        print('Select an option: \n '
              '1: Get all cars \n '
              '2: Get cars in price range \n '
              '3: Add new car \n '
              '4: Quit \n')
        option = input("So...: ")
        if option == '1':
            pretty_print(get_cars_prices())
        elif option == '2':
            while True:
                try:
                    price_range = tuple(
                        map(int,
                            re.split(r'[,-]',
                                     input("Enter price range in '(number)-(number)' format: \n"))))
                    pretty_print(get_cars_by_price_range(price_range))
                    break
                except ValueError:
                    print("Oops! Wrong format. Try again.")
                    continue
        elif option == '3':
            get_models()
            model = get_non_negative_int("Select Model: \n")
            get_gearboxes()
            gearbox = get_non_negative_int("Select Gearbox: \n")
            get_colours()
            colour = get_non_negative_int("Select Colour: \n")
            get_engines()
            engine = get_non_negative_int("Select Engine: \n")
            car = CarBase(model, colour, gearbox, engine)
            print(car)
            save_car(car)

        elif option == '4':
            break
        else:
            print('Wrong option. Try again.')


def pretty_print(cars):
    """ Format car attributes and print in a readable way"""
    if not cars:
        print("There's nothing to show.\n\n")
    else:
        for car in cars:
            print(f"{car[0]} is {car[1]} USD")
    print("\n\n")


def get_non_negative_int(prompt):
    """re-use input validation"""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Oops! This is not a number. Try again.")
            continue

        if value < 0:
            print("Oops! Number must not be negative.")
            continue
        else:
            break
    return value


if __name__ == "__main__":
    main()
