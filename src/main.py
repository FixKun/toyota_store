"""Main script with menu and stuff"""

import re
from cars.parts import (
    Model,
    Gearbox,
    EngineCapacity,
    Colour)
from cars.car import CarBase
from app import create_app


def main():
    """
    Menu for getting and adding cars
    """

    app = create_app()

    while True:
        print('Select an option: \n '
              '1: Get all cars \n '
              '2: Get cars in price range \n '
              '3: Add new car \n '
              '4: Quit \n'
              '5: Let\'s start a server... \n')
        option = input("So...: ")
        if option == '1':
            with app.app_context():
                pretty_print(CarBase.get_cars_prices())
        elif option == '2':
            while True:
                try:
                    price_range = tuple(
                        map(int,
                            re.split(r'[,-]',
                                     input("Enter price range in '(number)-(number)' format: \n"))))
                    with app.app_context():
                        pretty_print(CarBase.get_cars_by_price_range(price_range))
                    break
                except (ValueError, IndexError):
                    print("Oops! Wrong format. Try again.")
                    continue
        elif option == '3':
            with app.app_context():
                models = Model.get_models()
                print_parts(models)
                model = get_non_negative_int("Select Model: \n", max_value=len(models))
                gearboxes = Gearbox.get_gearboxes()
                print_parts(gearboxes)
                gearbox = get_non_negative_int("Select Gearbox: \n", max_value=len(gearboxes))
                colours = Colour.get_colours()
                print_parts(colours)
                colour = get_non_negative_int("Select Colour: \n", max_value=len(colours))
                engines = EngineCapacity.get_engines()
                print_parts(engines)
                engine = get_non_negative_int("Select Engine: \n", max_value=len(engines))
                car = CarBase(model, colour, gearbox, engine)
                car.save_car()

        elif option == '4':
            break
        elif option == '5':
            print('Starting a server...')
            app.run()
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


def print_parts(parts):
    """ Printing parts of a car to a console """
    for part in parts:
        print(part)


def get_non_negative_int(prompt, max_value=None):
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
        elif max_value:
            if value >= max_value:
                print("Please, select one of the options above.")
                continue
            else:
                break
        else:
            break
    return value


if __name__ == "__main__":
    main()
