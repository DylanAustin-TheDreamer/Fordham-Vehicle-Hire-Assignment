from PythonScripts.Classes.Car import Car
from PythonScripts.Classes.Van import Van

def test_check_type():
    """ Return Cost Unit test function """

    car = Car("s")
    result = car.generate_cost()

    assert result == 22.50

def test_check_type_hp():
    """ Second Return Cost Unit test """

    car = Car("hp")
    result = car.generate_cost()

    assert result == 28

def test_check_type_van():
    """ Third Return Cost Unit test """

    van = Van("v")
    result = van.generate_cost()

    assert result == 35
    
    