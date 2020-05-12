###########################################
# Desc: Assignment 4 - Prog 1.
#
# Author: Reynaldo Junior.
###########################################

""" Program that reads the text from a provided text file into a list, displays the text on-screen, 
makes some alterations to the text and outputs the changed text to the screen, then saves the altered 
text as a new file. """ 


import random

def main():
    
    intro("Files\\ateam_Original.txt")
    
    filename = "Files\\ateam_Original.txt"
    my_file= open(filename,"r")
    
    filename_altered = "Files\\ateam_Altered.txt"
    my_filename_altered = open(filename_altered,"a")

    max = len(open(filename).readlines())
    rand = random.randrange(1,max)

    n = 1

    for line in my_file:
          
        line = more_than_x_characters(line,20)

        if n == rand:
            line = " "
            print(" ")
            my_filename_altered.write("\n")
        else:
            print("{0}: {1}".format(n,line.strip()))
            my_filename_altered.write("{0}: {1} \n".format(n,line.strip()))
       
        
        n +=1
    
    my_file.close()
    

def intro(old_file):
   
    my_file = open(old_file,"r")

    print("-"*40)
    print("Original Text")
    print("-"*40)
    
    print()
    print(my_file.read())
    my_file.close()
    print()

    print("-"*40)
    print("Altered Text")
    print("-"*40)

def more_than_x_characters(lines,x):
    if len(lines) > x:
        new_line = lines.lower()
    else:
        new_line = lines.upper()

    return new_line        





#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()