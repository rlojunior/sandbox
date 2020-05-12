###########################################
# Desc: This application calcules the tax due
#
# Author: Reynaldo Junior
###########################################

def main():
    
    # Adding the title
    print("Tax Withholding Calculator \n")

    # Input
    weekly_salary = int(input("Please enter the full amount of your weekly salary: "))
    #weekly_salary = 1000
    
    n_dependents = int(input("How many dependents do you have?: "))
    print("")
    #n_dependents = 2

    
    # Process

    # The provincial tax is 6% of the weekly salary
    provincial_tax = 0.06*weekly_salary

    # The federal tax is 25% of the weekly salary
    federal_tax = 0.25*weekly_salary

    # For each dependent We deduct 2% (calculated based on the weekly salary)
    deduction = n_dependents * 0.02 * weekly_salary

    # Here is the total due
    total_tax = provincial_tax + federal_tax - deduction

    # Here is how much the person will receive
    total_take_home = weekly_salary - total_tax

    # Output
    print("Provincial Tax Withheld: ${0:.2f}".format(provincial_tax))
    print("Federal Tax Withheld: ${0:.2f}".format(federal_tax))
    print("Dependent Deduction for {0} dependents: ${1:.2f}".format(n_dependents, deduction))
    print("Total Withheld: ${0:.2f}".format(total_tax))
    print("Total Take-Home Pay: ${0:.2f} \n".format(total_take_home))






    

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()