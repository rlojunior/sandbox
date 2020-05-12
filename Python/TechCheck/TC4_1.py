###########################################
# Desc: Tech Check #3.
#
# Author: Enter name here.
###########################################

def main():
      
    numeric_value = 0
    final_grade = 0
    
    grade_A = 4.0
    grade_B = 3.0
    grade_C = 2.0
    grade_D = 1.0
    grade_F = 0.0

    modifier_value = 0.3

    print("Grade Point Calculator")
    print()
    print("Valide letter grades that can be entered: A, B, C, D, F.")
    print("Valid grade modifier are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.") 
    print("Calculated grade point value cannot exceed 4.0.")
    print()

    # Input
    grade = input("Please enter a letter grade: ").upper()
    modifier = input("Please enter a modifier (+, - or nothing): ")
    
    
    # Process
    if grade == "A":
        numeric_value = grade_A
    elif grade == "B":
        numeric_value = grade_B
    elif grade == "C":
        numeric_value = grade_C
    elif grade == "D":
        numeric_value = grade_D
    else:
        print("You entered an invalid letter grade")

    if modifier == "+":
        final_grade = numeric_value + modifier_value
    elif modifier == "-":
        final_grade = numeric_value - modifier_value
    else:
        final_grade = numeric_value

    if final_grade > 4.0:
        final_grade = 4.0
    
    message = "The numeric value is: {0}".format(final_grade)

    # Output
    
    print(message)

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()