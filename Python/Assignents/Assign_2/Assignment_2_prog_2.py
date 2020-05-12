###########################################
# Desc: Program 2 – Erewhon Mobile Data Plans .
#
# Author: Reynaldo Junior.
###########################################

def main():
    # Input

    Data_usage = int(input("Enter the data usage (Mb): "))

    # Process

    #Call the function charge_calculator() to calculate the total amount due
    Total_charge = charge_calculator(Data_usage)
        
    # Output
    print("Total charge is ${0:.2f}".format(Total_charge))
    

#Function to calculate the charge due based in a data usage 
def charge_calculator(data):
    flat_rate_upto_200 = 20
    tax_upto_500 = 0.105
    tax_upto_1000 = 0.110
    flat_rate_over_1000 = 118
    
    if data <= 200:
        charge = flat_rate_upto_200

    elif data > 200 and data <=500:
        tax = tax_upto_500
        charge = data * tax

    elif data > 500 and data <=1000:
        tax = tax_upto_1000
        charge = data * tax

    else:
        charge = flat_rate_over_1000

    return charge


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()