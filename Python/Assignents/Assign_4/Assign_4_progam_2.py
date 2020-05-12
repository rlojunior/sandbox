###########################################
# Desc: Assignment 4 - Prog 2.
#
# Author: Reynaldo Junior.
###########################################


def main():
    
    filename_options = "the_choices_file.csv"
    my_options= open(filename_options,"r")
    
    
        
    lines = my_options.readlines()
    max_lines = len(lines)

    option_letter = ['a','b','c','d','e'] 
    option_word = [1,2,3,4,5]

    
    user_choice = []
    user_choice_num = []
    word_choice = []

    line_count = 0

    for option in range(max_lines):
        
        word = word_position("the_choices_file.csv",option,0)
        print("Please choose {0}:".format(word))
        n = 1
        for letter in option_letter:
            
            noums = word_position("the_choices_file.csv",option,n)
            print("{0}) {1}".format(letter,noums))   
            n +=1
        
        
        
        
        while True:
            
            k = input("Enter choice (a-e): ")
            if k in option_letter:
                user_choice.append(k)
                user_choice_num.append(option_letter.index(k)+1) 
                word_choice.append(word_position("the_choices_file.csv",line_count,option_letter.index(k)+1))
                line_count +=1
                break
        

    filename_story = "the_story_file.txt"
    mystory= open(filename_story,"r")

    filename_new_story = "the_new_story_file.txt"
    myNewstory= open(filename_new_story,"w")    


            
       
    with mystory as story:
        for line in story:
            for word in line:
                for i in range(0,7):
                    if word == str(i+1):
                        word = word_choice[i].upper()
                    if word == "_":
                        word = ""
                    if i == 8:
                        break

                
                myNewstory.write(word)

    
   

def word_position(file, line_num,word_num):
    # this function works like a xy plane. We choose the word position (x),
    # we choose the line position (y) and the function returns the word (string)
    # file - The name of the "open" file
    # line_num - The number of the text line (act as a y in a plane xy)
    #            The line number starts in 0  
    # word_num -The number of the word (act as a x in a plane xy)
    #           The word number starts in 0 
    
    
    my_file= open(file,"r")
    
    commas_place = []
    lines = my_file.readlines()
    
    max_letters = len(lines[line_num])

    for i in range(max_letters):
        if lines[line_num][i] == "," or i == max_letters -1:
            commas_place.append(i)

    if word_num == 0:
        y = 0
    else:
        y =  commas_place[word_num-1]+1
    
    my_file.close()
    return lines[line_num][y:commas_place[word_num]]


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()