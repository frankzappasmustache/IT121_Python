"""
    Project Name: IT121_Python
    Sub-project: Labs
    File Name: employee.py
    Author: Dustin McClure
    Lab: Lab 8 - Employee Class
    Modified Date: 12/16/2020

    Python Class Inheritance
"""
#Common base class for all employees
class Employee():
    # Common base class for all employees
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        self.empNum = Employee.empCount

    def displayCount(self):
        print("%s is employee %d of %d" %
              (self.name, self.empNum, Employee.empCount))

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)
