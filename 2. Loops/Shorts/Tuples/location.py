import sys


def main():
    coordinates_tuple = (42.376, -71.115)
    coordinates_list = [42.376, -71.115]

    print(f"{sys.getsizeof(coordinates_tuple)} bytes")
    print(f"{sys.getsizeof(coordinates_list)} bytes")

    # coordinates[0] = -42.376 # Immutable - TypeError: 'tuple' object does not support item assignment

    # latitude, longitude = coordinates
    #
    # print(f"Latitude: {latitude}")
    # print(f"Longitude: {longitude}")


main()