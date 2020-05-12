###########################################
# Desc: TC5.
#
# Author: Reynaldo Junior.
###########################################


def main():
   
        
    getHighestCommonDivisor()   

    x = input("Do you like to try again? (y/n)").upper()
    if x == "Y":
        getHighestCommonDivisor()
    else:
        print()
    
    
         


def getHighestCommonDivisor():
    
    num1 = input("Enter ther first number: ")
    if (not num1.isnumeric()):
        print("ERROR! Enter a valid first number.")
    else:
        num1 = int(num1)
    num2 = input("Enter ther second number: ")
    if (not num2.isnumeric()):
        print("ERROR! Enter a valid second number.")
    else:
        num2 = int(num2)
    

    

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()