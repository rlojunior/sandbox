###########################################
# Desc: TC4.
#
# Author: Reynaldo Junior.
###########################################
letterGrade = 0
modifier = 0

def main():
    global letterGrade
    global modifier

    course_1 = "PROG1700"
    course_2 = "NETW1700"
    course_3 = "OSYS1200"
    course_4 = "WEBD1000"
    course_5 = "COMM1700"
    course_6 = "DBAS1007"
    
    # grade_course_1 = 0
    # grade_course_2 = 0
    # grade_course_3 = 0
    # grade_course_4 = 0
    # grade_course_5 = 0
    # grade_course_6 = 0


    start_program()
    
    # Input
    grade_course_1 = input("Please enter a letter grade for {0}: ".format(course_1)).upper()
    modifier = input("Please enter a modifier (+, - or nothing) : ")
    grade_course_1_final = evaluate_grade(grade_course_1,modifier)
    print()

    grade_course_2 = input("Please enter a letter grade for {0}: ".format(course_2)).upper()
    modifier = input("Please enter a modifier (+, - or nothing) : ")
    grade_course_2_final = evaluate_grade(grade_course_2,modifier)
    print()

    grade_course_3 = input("Please enter a letter grade for {0}: ".format(course_3)).upper()
    modifier = input("Please enter a modifier (+, - or nothing) : ")
    grade_course_3_final = evaluate_grade(grade_course_3,modifier)
    print()

    grade_course_4 = input("Please enter a letter grade for {0}: ".format(course_4)).upper()
    modifier = input("Please enter a modifier (+, - or nothing) : ")
    grade_course_4_final = evaluate_grade(grade_course_4,modifier)
    print()

    grade_course_5 = input("Please enter a letter grade for {0}: ".format(course_5)).upper()
    modifier = input("Please enter a modifier (+, - or nothing) : ")
    grade_course_5_final = evaluate_grade(grade_course_5,modifier)
    print()

    grade_course_6 = input("Please enter a letter grade for {0}: ".format(course_6)).upper()
    modifier = input("Please enter a modifier (+, - or nothing) : ")
    grade_course_6_final = evaluate_grade(grade_course_6,modifier)
    print()

    # print("*"*60)

    print("The numeric value for {0} is: {1}".format(course_1,grade_course_1_final))
    print("The numeric value for {0} is: {1}".format(course_2,grade_course_2_final))
    print("The numeric value for {0} is: {1}".format(course_3,grade_course_3_final))
    print("The numeric value for {0} is: {1}".format(course_4,grade_course_4_final))
    print("The numeric value for {0} is: {1}".format(course_5,grade_course_5_final))
    print("The numeric value for {0} is: {1}".format(course_6,grade_course_6_final))


    # Process

    sum_all_grades = grade_course_1_final + grade_course_2_final+grade_course_3_final+grade_course_4_final+grade_course_5_final+grade_course_6_final
    average_grade = sum_all_grades/6

    print("="*60)
    print("Your grade point average for the semester is: {0:.1f}".format(average_grade))
    print("="*60)


    # Output

def start_program():
    print("Grade Point Calculator\n")
    print("Valid letter grades that can be entered: A, B, C, D, F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0.\n")   

def evaluate_grade(letterGrade,modifier):
    
    numericGrade = 0

    if letterGrade == "A":
        numericGrade = 4.0
    elif letterGrade == "B":
        numericGrade = 3.0
    elif letterGrade == "C":
        numericGrade = 2.0
    elif letterGrade == "D":
        numericGrade = 1.0
    elif letterGrade == "F":
         numericGrade = 0.0
    else:
        print("You entered an invalid letter grade.")
        
    # Determine whether to apply a modifier
    if modifier == "+":
        if letterGrade != "A" and letterGrade != "F": # Plus is not valid on A or F
            numericGrade += 0.3
    elif modifier == "-":
        if letterGrade != "F":     # Minus is not valid on F
            numericGrade -= 0.3
   
    return numericGrade

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()