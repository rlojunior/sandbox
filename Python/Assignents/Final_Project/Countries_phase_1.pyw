#####################################################
#      
# 
#         Assignment 5 (a.k.a Final Project)           
#   GRAPHICAL USER INTERFACE (GUI) PROGRAMMING       
#            Author: Reynaldo Junior
#
#
####################################################
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap

#import generated UI file here
import Ui_MainWindowCountries
import csv

class MyForm(QMainWindow, Ui_MainWindowCountries.Ui_MainWindow):
    # declare a list variable that will hold all
    # of the country data loaded from file into memory
    country = []

    

        # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
        # END DO NOT MODIFY

        # Hide (i. e. not show) some objects after the program is open.
        # These objects must apear just when the user selects his/her first country from the list.
        self.label.hide()
        self.linePopulationInfo.hide()
        self.buttonUpdatePopulation.hide()
        self.label_2.hide()
        self.comboBoxAreaConversion.hide()
        self.labelAreaValue.hide()
        self.groupBox.hide()
        self.radioSqMile.hide()
        self.radioSqKm.hide()
        self.labelDensityValue.hide()
        self.label_4.hide()
        self.labelWorldPop.hide()
        

        # ADD SLOTS HERE
        # slot for when the user select file > Load Countries
        self.actionLoadCountries.triggered.connect(self.load_countries)

        # slot for when an item is selected in the list
        self.listCountries.currentRowChanged.connect(self.country_selected_from_list)


    # ADD SLOT FUNCTIONS HERE
    def load_countries(self):
        # This function: 
        # 1)calls the helper function to open the txt file 
        # 2)calls the helper function to load the file on the screen      
        self.load_country_from_file()
        self.populate_list_with_country()


    def country_selected_from_list(self, selected_index):
        # When the user selects a country from the list, the functions below are triggered.
        
        self.display_country_data(selected_index)  #This function changes the text of the label to show the name of the country
        self.flag_image_display(selected_index)  #This fucntion shows the flag of the selected country 
        self.show_objects_hidden() #This function shows the objects that was hide in the begining of the program.


    # ADD ALL OTHER HELPER FUNCTIONS HERE
    def load_country_from_file(self):
        #This function: 
        # 1) opens the countries.txt (the csv file where the infos of the Country are)
        # 2) loads each row of that file to an array called country

        self.country.clear()

        # open countries.txt file with csv reader and read data into country list.
        with open("countries.txt", "r") as myFile:        

            # load data into reader object
            fileData = csv.reader(myFile)
            # loop through each line in reader...each line is a list of values
            for row in fileData:
                # add each list to the people list variable declared above
                self.country.append(row)

       
    def populate_list_with_country(self):
        #This function puts the names of the Countries on a list and shows on the screen
        self.listCountries.clear()

        for element in self.country:   
            self.listCountries.addItem(element[0])

    def show_objects_hidden(self):
        #This function shows the objects that was hide in the begining of the program.

        self.label.show()
        self.linePopulationInfo.show()
        self.buttonUpdatePopulation.show()
        self.label_2.show()
        self.comboBoxAreaConversion.show()
        self.labelAreaValue.show()
        self.groupBox.show()
        self.radioSqMile.show()
        self.radioSqKm.show()
        self.labelDensityValue.show()
        self.label_4.show()
        self.labelWorldPop.show()
    
    def flag_image_display(self,selected_index):
        #This fucntion shows the flag of the selected country

        if self.country[selected_index][0] == "Cote d'Ivoire":
            image_name = self.country[selected_index][0].replace('o','ô',1)
            image_name = image_name.replace(' ','_')
        else:
            image_name = self.country[selected_index][0].replace(' ','_')
        

        image_path = "Flags\\"
        image_extension = ".png"
        image = QPixmap(image_path + image_name+image_extension)
        
        #set the label with the selected pixmap
        self.labelFlagImage.setPixmap(image)

    
    def display_country_data(self, selected_index):
        #This function changes the text of the label to show the name and the population of the country.

        country_name = self.country[selected_index][0]
        country_population = self.country[selected_index][1]

        self.labelCountryName.setText(country_name)

        if len(country_population) == 8:
            mask = "00,000,000"
        elif len(country_population) == 7:
            mask = "0,000,000"
        elif len(country_population) == 6:
            mask = "000,000"
        elif len(country_population) == 9:
            mask = "000,000,000"
        else:
            mask = "00,000"

                
        self.linePopulationInfo.setInputMask(mask)
        self.linePopulationInfo.setText(country_population)

#DO NOT MODIFY THIS CODE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
#END DO NOT MODIFY


