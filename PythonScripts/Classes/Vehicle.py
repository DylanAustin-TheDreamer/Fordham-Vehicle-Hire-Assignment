from ..Utilities.vehicle_cost import check_type

class Vehicle:
    def __init__(self, type):
        """ initialize object """

        self.type = type

    # we use the type in the utility function - vehicle_cost.py
    # I will use more conventional OOP styles in my OOP assignment.
    def generate_cost(self):
        """ Returns a base hire cost """

        return check_type(self.type)

    def get_type(self):
        return self.type