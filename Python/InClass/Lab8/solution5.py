###########################################
# Desc: Solution 5.
#
# Author: Reynaldo Junior.
###########################################

def main():
   
    # Input
    numbers = [6,5,3]
    # Process
    
    max_numbers_list = ChangeToMax(numbers)
     

    

    # Output
    print(max_numbers_list)

def ChangeToMax(list):
    max_list = max(list)
    new_list = [max_list,max_list,max_list]  
    return new_list 

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()
    