###########################################
# Desc: Solution 4.
#
# Author: Reynaldo Junior.
###########################################

def main():
   
    # Input
    numbers = [2,2,3]
    # Process

    sum = SumList(numbers)
    

    # Output
    print(sum)

def SumList(list):
    add = list[0]+list[1]+list[2]
    return add

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()
    