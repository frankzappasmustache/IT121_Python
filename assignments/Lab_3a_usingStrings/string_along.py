"""
    Project Name: IT121_Python
    Sub-project: Labs
    File Name: stringAlong.py
    Author: Dustin McClure
    Lab: Lab 3a - Using Strings
    Modified Date: 10/06/2020

    {Description of program here}
"""
# Import the class 'Fuck' from the library foaas
from foaas import Fuck

fuck = Fuck()

lab_three = 3
fuck_amount = 4
print('''Today, for lab %d, we will be exploring precisely %.1f
of the many satisfying ways one can use %s to
tell someone to %s off.
''' % (lab_three, fuck_amount, 'fuck','fuck'))

asshole = fuck.asshole(from_='Dustin').text
asshole_one = asshole[0:18]
asshole_two = asshole[19:28]
total_asshole = '''\
{x}

Sincerely,

{y}\
 '''.format(x=asshole_one, y=asshole_two)

print(total_asshole + '\n')

fuck_goto_shaming = fuck.off_with(behavior="that strict programming dogma.", from_="Dustin").text

print(fuck_goto_shaming + '\n')

bigfuckinghammer = fuck.caniuse(tool="the \'BFH\' (big fucking hammer)", from_="Dustin")

print(bigfuckinghammer.text, end="")
print(" (keeper of the BFH)" + '\n')

recursion_fuck = fuck.particular(thing="recursion loop" * 5, from_="Dustin").text

fuck_this = recursion_fuck[0:9]
recursion_one = recursion_fuck[9:24]
recursion_two = recursion_fuck[24:38]
recursion_three = recursion_fuck[38:52]
recursion_four = recursion_fuck[52:66]
recursion_five = recursion_fuck[66:80]
in_particular = recursion_fuck[80:94]
my_name = recursion_fuck[95:109]

fuckery = '''\
      {a}
      {b}
         {c}
            {d}
               {e}
                  {f}
                     {g}
                      {h}\
                    '''.format(a=fuck_this, b=recursion_one, c=recursion_two, d=recursion_three, e=recursion_four, f=recursion_five, g=in_particular, h=my_name)

print(fuckery)
