###########################################
# Desc: Lab12.
#
# Author: Reynaldo Junior.
###########################################

def main():
    
    filename = "GuestList.csv"
    accessMode = "w"
    
    myGuest = open(filename, accessMode)

    names = " "

    while names != "":
        
        names = input("Enter the NAME of the guest: ")
        
       # age = int(input("Enter the AGE of the guest: "))
       # myGuest.write(names + "," + str(age) + "\n")
        
        
        try:
            age = int(input("Enter the AGE of the guest: "))
            myGuest.write(names + "," + str(age) + "\n")
        except ValueError:
            print("You didn't enter a valid AGE.")
        except:
            print("This is an unexpected error")
        
        
        
        

    myGuest.close()
    


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()