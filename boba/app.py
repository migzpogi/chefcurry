import requests


def sum(a, b):
    """
    Returns the sum of a and b
    :param int a: First integer
    :param int b: Second integer
    :return int: Sum
    """

    return a+b


def get_foobar():
    """
    Makes an HTTP GET request
    :return:
    """

    r = requests.get("https://www.google.com")
    return r.status_code


print(get_foobar())