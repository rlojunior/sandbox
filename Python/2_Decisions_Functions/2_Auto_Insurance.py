###########################################
# Desc: Program 3 – Auto Insurance 
#
# Author: Reynaldo Junior
###########################################

#A program that computes monthly insurance 




def main():
    
    

    # Input
    gender = input("Are you 'Male' or 'Female': ").upper()
    age = int(input("Enter your age: "))
    vehicle_price = int(input("Enter the purchase price of the vehicle: "))

    # Process
    
    #Call the function gender_age_evaluation() to `decide` which tax will be applied
    insurance_tax= gender_age_evaluation(gender,age)
   
    #Calculate the total ($) of the monthly insurance  
    insurance_total = insurance_tax*vehicle_price


    # Output
    print("Your monthly insurance will be ${0:.2f}".format(insurance_total))


#Function to calculate the insurance tax based in the gender and the age of the customer
def gender_age_evaluation(gender,age):

    male_over_15 = 0.25
    male_over_25 = 0.17
    male_over_40 = 0.10

    female_over_15 = 0.20
    female_over_25 = 0.15
    female_over_40 = 0.10

    
    if age >=15 and age <25:
        if gender == "MALE":
            multiplier = male_over_15
        else:
            multiplier = female_over_15

    elif age >=25 and age <40:
        if gender == "MALE":
            multiplier = male_over_25
        else:
            multiplier = female_over_25
    elif age >=40 and age <70:
        if gender == "MALE":
            multiplier = male_over_40
        else:
            multiplier = female_over_40
   
    monthly_multiplier = multiplier/12
    return monthly_multiplier







#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()