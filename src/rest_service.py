import requests


class RESTService:

    def __init__(self):
        pass

    """
    :arg
    """

    def get_data(self, URL):
        r = requests.get(URL)
        