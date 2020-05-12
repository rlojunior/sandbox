###########################################
# Desc: List puzzle - Solution 1.
#
# Author: Reynaldo Junior.
###########################################

def main():
    
    numbers1 = [1,3,7]
    numbers2 = [7, 8, 2, 4]
    numbers3 = [13, 7, 1, 5, 9]

    
    print("Is the list {0} True or False? {1}".format(numbers1,FirstOrLast7(numbers1)))
    print()
    print("Is the list {0} True or False? {1}".format(numbers2,FirstOrLast7(numbers2)))
    print()
    print("Is the list {0} True or False? {1}".format(numbers3,FirstOrLast7(numbers3)))

    


def FirstOrLast7(list):
    if(list[0]==7 or list[-1]==7):
        x = True
        
    else:
         x = False
    return x




#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()