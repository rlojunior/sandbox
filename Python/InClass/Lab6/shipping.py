###########################################
# Desc: This program will calculate the total to charge for an order 
#       from an online store in Canada.
# Author: Reynaldo Junior.
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    ALBERTA_TAX = 0.05
    ONTARIO_AND_OTHERS_TAX = 0.15
    ALL_OTHER_PROVINCE = 0.11
    
    tax_amount = 0

    # Input
    total_purchase = float(input("How much is the purchase? "))
    country = input("Where are you? ").upper()
    
    #total_purchase = 1000
    #country = "CANADA"
    

    # Process
    if country == 'CANADA':
        province = input("What is your province? ").upper()
        if province == "ALBERTA":
            tax_amount = total_purchase*ALBERTA_TAX
        elif province == "ONTARIO" or province == "NEW BRUNSWICK" or province == "NOVA SCOTIA":
            tax_amount = total_purchase*ONTARIO_AND_OTHERS_TAX
        else:
            tax_amount = total_purchase*ALL_OTHER_PROVINCE 
    else:
        print('No charge will be applied in your order' )

    print("Your total tax is: ${0:.2f}".format(tax_amount))

    total_amount = total_purchase + tax_amount
    
    # Output
    print("Your total amount is: ${0:.2f}".format(total_amount))
    

#PROGRAM :
if __name__ == "__main__":
    main()