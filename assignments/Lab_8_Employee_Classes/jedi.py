class Jedi(Employee):
    def __init__(self, side, force, name, salary, number, rank):
        self.force = force
        self.side = side
        Employee.__init__(self, side, force)

    def displayJedi(self):
        self.displayEmployee()
        print("%s is on the side of the %s." % (self.name, self.side))

    def mayTheForceBeWithYou(self, resistance, reason, useForce = employee.devnull()):
        print("%s has used the force to erase %s from existence." % (self.name, employee.name))
        print("%s has been cast into the belly of the %s ." %
              (employee.name, useForce))
        print(''' "%s" ''' % (reason))
