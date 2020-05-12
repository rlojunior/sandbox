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

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap

#import generated UI file here
import Ui_MainWindowCountries
import csv

class MyForm(QMainWindow, Ui_MainWindowCountries.Ui_MainWindow):
    # declare a list variable that will hold all
    # of the country data loaded from file into memory
    country = []

    unsaved_changes = False

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

        # slot for when the button is clicked
        self.buttonUpdatePopulation.clicked.connect(self.update_population)

        # slot for when the Save to File command in the menu is clicked
        #self.actionSave_to_File.triggered.connect(self.save_action_clicked)
        self.actionSavetoFile.triggered.connect(self.save_action_clicked)

        # slot for when the Exit command in the menu is clicked
        self.actionExit.triggered.connect(self.exit_program)

        # slot for when the radio button is clicked
        self.radioSqMile.clicked.connect(self.radiobuttons)
        self.radioSqKm.clicked.connect(self.radiobuttons)

        # slot for when the combo button is clicked
        self.comboBoxAreaConversion.currentIndexChanged.connect(self.combobox)
        


    # ADD SLOT FUNCTIONS HERE
    def radio_sqmile_clicked(self, enabled,selected_index):
        if enabled:
            country_population = int(self.country[selected_index][1])
            country_area_mile= int(self.country[selected_index][2])
            country_density_mile = float(country_population/country_area_mile)
            self.labelDensityValue.setText(format(country_density_mile,">7,.2f"))
            
    def radio_sqkm_clicked(self, enabled,selected_index):
        if enabled:
            country_population = int(self.country[selected_index][1])
            country_area_km= int(self.country[selected_index][2])*2.59
            country_density_km = float(country_population/country_area_km)
            self.labelDensityValue.setText(format(country_density_km,">7,.2f"))



    def load_countries(self):
        # This function: 
        # 1)calls the helper function to open the txt file 
        # 2)calls the helper function to load the file on the screen      
        self.load_country_from_file()
        self.populate_list_with_country()
        self.actionSavetoFile.setEnabled(True)

    def exit_program(self):
        QApplication.closeAllWindows()

    def save_action_clicked(self):
        # call the save_changes_to_file helper function which does the heavy lifting
        self.save_changes_to_file()
        # popup a message to the user confirming that the changes were saved to the file
        QMessageBox.information(self, 'Saved', 'Changes were saved to the file', QMessageBox.Ok)
        # toggle the unsaved_changes variable back to False because we no longer have any unsaved changes
        self.unsaved_changes = False
    
    def save_changes_to_file(self):
        # open the file for writing (w). Make sure it is the same location as the file you opened.
        with open("countries.txt", "w") as myFile:
            #loop through each list within the in-memory people list
            for country in self.country: #<- refer to each list as person
                # join each value in the person list and write them with a line break
                myFile.write(",".join(country) + "\n")


    
    def update_population(self):
        # determine the index of the currently selected person in the list
        #selected_index = self.listPeople.currentRow()
        selected_index = self.listCountries.currentRow()
        
        

        try:
            self.country[selected_index][1] = int(self.linePopulationInfo.text())
            # reload the list in case the name was changed...we want the change to be reflected in the UI list
            
            # popup a message to the user to let them know that the data was updated
            QMessageBox.information(self,
                                'Updated',
                                'Data has been updated in memory, but hasn''t been updated in the file yet',
                                QMessageBox.Ok)
            # toggle the unsaved_changes variable to True so that the program
            # prompts you to save to file when shutting down.
            self.unsaved_changes = True
            
        except:
            QMessageBox.information(self,
                                'Error',
                                'Type a valid number',
                                QMessageBox.Ok)
       
        

        
        


    def country_selected_from_list(self, selected_index):
        # When the user selects a country from the list, the functions below are triggered.
        
        self.display_country_data(selected_index)  #This function changes the text of the label to show the name of the country
        self.flag_image_display(selected_index)  #This fucntion shows the flag of the selected country 
        self.show_objects_hidden() #This function shows the objects that was hide in the begining of the program.
        # self.radio_sqkm_clicked(self,selected_index)
        # self.radio_sqmile_clicked(self,selected_index)


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
            total = 0
            for row in fileData:
                # add each list to the people list variable declared above
                self.country.append(row)
                total = total + float(row[2])
        print(total)
       
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
        #This function changes the text of the label to show the name, the population, the density population and the area of the country.

        country_name = self.country[selected_index][0]
        country_population = int(self.country[selected_index][1])
        country_area_mile= int(self.country[selected_index][2])
        # country_density_mile = float(country_population/country_area_mile)

        self.radiobuttons()
        self.combobox()

        self.labelCountryName.setText(country_name)
        self.linePopulationInfo.setText(format(country_population,">7,d"))
        

        world_population_total = 0
        for i in range(len(self.country)): 
            world_population_total += int(self.country[i][1])
        percentage = (int(country_population)*100)/world_population_total
        self.labelWorldPop.setText("{0:.4f}%".format(percentage))

    def closeEvent(self, event):

        if self.unsaved_changes == True:

            msg = "Save changes to file before closing?"
            reply = QMessageBox.question(self, 'Save?',
                     msg, QMessageBox.Yes, QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.save_changes_to_file()
                event.accept()


    def radiobuttons(self):

        selected_index = self.listCountries.currentRow()

        if self.radioSqKm.isChecked()== True:
            self.radio_sqkm_clicked(self, selected_index)
        if self.radioSqMile.isChecked()== True:
            self.radio_sqmile_clicked(self, selected_index)

    def combobox(self):

        selected_index = self.listCountries.currentRow()
        

        #When square mile is choosen
        if self.comboBoxAreaConversion.currentIndex() == 0:         
            country_area_mile= int(self.country[selected_index][2])
            self.labelAreaValue.setText(format(country_area_mile,">7,d"))
        
        #When square kilometer is choosen
        if self.comboBoxAreaConversion.currentIndex() == 1:
            country_area_km = int((int(self.country[selected_index][2]))*2.59)
            self.labelAreaValue.setText(format(country_area_km,">7,d"))

        
#DO NOT MODIFY THIS CODE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
#END DO NOT MODIFY


