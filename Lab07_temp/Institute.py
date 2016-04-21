import math
import copy
import sys

class Simulation:

    def __init__(self, simNo, simDate, chipName, chipCount, chipCost):
        self.simulationNumber = simNo
        self.simulationDate = simDate
        self.chipName = chipName
        self.chipCount= chipCount
        self.chipCost = chipCost
        self.simulationCost = round(chipCount * chipCost, 2)

    def __str__(self):
        return "{0}: {1:03d}, {2}, ${3:06.2f}".format(self.chipName, self.simulationNumber, self.simulationDate,self.simulationCost)

class Employee:
    def __init__(self, employeeName, employeeID):
        self.employeeID = employeeID
        self.employeeName = employeeName
        self.simulationsDict = {}

    def addSimulation(self, sim):
        key = "simulationNumber"

        self.simulationsDict[sim.simulationNumber] = sim

    def getSimulation(self, simNo):
        if simNo in self.simulationsDict.keys():
            return self.simulationsDict[simNo]
        else:
            return None

    def __str__(self):
        return "{0}, {1}: {2:02d} Simulations".format(self.employeeID, self.employeeName, len(self.simulationsDict.keys()))

    def getWorkload(self):
        string = ""
        list_vals = []
        for key in self.simulationsDict:
            list_vals.append(str(self.simulationsDict[key]))

        list_vals.sort()

        for value in list_vals:
            string += value
            string += "\n"

        string = string[0:-1]

        ns= "{0}, {1}: {2:02d} Simulations\n".format(self.employeeID, self.employeeName, len(self.simulationsDict.keys()))
        ns += string
        return ns

    def addWorkload(self, fileName):
        with open(fileName) as input:
            data = input.readlines()
            for line in data[2:]:
                values = line.split()
                print (values)
                values[0] = int(values[0].strip())
                values[1] = values[1].strip()
                values[2] = values[2].strip()
                #print(values[3].strip())
                values[3] = values[3].strip()
                val = values[4].split("$")
                print(val)
                #print(values[4])
                print(val[1])
                float_val = float(val[1].strip())
                simObject = Simulation(values[0],values[1],values[2],int(values[3]),float_val)
                print(str(simObject))
                self.addSimulation(simObject)

class Facility:
    def __init__(self, facilityName):
        self.facilityName = facilityName
        self.employeesDict = {}


    def addEmployee(self,employee):
        self.employeesDict[employee.employeeName] = employee

    def getEmployees(self, *args):
        list_val = []
        for i in args:
            list_val.append(self.employeesDict[i])

        return list_val

    def __str__(self):
        string = "{0}: {1:02d} Employees\n".format(self.facilityName,len(self.employeesDict.keys()))
        list_val = []
        for i in self.employeesDict:
            str_val = str(self.employeesDict[i])
            list_val.append(str_val)

        list_val.sort()
        string_append =""
        for value in list_val:
            string_append += value
            string_append += "\n"

        string_append = string_append[0:-1]

        string += string_append

        return string

    def getSimulation(self,simNo):
        for i in self.employeesDict:
            for j in self.employeesDict[i].simulationsDict:
                if j == simNo:
                    return self.employeesDict[i].simulationsDict[j]

        return None














