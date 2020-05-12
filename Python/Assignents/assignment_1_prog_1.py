###########################################
# Desc: Assignment 1 - Hipster's Local Vinyl Records
#
# Author: Reynaldo Junior.
###########################################

"""
Pseudocode: 
    Here follow what the user should enter:
        1) Ask the user to enter the customer`s name
        2) Ask the user to enter how many kilometers is
        the customer`s home is from the store
        3)Ask the user to enter the cost of record purchase
    
    Here follow what the program is going to produce:
        1) Calculate the delivery cost =  $15 * distance from customer`s fome to the store 
        2) Calculate the purchase cost = price of the product + 14% of the product`s price
        3) Calculate the total cost = delivery cost + purchase cost
        
"""



def main():
    #Presenting to the user the title of the program    
    print("Hipster`s Local Vinyl Records - Customer Order Details")
    
    #just adding a blank line
    print("")

    # Input
    #Ask the user to enter the customer`s name
    customer_name = input("Enter the customer`s name: ") 

    #Ask the user to enter the distance (in kilometers)
    distance = float(input("Enter the distance in kilometers for delivery: ")) 

    #Ask the user to enter the cost of record purchase
    item_cost = float(input("Enter the cost of records purchased: ")) 


    # Process
    #each kilometer cost $15
    cost_per_kilometer = 15 

    #calculating the delivery cost
    delivery_cost = distance * cost_per_kilometer 

    #the tax is 14% of the product`s price
    tax = 0.14 

    #calculating the purchase cost
    purchase_cost = item_cost + item_cost * tax 

    #The amount that the customer will pay
    total_cost = purchase_cost + delivery_cost 
    

    # Output
    print("") #just print a blank line

    print("Purchase summary for {}".format(customer_name))

    print("Delivery Cost: ${0:.2f}".format(delivery_cost))

    print("Purchase Cost: ${0:.2f}".format(purchase_cost))

    print("Total Cost: ${0:.2f}".format(total_cost))
    



#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()