from math import radians, sin, asin, sqrt, cos


def get_distance(latitude_x, longitude_x, latitude_y, longitude_y):
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lat1 = radians(latitude_x)
    lon1 = radians(longitude_x)
    lat2 = radians(latitude_y)
    lon2 = radians(longitude_y)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2

    c = 2 * asin(sqrt(a))

    # Radius of earth in kilometers. Use 3956 for miles
    radius = 6371

    # calculate the result
    return c * radius

