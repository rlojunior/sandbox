###########################################
# Desc: TC 6.
#
# Author: Reynaldo junior.
###########################################

import csv

def main():
    fileNamme = "TC6_monsters.csv"
    accessMode = "r"

    


    print("Welcome to the Dungeon Attack application where none shall survive! Simply try to live as long as you can.")
           

    while True:
        continue_question = input("Hit any key to continue ('Q' or 'q' to quit): ")
        if continue_question.lower() == "q":
            print("That's it. Retreat in fear and warn your friends")
            break

        initial_hit_point =-1

        error_message ="You do not listen very well do you? Think you are going to survive this dungeon?" 
        
        while initial_hit_point == -1:
                    
            while True:
                try:                
                    initial_hit_point = int(input("Please enter your initial hit point (1-200): "))
                    if initial_hit_point < 1 or initial_hit_point > 200:
                        print(error_message)
                    else:
                        break
                except:
                    print(error_message)
                
                

        print("Lets continue")
        
        with open(fileNamme,accessMode) as myCSVFile:
            dataFromFile = csv.reader(myCSVFile)
            for row in dataFromFile:
                print("You are attacked by {}".format(row[0]))

            

  

            


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()