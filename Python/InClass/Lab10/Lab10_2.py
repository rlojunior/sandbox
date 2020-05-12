###########################################
# Desc: Create a .csv file and a user input.
#
# Author: Reynaldo Junior.
###########################################

def main():
    filename = "GuestList_version_2.csv"
    accessMode = "a"
    myfile = open(filename,accessMode)
    print("If you don't want to add mor names type `no` \n")

    choice = True
    while choice:
        user_input = input("Enter the name and age of your guests (format: name, age): ")

        if user_input == "no":
            choice = False
        else:
            myfile.write(user_input)
            myfile.write("\n")

    myfile.close()

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()