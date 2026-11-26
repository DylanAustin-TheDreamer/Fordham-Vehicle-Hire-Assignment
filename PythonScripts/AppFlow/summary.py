
def tally_price(user, vehicle):
    """ Function for handling the final stage of the application """

    ended = False
    while ended == False:
        apply_discount = False
        apply_insurance = False
        apply_membership_discount = False
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
                    apply_insurance = True
                    total += 15.50

                total += vehicle.generate_cost()

                if user.get_membership() == "gold" and vehicle.get_type() == "hp":
                    total -= 18
                    apply_membership_discount = True

                discount = (total / 100) * 10

                if apply_discount == True and apply_insurance == True and apply_membership_discount == True:
                    return f"{(total - discount)} With a 10% discount, an £18 discount for gold membership and High Performance vehicle, and added Insurance of +£15.50"
                elif apply_discount == True and apply_insurance == True and apply_membership_discount == False:
                    return f"{(total - discount)} With a 10% discount, and added Insurance of +£15.50"
                elif apply_discount == True and apply_insurance == False and apply_membership_discount == False:
                    return f"{(total - discount)} With a 10% discount"
                else:
                    return total
        except:
            print("Enter a number")

        
        