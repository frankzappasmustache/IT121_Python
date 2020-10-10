"""
    Project Name: IT121_Python
    Sub-project: Labs
    File Name: fuckstrings.py
    Author: Dustin McClure
    Lab: Lab 3a - Using Strings
    Modified Date: 10/10/2020

    A program that formats and prints responses from the
    foaas api (Fuck off as a Service); an api that allows
    you to very efficiently tell someone or something to
    'fuck off'.
"""
# import the Fuck class from the foaas module
from foaas import Fuck

# create a new instance of the class Fuck
fuck = Fuck()

# set variables for the current lab and number of fuck operations
lab_three = 3
fuck_amount = 4

# print a fucking explanation of what this program accomplishes
# using string modulo operators  %d (digit), %s (string), and
# %f (floating point) to embed values
print('''Today, for lab %da, we will be exploring precisely %.1f
of the many satisfying ways one can use %s off as a service to
simplify the action of telling someone to %s off. \n
''' % (lab_three, fuck_amount, 'fuck','fuck'))

print("=====================================================================\n")

# assign response value of fuck.asshole action to var asshole
asshole = fuck.asshole(from_='Dustin').text

# create string slices of string stored in asshole and assign
# them to variables that can more easily be formatted
asshole_one = asshole[0:18]
asshole_two = asshole[19:28]

# format our slice variables into a multiline string stored
# in its own variable
total_asshole = '''\
{x}

Sincerely,

{y}\
 '''.format(x=asshole_one, y=asshole_two)

# print our newly formatted multiline string and add an
# additional newline
print(total_asshole + '\n')
print("=====================================================================\n")
# assign response value of fuck.off_with action to var fuck_goto_shaming
fuck_goto_shaming = fuck.off_with(behavior="that strict programming dogma.", from_="Dustin").text

# print the string stored in var fuck_goto_shaming and add an
# additional newline
print(fuck_goto_shaming + '\n')
print("=====================================================================\n")
# assign response value of fuck.caniuse action to var big_fucking_hammer
# escaping out special characters so they print
big_fucking_hammer = fuck.caniuse(tool="the \'BFH\' (big fucking hammer)", from_="Dustin")

# print string stored in nvar big_fucking_hammer and remove newline
# with end=""; adding a little extra at the end so we know who
# keeps the BFH
print(big_fucking_hammer.text, end="")
print(" (keeper of the BFH)" + '\n')
print("=====================================================================\n")
# assign response value of fuck.particular action to var
# recursion_fuck, and multiply our arg string for thing
# by 5 so we can simulate mild recursion in our print statement
recursion_fuck = fuck.particular(thing="recursion loop" * 5, from_="Dustin").text

# create string slices of string stored in recursion_fuck
# and assign them to variables that can more easily be formatted
fuck_this = recursion_fuck[0:9]
recursion_one = recursion_fuck[9:24]
recursion_two = recursion_fuck[24:38]
recursion_three = recursion_fuck[38:52]
recursion_four = recursion_fuck[52:66]
recursion_five = recursion_fuck[66:80]
in_particular = recursion_fuck[80:94]
my_name = recursion_fuck[95:109]

# store formatted multiline string in fuckery variable
fuckery = '''\
      {a}
      {b}
         {c}
            {d}
               {e}
                  {f}
                     {g}.
                      {h}\
                    '''.format(a=fuck_this, b=recursion_one, c=recursion_two, d=recursion_three, e=recursion_four, f=recursion_five, g=in_particular, h=my_name)

# print multiline string stored in fuckery
print(fuckery)
