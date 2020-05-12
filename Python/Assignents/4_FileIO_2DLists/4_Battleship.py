###########################################
# Desc: Assignment 4 - Prog 3.
#
# Author: Reynaldo Junior.
###########################################

# A simple version of the game Battleship.

def main():

    missiles_remaining = 30
    
    #opening the map.txt provided
    filename_map = "Files\\map.txt"
    my_map= open(filename_map,"r")

    columns = ["A","B","C","D","E","F","G","H","I","J"]
    rows = ["1","2","3","4","5","6","7","8","9","10"]

    #creating an empty matrix. This matrix is where I going to put the O's and X's on the screen
    rows_total = len(columns)
    columns_total = len(rows)
    matrix = [[0] * columns_total for i in range(rows_total)]
    for i in range(rows_total):
        for j in range(columns_total):
            matrix[i][j] = " "
    
    # printing the frame of the screen. I mean, printing A to J (columns) and 1 to 10 (rows)
    print_board(matrix, columns)

    
    # I transformed the file map.txt in a 2D vector (map_array)
    map_array =[]    
    with my_map as map:
        for row in map:
            map_array.append(row)
    

    # I created a 1D vector (map_fleet_ones) to store the place (xy) where the 1's are.
    # This vector will help me to evaluate the user input. 
    # Instead to go throught the entire map file, I will search if the user is wrong/correct
    # just serching in the vector map_fleet_ones.
    map_fleet_ones = []
    total_one = 0
    for i in range(0,9):
        for j in range(1,20):
            if map_array[i][j] == "1":
                total_one += 1 
                map_fleet_ones.append([i,int(j/2)])

    
    #This variable will store how many hits the user did (i.e. the user found where the '1' is).
    total_hit = 0

    
    #This is the main loop of the game. It is based in how many missile the user has.
    while missiles_remaining > 0:
        missiles_remaining -= 1
        user_option = input("Choose your target (Ex. A1): ").upper()
        user_option_converted = "["+str(rows.index(user_option[1:3]))+","+" "+str(columns.index(user_option[0]))+"]"
        
        #this variable store YES/1 (if the user hit the target) or NO/0 (if the user missed the target).
        did_hit = 0

        # as mentioned before, here is where I look if the user input value is IN the answer vector (map_fleet_ones).
        for element in map_fleet_ones:
            if str(element) == user_option_converted:
                print("Hit !!!! ")
                matrix[int(user_option_converted[1])][int(user_option_converted[4])] = "X"
                
                print("You have {0} missiles remaining".format(missiles_remaining))
                
                print_board(matrix, columns)
                
                did_hit = 1
                total_hit +=1
                map_fleet_ones.remove(element) #when the user hit the point, I remove that point from the vector
            
           
        #if the user input is not in the vector (map_fleet_ones) then his/her input missed the target        
        if did_hit == 0:
            print("Miss ")
            matrix[int(user_option_converted[1])][int(user_option_converted[4])] = "O"
            
            print("You have {0} missiles remaining".format(missiles_remaining))
            print_board(matrix, columns)
           

    
    #checking if the user won (or not)
    if total_hit == total_one:
        print("YOU SANK MY ENTIRE FLEET !")
        print("You had {0} of {1} hits, wich sank all the ships ".format(numberOfHits, numberOfOnes))
        print("You won, congratulations!")
    else:
        print("GAME OVER")
        print("You had {0} of {1} hits, but didn't sink all the ships ".format(numberOfHits, numberOfOnes))
        print("Better luck next time")
    
    
    
    print(map_fleet_ones)
    #print(user_option_converted)



def print_board(matrix, columns):
    r = 1
    print(" ",end= " ")
    for letter in columns:
        print(letter, end= " ")
    print("\n")
    for row in matrix:
        print(str(r)+' '+' '.join([str(elem) for elem in row]))
        r += 1



#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()
