import sys
import re

from PySide.QtGui import *
from BasicUI import *


class Consumer(QMainWindow, Ui_MainWindow):

    states = ["AK", "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
              "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
              "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]



    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)

        self.clearButton.clicked.connect(lambda : self.clear_values())
        self.saveToTargetButton.clicked.connect(lambda : self.save_values())
        self.loadButton.clicked.connect(lambda : self.loadData())
        self.textlist = [self.firstNameLineEdit,self.lastNameLineEdit,self.addressLineEdit,self.cityLineEdit,self.stateLineEdit,self.zipLineEdit,self.emailLineEdit]
        self.user_init_flag = 0

        for value in self.textlist:
            value.textChanged.connect(lambda: self.text_changed_values())


    def clear_values(self):
        for values in self.textlist:
            values.setText("")

        self.loadButton.setEnabled(True)
        self.saveToTargetButton.setDisabled(True)

    def save_values(self):

        self.valid = 0
        temp = 1
        pattern = re.compile(r"\d{5}")
        value_match = re.match(pattern, self.zipLineEdit.text())
        pattern_email = re.compile(r"([\w.-]+@[\w.-]+)")
        email_match = re.match(pattern_email, self.emailLineEdit.text())

        for values in self.textlist:
            if values.text() == "":
                temp = 0

        if temp == 0:
            self.errorInfoLabel.setText("Error: ALL ENTRIES NOT POPULATED!")

        elif self.stateLineEdit.text() not in self.states:
            self.errorInfoLabel.setText("Error: State is not Valid!")


        elif value_match is None:
            self.errorInfoLabel.setText("Error: Zip is not valid!")

        elif email_match is None:
            self.errorInfoLabel.setText("Error: Email is not valid!")

        else:
            self.errorInfoLabel.setText("")
            self.valid = 1

        if(self.valid == 1):
            output = open("target.xml","w+")
            string = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<user>\n\t<FirstName>{0}</FirstName>\n\t<LastName>{1}</LastName>\n\t<Address>{2}</Address>\n\t<City>{3}</City>\n\t<State>{4}</State>\n\t<ZIP>{5}</ZIP>\n\t<Email>{6}</Email>".format(self.firstNameLineEdit.text(),self.lastNameLineEdit.text(),self.addressLineEdit.text(),self.cityLineEdit.text(),self.stateLineEdit.text(),self.zipLineEdit.text(),self.emailLineEdit.text())
            string += "\n</user>\n"
            print(string)

            output.write(string)








    def text_changed_values(self):
        self.saveToTargetButton.setEnabled(1)
        self.loadButton.setDisabled(1)





    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.

        *** This method is required for unit tests! ***
        """
        counter = 0
        with open(filePath, "r") as input:
            input_val= input.readlines()
            for line in input_val[2:-1]:
                value_temp = line.split(">")
                value_final = value_temp[1].split("<")
                self.textlist[counter].setText(value_final[0])
                counter = counter + 1




    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
