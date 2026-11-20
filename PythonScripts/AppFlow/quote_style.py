from ..Classes.User import User

def make_quote():
    """ Function to make user object """
    membership = None
    email = None

    print("Are you an existing user?")
    print("YES / NO")
    print("--------------------------------")
    user_input = input()
    
    while email == None:
        if user_input.lower().strip() == "yes":
            print("Please enter your email: \n")
            user_input = input()
            if "@" in user_input.lower() and ".com" in user_input.lower() or ".co.uk" in user_input.lower():
                email = user_input
            else:
                print("Please enter a valid email - Must include @ and .com or .co.uk")
        else:
            membership = "no_existing"
            print("Please enter your email: \n")
            user_input = input()
            if "@" in user_input and ".com" in user_input or ".co.uk" in user_input:
                email = user_input
            else:
                print("Please enter a valid email - Must include @ and .com or .co.uk")
    
    while membership == None:
        print("Please enter your membership: \n")
        print("Bronze | Silver | Gold")
        user_input = input()
        if user_input.lower().strip() == "bronze" or user_input.lower().strip() == "silver" or user_input.lower().strip() == "gold":
            membership = user_input
        else:
            print("Please enter a valid selection")

    if membership == "no_existing":
        return User(email=email, membership=None)
    else:
        return User(email=email, membership=membership.lower().strip())