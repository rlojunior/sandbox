###########################################
# Desc: Assignment 3 - Prog 2.
#
# Author: Reynaldo Junior.
###########################################

""" Design and write a program that removes all desired letters from any user-entered sentence or phrase.
Your solution should demonstrate an understanding of how to apply list and looping concepts in a program that should:
•	Take a sentence or phrase as input,
•	Take a comma-separated list of letters to remove as input,
•	Replace all occurrences of each target letter in the user-entered sentence, regardless of case sensitivity, with an underscore (“_”) character.
•	Display the number of letters removed to the user,
•	The program will keep asking the user to enter a new sentence until the user enters the command ‘quit’.
 """



def main():
    user_phrase = ""
    
    run_the_program = True

    # run the program infinitely until the user type "quit"
    while run_the_program:
        user_phrase = input("Type a phrase (or quit to exit program): ")
        if user_phrase.upper() == "QUIT":
            break
            
        user_letters_redact = input("Type a comma-separeted list of letters to redact: ")
        
        # call the function "replace_letter" and store the result in a string
        new_phrase = replace_letter(user_phrase,user_letters_redact)
          

       
        print("Number of letters redacted: {0}".format(new_phrase.count("_")))
        print("Redacted phrase: {0}".format(new_phrase))
        
# this function is the core of the program. Its goal is to return a new phrase based on the user inputs
def replace_letter(phrase,letters_redact):
    
    #the idea here is to "clean" the input and delete the commas
    letters_redact_new = letters_redact.replace(",","")
    
    #these variables and the for loop were created to make the program "non case sensitive"
    letters_redact_new_lower = letters_redact_new.lower()
    letters_redact_new_upper = letters_redact_new.upper()
    
    for letter in phrase:
            if letter in letters_redact_new_lower:
                phrase = phrase.replace(letter,"_")
            
            if letter in letters_redact_new_upper:
                phrase = phrase.replace(letter,"_")  
    return phrase
        

    

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()