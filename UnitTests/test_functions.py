from PythonScripts.AppFlow.summary import tally_price
from PythonScripts.Classes.User import User
from PythonScripts.Classes.Car import Car

def test_tally_price_no_insurance(monkeypatch):
    responses = iter(["5", "no"])
    monkeypatch.setattr("builtins.input", lambda: next(responses))

    user = User(membership="none")
    vehicle = Car(type="s")

    result = tally_price(user, vehicle)

    assert result == vehicle.generate_cost()

def test_tally_price_with_insurance(monkeypatch):
    responses = iter(["5", "yes"])
    monkeypatch.setattr("builtins.input", lambda: next(responses))

    user = User(membership="none")
    vehicle = Car(type="s")

    result = tally_price(user, vehicle)

    assert result == vehicle.generate_cost() + 15.50

def test_tally_price_with_insurance_and_membership(monkeypatch):
    responses = iter(["5", "yes"])
    monkeypatch.setattr("builtins.input", lambda: next(responses))

    user = User(membership="gold")
    vehicle = Car(type="hp")

    result = tally_price(user, vehicle)
    print(result)
    assert result == (vehicle.generate_cost() + 15.50) -18
