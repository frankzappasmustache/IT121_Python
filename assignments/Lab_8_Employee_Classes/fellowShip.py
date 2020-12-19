"""
    Project Name: IT121_Python
    Sub-project: Labs
    File Name: fellowShip.py
    Author: Dustin McClure
    Lab: Lab 8 - Employee Class
    Modified Date: 12/16/2020

    Python Class Inheritance
"""
import employee
from employee import Employee
import manager
from manager import Manager
import whiteCouncil
from whiteCouncil import WhiteCouncil

# create 3 new instances of employee
merry = employee.Employee("Merry", 5000)
sam = employee.Employee("Sam", 5000)
pippin = employee.Employee("Pippin", 5000)

#display the employee information
merry.displayEmployee()
sam.displayEmployee()
pippin.displayEmployee()


# create instance of manager
aragorn = manager.Manager("Aragorn II Elessar", 10000, "King of Gondor")

# adjust employee salary with manager class permissions
aragorn.adjustSalary(merry, +3000, "For protecting Mr. Frodo")

# create white council member
gandalfTheGrey = whiteCouncil.WhiteCouncil("Gandalf The Grey", 20000,
    "White Council & Order of Wizards", "great", "Narya and Glamdring", "ShadowFax",
    "Grey Robe", "Stop Sauron")

# display information on mamber
gandalfTheGrey.displayCouncilMember()

# die and respawn as Gandalf the White, leader of the White Council
gandalfTheGrey.dieAndRespawn(gandalfTheGrey, gandalfTheGrey.name, "Leader of White Council", gandalfTheGrey.knowledge, "Exceptionally Wise", gandalfTheGrey.company_vehicle, "Gwaihir, lord of eagles", gandalfTheGrey.attire, "White Robe", gandalfTheGrey.mission)
