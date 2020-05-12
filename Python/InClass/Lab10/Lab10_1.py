###########################################
# Desc: Create a .csv file.
#
# Author: Reynaldo Junior.
###########################################

def main():
    filename = "GuestList.csv"
    accessMode = "w"
    myfile = open(filename,accessMode)

    write_data(myfile,"Doyle McCarty, 27")
    write_data(myfile,"Jodi Mills, 25")
    write_data(myfile,"Nicholas Rose, 32")
    write_data(myfile,"Zian Goddard, 36")
    write_data(myfile,"Zuha Hannania, 26")

    myfile.close()


def write_data(file,data):
    file.write(data)
    file.write("\n")

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()