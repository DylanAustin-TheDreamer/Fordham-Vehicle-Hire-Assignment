from PythonScripts.AppFlow.account_style import login
from PythonScripts.AppFlow.quote_style import make_quote
from PythonScripts.AppFlow.selection import vehicle_select
from PythonScripts.AppFlow.summary import tally_price
import uuid

def main_application():
    """ Main Program Application """

    total_cost = None
    while total_cost == None:
        # I have removed user login functionality since it was not in line with the assignment requirements
        # user = login()

        # The quote style is more in line with the assignment requirements. I would like to document that I-
        # can understand the assignment requirements
        quote = make_quote()
        vehicle = vehicle_select()
        total_cost = tally_price(user=quote, vehicle=vehicle)
    print("Thank you for using our service.")
    print(f"Your ticket Id is: {uuid.uuid4()}")
    print("-----------------------------------------------")
    print(f"total to pay: £{total_cost}")
    print("returnable deposit: £50")
    print("-----------------------------------------------")

main_application()
