from PythonScripts.Classes.Car import Car
from PythonScripts.Classes.Van import Van

def vehicle_select():
    """ Function that returns a selected vehicle """

    ended = False
    while ended == False:
        print("Please select from the following vehicle types: ")
        print("------------------------------------------------")
        print("Van = v\n", "Saloon = s\n", "High Performance = hp")
        selection = input()

        if selection == "v" or selection == "hp" or selection == "s":
            return make_vehicle(selection=selection)

def make_vehicle(selection):
    """ Function for returning a new vehicle object """

    if selection == "v":
        return Van(type=selection)
    else:
        return Car(type=selection)