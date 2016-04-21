import os
import sys
import re

class Simulation:
    def __init__(self, simnNo, simDate, chipName, chipCount, chipCost):
        self.simulationNumber = simnNo
        self.simulationDate = simDate
        self.chipName = chipName
        self.chipCount = chipCount
        self.chipCost = chipCost
        self.simulationCost = round(self.chipCost * self.chipCount, 2)

    def __str__(self):
        return "{0}: {1:03d}, {2}, ${3:06.2f}".format(self.chipName, self.simulationNumber, self.simulationDate, self.simulationCost)

class Employee:
    def __init__(self, employeeName, employeeID):
        self.simulationsDict = {}
        self.employeeName = employeeName
        self.employeeID = employeeID

    def addSimulation(self,sim):
        self.simulationsDict[sim.simulationNumber] = sim

    def getSimulation(self,simNo):
        if simNo not in self.simulationsDict.keys():
            return None
        else:
            return self.simulationsDict[simNo]

    def __str__(self):
        ret_string = "{0}, {1}: {2:02d} Simulations".format(self.employeeID, self.employeeName, len(self.simulationsDict))
        return ret_string

    def getWorkload(self):
        string1 = str(self)
        string1 += "\n"

        list_strings = []
        for key in self.simulationsDict.keys():
            temp_string = str(self.simulationsDict[key])
            list_strings.append(temp_string)

        list_strings.sort()

        for item in list_strings:
            string1 += item
            string1 += "\n"

        string1 = string1[0:-1]

        return string1

if __name__ == "__main__":
    pass