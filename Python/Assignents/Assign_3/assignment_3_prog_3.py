###########################################
# Desc: Assignment 3 - Prog 3.
#
# Author: Reynaldo Junior.
###########################################

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