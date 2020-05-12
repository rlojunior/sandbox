###########################################
# Desc: In class project.
#
# Author: Renlaod Junior
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # Input
    #height = 10
    height = float(input("What is the room height? "))
    
    #width1 = 20
    width1 = float(input("What is the wall ONE width? "))
    
    #width2 = 25
    width2 = float(input("What is the wall TWO width? "))

    square_feet_per_galon = 150
    
    # Process
    total_area1 = (height*width1)*2
    total_area2 = (height*width2)*2
    total_area = total_area1 + total_area2

    number_of_galons = round(total_area/square_feet_per_galon)

    # Output
    
    print("Your total area is {}".format(total_area))
    print("The number of galons are {} ".format(number_of_galons))


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()