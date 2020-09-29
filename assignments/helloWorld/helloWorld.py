# Create a list containing all characters plus some :)
helloCruelWorld = ['H', 'e', 'l', 'l', 'o', 'C',
                   'r', 'u', 'e', 'l', 'W', 'o', 'r', 'l', 'd']

# Iterate over all items in our list with '' defined as their separator
# and for each item (x) concatenate into one string object, which is 
# stored in the variable hello
hello = ''.join([str(x) for x in helloCruelWorld])

# Filter one's cynical view of the world by replacing the second word in
# our string object with a convenient comma and space, which is stored in
# the variable world
world = hello.replace('Cruel', ', ')

# Add a dose of enthusiasm to our statement by adding an exclamation point
# to the end of our parsed down string, which is stored in the variable
# helloWorld
helloWorld = world + '!'

# Print our string object as we want it to be with python's print function
print(helloWorld)
