###########################################
# Desc: Program 1 – Landscape Calculator .
#
# Author: Reynaldo Junior.
###########################################

""" A landscaping company needs a program that computes the price of landscaping for a new housing development. Work orders are based on: address, plot length and width in feet, type of grass (“fescue”, “bentgrass” or “campus”), and number of trees. The price is computed as follows:  
•	There is a base labour charge of $1000. 
•	If the surface (length * width) is over 5000 square feet, add $500. 
•	The cost is calculated per square foot. If the grass is “fescue” the cost is $0.05; for “bentgrass” it is $0.02; “campus” is $0.01. 
•	Each tree requested has a $100 charge. 
 """






#global variable. It will be used by the main() and surface_calculator() functions
area_extra_fee = 0  

def main():
    #Base labour charge
    base_labour = 1000    

    #It is the cost of each tree
    tree_unit_cost = 100  

    # Input
    House_number = int(input("Enter House Number: "))
    Property_depth = int(input("Enter property depth (feet): "))
    Property_width = int(input("Enter property width (feet): "))
    Grass_type = input("Enter type of grass (fescue, bentgrass, campus): ").upper()
    Tree_number = int(input("Enter the number of trees: "))

    # Process
    #Calculate the surface area
    area = surface_calculator(Property_depth,Property_width)

    #Calculate the 'grass tax' based on which type of grass the customer wants
    grass_tax = grass_calculation(Grass_type)

    #Calculate the amount ($) based on how many trees the customer wants
    tree_amount = Tree_number * tree_unit_cost

    #Calculate the cost ($) of the grass used based in total area and the type of the grass 
    grass_cost = area*grass_tax

    #Calculate the final amount due
    total_amount = base_labour + tree_amount +grass_cost + area_extra_fee
    
    
    # Output
    
    print("Total cost for house {0} is: ${1:.2f}".format(House_number,total_amount))

#Function to calculate/evaluate the surface area 
def surface_calculator(depth, width):
    global area_extra_fee
    Surface_area = depth * width
    if Surface_area > 5000:
        area_extra_fee = 500
    else:
        area_extra_fee = 0 
    return Surface_area

#Function to calculate the 'grass tax' based on the type of the grass used
def grass_calculation(type):
    fescue_tax = 0.05
    bentgrass_tax = 0.02
    campus_tax = 0.01
    grass_total = 0
    if type == "FESCUE":
        grass_tax = fescue_tax
    elif type == "BENTGRASS":
        grass_tax = bentgrass_tax
    elif type == "CAMPUS":
        grass_tax = campus_tax
    return grass_tax



#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()