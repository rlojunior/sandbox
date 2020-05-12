###########################################
# Desc: Solution 7.
#
# Author: Reynaldo Junior.
###########################################

def main():
   
    # Input
    numbers = [0,6]
    # Process
    

    check = Has2Or3(numbers)

        

    
     

    

    # Output
    print(check)

def Has2Or3(list):
    if list[0]==2 or list[1]==2 or list[0]==3 or list[1]==3 :
        has_2_or_3 = True
    else:
        has_2_or_3 = False
    return has_2_or_3
    
    

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()
    