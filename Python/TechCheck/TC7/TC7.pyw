import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


import Ui_MainWindowTC7



class MyForm(QMainWindow, Ui_MainWindowTC7.Ui_MainWindow):
    

        # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
        # END DO NOT MODIFY

        # ADD SLOTS HERE
        
        self.pushButtonCalculate.clicked.connect(self.update_screen)        

        

    # ADD SLOT FUNCTIONS HERE
        
    def update_screen(self):
        
        self.Salary = self.lineEditWeeklySalary.text()
        self.Dependent = self.lineEditDependentnum.text()
        self.labelDependentnum.setText(self.Dependent)
        
        self.ProvincialTax = 0.06*float(self.Salary)
        self.labelProvincialTax.setText("$"+str(self.ProvincialTax))

        self.FederalTax = (0.25*float(self.Salary))
        self.labelFederalTax.setText("$"+str(self.FederalTax))

        self.DependentTax = 0.02*int(self.Dependent)*float(self.Salary)
        self.labelDependentDeduction.setText("$"+str(self.DependentTax))

        self.TotalWithheld = (float(self.ProvincialTax) +  float(self.FederalTax))-float(self.DependentTax)
        self.labelTotalWtihheld.setText("$"+str(self.TotalWithheld))

        self.TotalTakeHome =  float(self.Salary) - float(self.TotalWithheld)
        self.labelTotalTakeHome.setText("$"+str(self.TotalTakeHome))


        
        


# DO NOT MODIFY THIS CODE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
# END DO NOT MODIFY