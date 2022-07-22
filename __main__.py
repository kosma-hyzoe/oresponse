import requests
import sys
key = 'c579c9867ccd952827d1a891169a36c5'

def __main__():
    try:
        city = sys.argv[1]
        print(city)
    except IndexError:
        print("Usage: python3 -m orange_sun {city}")


if __name__ == '__main__':
    __main__()
