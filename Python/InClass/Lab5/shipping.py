###########################################
# Desc: This application will calculate shipping charges
#       based on conditional statments
# Author: Reynaldo Junior
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # Input
    total_purchase = float(input("Enter the amount of your purchase: $"))
    
    # Process
    if total_purchase < 50:
        shipping_tax = 10
        total_cost = total_purchase + shipping_tax
        print("We add $10 of shipping cost. Your total cost is now ${0}".format(total_cost))
    else:
        print("Congrats! Your shipping is free")

    # Output
    print("Regards ;-)")

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()