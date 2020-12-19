"""
    Project Name: IT121_Python
    Sub-project: Labs
    File Name: manager.py
    Author: Dustin McClure
    Lab: Lab 8 - Employee Class
    Modified Date: 12/16/2020

    Python Class Inheritance
"""
from employee import Employee

# derived from Employee and inherets its attributes
class Manager(Employee):

    def __init__(self, name, salary, department):
        self.department = department
        Employee.__init__(self, name, salary)

    def getdept(self):
        return self.department

    def setdept(self, department):
        department = self.department

    def displayManager(self, name):
        self.displayEmployee()
        print("%s manages the %s department." % (self.name, self.department))

    def adjustSalary(self, employee, amount, reason):
        employee.salary += amount
        print("%s\'s new salary is %s." % (employee.name, employee.salary))
        print("Reason for adjustment: %s" % reason)
