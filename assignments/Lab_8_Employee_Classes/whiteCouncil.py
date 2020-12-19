"""
    Project Name: IT121_Python
    Sub-project: Labs
    File Name: whiteCouncil.py
    Author: Dustin McClure
    Lab: Lab 8 - Employee Class
    Modified Date: 12/16/2020

    Python Class Inheritance
"""
from employee import Employee
from manager import Manager

# Derived from manager and inherits the class attributes of employee as well
class WhiteCouncil(Manager):

    def __init__(self, name, salary, department, knowledge, weapon, company_vehicle, attire, mission):
        self.knowledge = knowledge
        self.weapon = weapon
        self.company_vehicle = company_vehicle
        self.attire = attire
        self.mission = mission
        Manager.__init__(self, name, salary, department)

    def displayCouncilMember(self):
        print("\n\t%s:\n\tPosition: %s\n\tPrimary Weapons: %s\n\tTransportation: %s\n\tKnowledge: %s\n\tUniform: %s\n\tMission: %s\n" %(self.name, self.department, self.weapon, self.company_vehicle, self.knowledge, self.attire, self.mission))

    def dieAndRespawn(self, name, department, theWhite, knowledge, wiser, company_vehicle, comp_vehicle, attire, gucci_suit, mission):
        print("\nName: %s\n\t\t" %(self.name))
        print("Promotion from: %s\n\t" %(self.department))
        self.__setattr__(department, theWhite)
        print("To:--> %s\n" %(theWhite))
        print("Old Knowledge Level:--> %s\n\t" %(self.knowledge))
        self.__setattr__(knowledge, wiser)
        print("New Knowledge Level:--> %s\n" %(wiser))
        print("Regular Whip: %s\n\t" %(self.company_vehicle))
        self.__setattr__(comp_vehicle, comp_vehicle)
        print("Temp on Loan:--> %s\n" %(comp_vehicle))
        print("Previous Style: %s\n\t" %(self.attire))
        self.__setattr__(attire, gucci_suit)
        print("New Style:--> %s\n\t" %(gucci_suit))
        print("Mission: %s" %(self.mission))
