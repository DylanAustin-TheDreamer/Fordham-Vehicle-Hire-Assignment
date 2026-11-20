from ..Classes.User import User
import json

def login():
    """ Function for user log-in """

    validated = False
    while validated == False:
        email = None

        print("Please choose from the following: ")
        print("-----------------------------------")
        print("Log in: 1")
        print("Create account: 2")

        user_input = input()

        if str(user_input) == "1":
            print("Please enter your email: \n")
            email = input()
            user = data_lookup(email = email)
            if user != None:
                return user
            print("User not found, please try again")
            continue
        elif str(user_input) == "2":
            print("Please enter your email: \n")
            email = input()
            return make_user(email=email, membership=None)
        else:
            continue

def data_lookup(email):
    """ Function to search user data """

    with open('Database/users.json', 'r') as file:
        data = json.load(file)

    if data["email"] != email:
        return
    else:
        # when found, run make_user() with the discovered user JSON object
        return make_user(email=data["email"], membership=data["membership"])

def make_user(email, membership):
    """ Function to make user object """

    if membership == None:
        return User(email=email, membership=None)
    else:
        return User(email=email, membership=membership)