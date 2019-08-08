"""Main script with menu and stuff"""

import re
from db.queries import (
    get_cars_prices,
    get_cars_by_price_range,
    get_colours,
    get_engines,
    get_gearboxes,
    get_models
)
from cars.car import CarBase
from app import create_app

# todo UI


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
                pretty_print(get_cars_prices())
        elif option == '2':
            while True:
                try:
                    price_range = tuple(
                        map(int,
                            re.split(r'[,-]',
                                     input("Enter price range in '(number)-(number)' format: \n"))))
                    with app.app_context():
                        pretty_print(get_cars_by_price_range(price_range))
                    break
                except (ValueError, IndexError):
                    print("Oops! Wrong format. Try again.")
                    continue
        elif option == '3':
            with app.app_context():
                models = get_models()
                print_parts(models)
                model = get_non_negative_int("Select Model: \n", max_value=len(models))
                gearboxes = get_gearboxes()
                print_parts(gearboxes)
                gearbox = get_non_negative_int("Select Gearbox: \n", max_value=len(gearboxes))
                colours = get_colours()
                print_parts(colours)
                colour = get_non_negative_int("Select Colour: \n", max_value=len(colours))
                engines = get_engines()
                print_parts(engines)
                engine = get_non_negative_int("Select Engine: \n", max_value=len(engines))
                car = CarBase(model, colour, gearbox, engine)
                print(car)
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
    for x in parts:
        print(x)


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
