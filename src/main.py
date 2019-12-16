"""Main script"""

from app import create_app


def main():
    """
    Entry point. Starting an app. Printing out what we are doing
    """

    app = create_app()
    print('Starting a server...')
    app.run(host='0.0.0.0')


if __name__ == "__main__":
    main()
