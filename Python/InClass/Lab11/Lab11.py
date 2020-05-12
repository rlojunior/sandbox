###########################################
# Desc: Lab11.
#
# Author: Reynaldo Jr.
###########################################

import csv

def main():
    fileName = "Ottawa_Ball_Diamonds.csv"
    accessMode = "r"
    
    userChoice = input("What the type of field would you like to list? (softball, baseball, or T-Ball) ")

    with open(fileName, accessMode) as myData:

        data = csv.reader(myData)
      

        for row in data:
            if userChoice == "softball" and row[3] == "softball":   
                print(row[2] +"  "+ row[5])
            elif userChoice == "baseball" and row[3] == "baseball":   
                print(row[2] +"  "+ row[5])
            elif userChoice == "T-Ball" and row[3] == "T-Ball":   
                print(row[2] +"  "+ row[5])

            
    


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()