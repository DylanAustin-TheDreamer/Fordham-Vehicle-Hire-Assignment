def tally_price(user, vehicle):
    """ Function for handling the final stage of the application """

    ended = False
    while ended == False:
        apply_discount = False
        total = 0
        print("----------------------------------------")
        print("Final Steps: ")
        print("How many days would you like to hire for? \n", "1 - 10 \n")
        hire_days = input()
        try:
            if int(hire_days) < 1 or int(hire_days) > 10:
                print("Please enter a number between 1 and 10")
                continue
            else:
                if int(hire_days) > 7:
                    apply_discount = True
                print("Would you like to include insurance for your hire? \n", "YES/NO \n")
                insurance = input()
                if insurance.lower() == "yes":
                    total += 15.50

                total += vehicle.generate_cost()

                if user.get_membership() == "gold" and vehicle.get_type() == "hp":
                    total -= 18

                discount = (total / 100) * 10

                if apply_discount == True:
                    return (total - discount)
                else:
                    return total
        except:
            print("Enter a number")

        
        