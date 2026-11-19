from PythonScripts.AppFlow.account import login
from PythonScripts.AppFlow.selection import vehicle_select
from PythonScripts.AppFlow.summary import tally_price
import uuid

def main_application():
    """ Main Program Application """

    total_cost = None
    while total_cost == None:
        user = login()
        vehicle = vehicle_select()
        total_cost = tally_price(user=user, vehicle=vehicle)
    print("Thank you for using our service.")
    print(f"Your ticket Id is: {uuid.uuid4()}")
    print("-----------------------------------------------")
    print(f"total to pay: £{total_cost}")
    print("returnable deposit: £50")
    print("-----------------------------------------------")

main_application()
