from employee import Employee
from jedi import Jedi
from firstOrder import FirstOrder
from resistance import Resistance

emp = Employee()
re = Resistance()
fo = FirstOrder()
jedeye = Jedi()

LoneStar = jedeye("Jedi", 100, "Lone Star", 500000, 1, "Grand Master")
Barf = re("Resistance", "Barf", 100000, 2, "Co-Pilot")
Yogurt = jedeye("Jedi", 100, "Yogurt", 1000000, 3, "Grand Master")
DarkHelmet = jedeye("First Order", 98, "Dark Helmet", 1000000, 4, "Sith")

LoneStar.displayJedi()
Barf.displayResistance()
Yogurt.displayJedi()
DarkHelmet.displayFirstOrder()

LoneStar.mayTheForceBeWithYou(DarkHelmet, "Because", useForce)
