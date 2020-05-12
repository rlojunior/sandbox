###########################################
""" 
 Desc: This program requires the user to enter the
    bill amount (input) and the result (output) will be the total 
    amount plus tax and plus tip.

 Author: Reynaldo Junior.

 """
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # Input
    #bill_amout is the variable that store the original amount
    bill_amount = input("Please enter your original bill amount: $")

    # Process

    # tax is the variable that store the value os the tax.
    # tax = 15% of the original amount(bill_amount variable)
    tax = 0.15*float(bill_amount)

    # tip is the variable that store the value os the tip.
    # tip = 20% of the original amount(bill_amount variable)
    tip = 0.20*float(bill_amount)

    #total variable is the total amount of thw bill
    #total = original amount + tax amount + tip amount
    total = float(bill_amount) + tax + tip

    # Output
    print("Your original bill amount is: $"+str(bill_amount))
    print("Your tax is: $"+ str(round(tax,2)))
    print("Your tip is: $"+str(round(tip,2)))
    print("Your total is: $"+ str(round(total,2)))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()