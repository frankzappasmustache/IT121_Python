"""
    Project Name: IT121_Python
    Sub-project: Midterm
    File Name: midterm.py
    Author: Dustin McClure
    Modified Date: 11/08/2020

    IT121 Midterm
"""

# create dictionary with k,v pairs representing classes/hours
classHrs = {"class1": 0, "class2": 0, "class3": 0}

# request input in the form of an integer for how many hours a day the
# student should be studying, store that integer in the associated
# hrs* variable, update each dictionary key classHrs["key"] with the
# new value stored in the variable from user input
hrsOne = int(input('''
    How many hours should you spend in a week on your first class?
    '''))

classHrs["class1"] = hrsOne

hrsTwo = int(input('''
    How many hours should you spend in a week on your second class?
    '''))

classHrs["class2"] = hrsTwo

hrsThree = int(input('''
    How many hours should you spend in a week on your third class?
    '''))

classHrs["class3"] = hrsThree

# request input in the form of an integer for how many days they can study
# per week, and store this in daysOfStudy
daysOfStudy = int(input('''
    Realistically, how many days per week do you feel you can study for
    your classes?
    '''))

# request input in the form of an integer for how many hours they actually
# study each day, and store this in currentHours
currentHours = int(input('''
    Currently, how many hours do you study each day?
    '''))

# take the hours stored in the classHrs dictionary, add them together to get
# total number of hours the student should be studying per week, and divide
# this by the number of days they can study per week to get the hours they
# should actually be studying each day stored in idealStudyHours
idealStudyHours = (classHrs["class1"] + classHrs["class2"] + classHrs["class3"]) / daysOfStudy

# print the average number of hours they should study each day to a scale of 1
# decimal, using substitution to sub the idealStudyHours variable
# into the string
print("You should spend, on average, %.1f hours studying each day" %
    idealStudyHours)

# use if elseif loop to print different  messages if they are studying over
# or under the ideal number of hours each day, and tell them how much over
# they are studying, or how much more they need to study
if currentHours > idealStudyHours:
    excessive = currentHours - idealStudyHours
    print('''
        Great job! It looks like you are putting in an extra %.1f hours of
        studying each day. Maybe look at your work/life balance?
        ''' % excessive)
elif currentHours < idealStudyHours:
    extraStudy = idealStudyHours - currentHours
    print("You should probably study about %.1f hours more each day" % extraStudy)
