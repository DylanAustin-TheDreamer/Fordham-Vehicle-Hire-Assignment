from ..Classes.User import User

def make_quote():
    """ Function to make user object """
    membership = None

    print("Are you an existing user?")
    print("YES / NO")
    print("--------------------------------")
    user_input = input()
    
    if user_input.lower() == "yes":
        while membership == None:
            print("Please enter your membership: \n")
            print("Bronze | Silver | Gold")
            user_input = input()
            if user_input.lower().strip() == "bronze" or user_input.lower().strip() == "silver" or user_input.lower().strip() == "gold":
                membership = user_input
            else:
                print("Please enter a valid selection")

        return User(membership=membership.lower().strip())
    else:
        return User(membership=None)