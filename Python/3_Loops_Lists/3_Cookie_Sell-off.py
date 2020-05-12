###########################################
# Desc: Assignment 3 - Prog 3.
#
# Author: Reynaldo Junior.
###########################################

""" The organizers of the annual Girl Guide cookie sale event want to raise the stakes on the number of cookies sold and are offering cool prizes to those guides who go above and beyond in their sales efforts. The organizers want a program to print the guide list and their prizes.

Your solution should demonstrate an understanding of how to apply list/loop concepts in a program that should:
•	Ask the user how many guides sold cookies in the current event,
•	For each numbered guide up to the user-entered count of guides, allow the user to enter a name and the number of boxes of cookies that person sold. 
•	Calculate and output a list of all guide names, 
•	Display the average sales, and the prize that each guide won,
•	The highest selling guide gets a trip to the Girl Guide Jamboree, any guides selling above average get a badge, and any guides selling at least one box get to split the remaining cookies, with guides selling no boxes shut out of all prizes (as they should be).
 """



def main():

    guides = []
    boxes_sold=[]
    
    
    number_of_guides = int(input("Enter the number of guides selling cookies: "))

    for sellers in range(0,number_of_guides):
        guides.append(input("Enter the name of guide #{0}: ".format(sellers+1)))
        boxes_sold.append(int(input("Enter the number of boxes sold by {0}: ".format(guides[sellers]))))
        print()
    
    average_box = sum(boxes_sold)/len(boxes_sold)
    print("The average number of boxes sold by each guide was {0:.1f}".format(average_box))
    print()
        
    
    prize = message_prize(boxes_sold)

    print_prize(guides,prize)
    
    
def message_prize(vector):
    message = []
    for item in vector:
        if item == max(vector):
            message.append("- Trip to Girl Guide Jamboree in Aruba !")
        elif item > (sum(vector)/len(vector)):
            message.append("- Top Seller Badge")
        elif item >= 1:
            message.append("- Left over cookies")
        else:
            message.append("- ")
    return message

def print_prize(names, prize_text):
    print("Guide"+"\t\t" + "Prize Won")
    print("-"*60)
    for persons in names:
        print("{0} \t \t {1}".format(names[names.index(persons)],prize_text[names.index(persons)]))



#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()