###########################################
# Desc: Assignment 3 - Prog 1.
#
# Author: Reynaldo Junior.
###########################################

""" Design and write a program that accepts the number of hours worked on each of five work days from the user, then displays different information calculated about those entries as output. 
Your solution should demonstrate an understanding of how to apply list and looping concepts in a program that should:
•	Prompt the user to enter the five daily hours worked amounts, and store them in the program. 
•	Determine the day(s) on which the most hours were worked and display the day(s) and hours onscreen. 
•	Calculate and display both the total and the daily average of hours worked.
•	Display a list of all days that had insufficient hours, which is defined as less than 7 hours.
 """




def main():
    hours = []
    hours = hours_worked_input()
    
    print("-"*40)
    print("The most hours worked was on:")
    
    print("Day #{0} when you worked {1} hours".format(hours.index(max(hours))+1,max(hours)))
    
    print("-"*40)
    print("The total number of hours worked was: {}".format(sum(hours)))

    #To calculate the average -> sum the values of the list and divide by the number of elements of that list
    print("The total number of hours worked was: {}".format(sum(hours)/len(hours)))
    print("-"*40)

    
    print("Days you slacked off (i.e. worked less than 7 hours):")
    less_than_7_hours(hours)
    
# "hours_worked_input" is a function that asks the user how much he/she worked during the 5 days of the week.
# This fuction returns a vector (lenth 5 -> number of work days) with the values enterded by the user. 
# This function only accept a valid number as input. 
def hours_worked_input():
    days = ['day1', 'day2', 'day3', 'day4', 'day5']
    hours_worked = []
    check = True
    for day in days:
        while check:
            day_num = input("Enter hours worked on Day #{}: ".format(days.index(day)+1))
            is_a_num = day_num.isnumeric()
            if is_a_num == True:
                hours_worked.append(int(day_num))
                check = False
        check = True
    return hours_worked

# "less_than_7_hours" evaluate if there is/are day(s) where the user worked less than 7 hours.
# There is no "return value" for this function, it only does the "action" to show the days and hours worked (if is less than 7 hours).
def less_than_7_hours(number_of_hours):
    for item in number_of_hours:
        if item < 7:
            print("Day #{0}: {1} hours".format(number_of_hours.index(item)+1,item))


    

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()