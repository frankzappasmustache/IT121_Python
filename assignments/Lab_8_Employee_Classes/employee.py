import subprocess

class Employee:
    def __init__(self, name, salary, number, rank):
        self.name = name
        self.salary = salary
        self.number = number
        self.rank = rank


class FirstOrder(Employee):
    def __init__(self, side, name, salary, number, rank):
        self.side = side
        Employee.__init__(self, side)

    def displayFirstOrder(self):
        self.displayEmployee()
        print("%s is on the side of the %s." % (self.name, self.side))

    def adjustSalary(self, employee, amount, reason):
        employee.salary += amount
        print("%s\'s new salary is %s." % (employee.name, employee.salary))
        print("Reason for adjustment: %s" % reason)


class Resistance(Employee):
    def __init__(self, side, name, salary, number, rank):
        self.side = side
        Employee.__init__(self, side)

    def displayResistance(self):
        self.displayEmployee()
        print("%s is on the side of the %s." % (self.name, self.side))

    def adjustSalary(self, employee, amount, reason):
        employee.salary += amount
        print("%s\'s new salary is %s." % (employee.name, employee.salary))
        print("Reason for adjustment: %s" % reason)


class Jedi(Employee):
    def __init__(self, side, force, name, salary, number, rank):
        self.force = force
        self.side = side
        Employee.__init__(self, side, force)

    def displayJedi(self):
        self.displayJedi()
        print("%s is on the side of the %s." % (self.name, self.side))

    def mayTheForceBeWithYou(self, reason, useForce=subprocess.:
        print("%s has used the force to erase %s from existence." %
              (self.name, employee.name))
        print("%s has been cast into the belly of the %s ." %
              (employee.name, useForce))
        print(''' "%s" ''' % (reason))
