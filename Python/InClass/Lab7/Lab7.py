###########################################
# Desc: Creating functions.
#
# Author: Reynaldo Junior.
###########################################

def main():
    # Input
    a = float(input('Enter the first number: '))
    b = float(input('Enter the second number: '))
    # Process

    # Output

    print('The sum is: {0}'.format(adding(a,b)))
    print('The subtaction is: {0}'.format(subtracting(a,b)))
    print('The multiplication is: {0}'.format(multipling(a,b)))
    print('The division is: {0}'.format(dividing(a,b)))


def adding(valueA,ValueB):
    result = valueA+ValueB
    return result

def multipling(valueA,ValueB):
    result = valueA*ValueB
    return result

def subtracting(valueA,ValueB):
    result = valueA-ValueB
    return result

def dividing(valueA,ValueB):
    result = valueA/ValueB
    return result



#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()