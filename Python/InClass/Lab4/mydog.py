###########################################
# Desc: This program is going to do lot os changes in user input
#
# Author: Reynaldo Junior
###########################################

def main():
    # Input
    user_phrase = "My dog has fleas"
    # Process
    
    # Output
    
    #Confirm the user phrase
    print("")
    print("Confirm the phrase: {0}".format(user_phrase))
    
    #all in uppercase
    print("")
    print("The phrase in uppercase is: "+ user_phrase.upper())

    #all in lowercase
    print("")
    print("The phrase in lowercase is: "+ user_phrase.lower())

    #counting how many o`s
    count_o = user_phrase.count("o")
    print("")
    print("There is/are {0} o`s in the user`s phrase".format(count_o))

    #if the phrase contains alpha-numeric characters
    print("")
    print("Is this phrase contains ONLY alpha-numeric characters? "+ str(user_phrase.isalpha())) 

    #changing lowercase s`s to lowercase z
    print("")
    print("Rewriting the phrase changing s`s to z`s: "+ user_phrase.replace("s","z"))
    print("")



#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()