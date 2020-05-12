###########################################
# Desc: Program 3 – Imperial to Metric Conversion
#
# Author: Reynado Junior
###########################################

"""
Pseudocode: first the program is going to ask the user to enter the 
tons value, then stone, after pounds and finally onces values.
After that the program is going to calculate (or convert) these
values to tons, kilos and grams

To calcule the result in tons, kilos and grams I did the following calculation.
I will work with number, as example:

tons: 5
stone: 20
pounds: 2
ounces: 4

Using the formula to calculate the total ounces: 35840 * tons + 224 * stone + 16 * pounds + ounces.
I will have 183716. Dividing this result by 35274 I obtain 5.20825537 (This is the total ounces converted to kilos).
Observe that it is possible to recognize the values given by the answer:
"The metric weight is 5 metric tons, 208 kilos, and 255.4 grams"

Now, I'm going to work splitting this number in parts: tons, kilos and grams.

If I get the integer of the number 5.20825537, I will have 5. This is the metric tons.

Now, I subtract 5 from 5.20825537. The result is 0.20825537.
Multiplying this result by 1000, I have 208.25537.
Again, the integer of this number will be the value in kilos.

Finally, if I subtract its integer (208) from 208.25537, the result is 0.25537.
Multiplying this number by 1000 I obtain 255.37.
If I display this result just with one decimal place, then the result is 255.4 

;-)

"""



def main():
    print("Imperial to Metric Conversion \n")
    
    # Input
    # Ask the user to input some values
    tons = int(input("Enter the number of tons: "))
    stone = int(input("Enter the number of stone: "))
    pounds = int(input("Enter the number of pounds: "))
    ounces = int(input("Enter the number of ounces: "))
    print("")
          
    
    # Process

    #Using the given formula to calculate the total ounces
    total_ounces = ((35840*tons)+(224*stone)+(16*pounds))+ounces

    #From total ounces I calculate the total in kilos
    total_kilos = total_ounces/35274

    #The integer number of the variable total_kilos will be the metric tons
    metric_tons = int(total_kilos)
    
    #Performing the calculations as showed in the pseudocode
    kilo_index =(total_kilos-metric_tons)*1000 
    kilos = int(kilo_index)

    #The remain result will be the value in grams
    grams = (kilo_index-kilos)*1000

    # Output
    print("The metric weight is {0} metric tons, {1} kilos, and {2:.1f} grams".format(metric_tons,kilos,grams))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()