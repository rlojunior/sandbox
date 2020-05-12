###########################################
# Desc: Solution 6.
#
# Author: Reynaldo Junior.
###########################################

def main():
   
    # Input
    numbers = [1,2,3]
    # Process
    
    RotateLeft(numbers)
    
     

    

    # Output
    print(numbers)

def RotateLeft(list):
    list.append(list[0])
    list.remove(list[0])
    
    

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()
    