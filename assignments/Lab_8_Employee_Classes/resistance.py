class Resistance(Employee):
    def __init__(self, side, name, salary, number, rank):
        self.side = side
        Employee.__init__(self, name, salary, number, rank)

    def displayResistance(self):
        self.displayEmployee()
        print("%s is on the side of the %s." % (self.name, self.side))

    def adjustSalary(self, employee, amount, reason):
        employee.salary += amount
        print ("%s\'s new salary is %s." % (employee.name,employee.salary))
        print ("Reason for adjustment: %s" % reason)
