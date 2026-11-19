# I had the idea of making an abstract class to be inherited
from ..Utilities.vehicle_cost import check_type

class Vehicle:
    def __init__(self, type):
        """ initialize object """

        self.type = type

    def generate_cost(self):
        """ Returns a base hire cost """

        return check_type(self.type)

    def get_type(self):
        return self.type
