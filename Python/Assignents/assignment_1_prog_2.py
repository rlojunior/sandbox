###########################################
# Desc: Assignment 1 - Weekly Loan Calculator
#
# Author: Reynaldo Junior
###########################################

"""
Pseudocode:
    Here follow what the user should enter:
    1) Ask the user to enter the amount of the loan borrowed
    2) Ask the user to enter the interest rate
    3) Ask the user to enter the number of years

    Here follow what the program is going to produce:
    1) using the weekly payment formula, calculate the
    amount to be payed weekly
"""


def main():
    #Print the title of the program
    print("Weekly Loan Calculator")

    #Add a blank line
    print ("")

    # Input
    # Ask the user the amount borrowed by the customer
    loan_amount = float(input("Enter the amount of loan: "))
    
    # Ask the user the interest`s rate
    rate = float(input("Enter the interesr rate: "))
    
    # Ask the user how many years the customer plans to pay the loan
    years = int(input("Enter the number of years: "))



    # Process
    # A variable for the calculation
    i_index = rate/5200

    # the formula for calculate the weekly payment based on the loan borrowed and the years 
    weekly_payment = (i_index/(1-(1+i_index)**(-52*years))*loan_amount)

    
    # Output
    #Add a blank line
    print ("")


    print("Your weekly payment will be: ${0:.2f}".format(weekly_payment))





#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()