# ** Lab Description - [Lab 3a](https://btc.instructure.com/courses/1997047/assignments/20426458)

## * Practice formatting and printing strings using the book and sample program examples. Practice using the following:
    * single and double quotes
    * triple quotes
    * backslash escape for special characters like apostrophes
    * multiple embedded values using %s, %d, and %f
    * multiplying strings
    * removing the newline of a print statement with end=""
    * adding newlines to print statements

## * For credit, write a small program that produces text output using the above techniques. Describe your use of these techniques in your recorded or in-person code walkthrough.
    - [ ] Single and Double Quotes
    - [ ] Triple Quotes
    - [ ] Backslash Escape for Special Characters (e.g. apostrophe)
    - [ ] Multiple embedded values using %s, %d, and %f
    - [ ] Multiply Strings
    - [ ] Removing the newline of print statement with end=""
    - [ ] Adding newlines to print statements

# **Chapter 3a String Examples

## * --- Working with strings

```python
# A string is a collection of letters. You can enclose a string with
# matching single quotes (') or double quotes ("). According to python
# there is no difference between single and double quotes so use whatever
# the standard is where you work and be consistent.

myString = "a b c 1 2 3"
print (myString)

# Printing a multi-line string won't work with single or double quotes.
# Use triple quotes which is three single quotes in a row. (''')
# Try using double or single quotes instead and see the error.

joke = '''What is Beethoven doing now?
De-composing.'''
print (joke)

# For special characters you can "escape" the specialness by putting
# a backslash (\) before the character. Try removing the backslash in
# the following line to see the error.

joke = 'I\'d tell you a UDP joke but you might not get it.'
print (joke)

# To "embed" or insert values or variables into strings use %s to mark the
# substitution position and follow the string with % and the value to embed.

myFirstName = "Monty"
print ("My name is %s." % myFirstName)

# To embed multiple values use multiple %s substitution markers followed
# by % and a list of values that match position.
myLastName = "Python"
print ("My full name is %s %s." % (myFirstName, myLastName) )

# Sometimes you want to embed numbers.
# Use %d for integers, %f for floating point.
pythonCount = 5.5
print ("There were %d members of %s %s." % (pythonCount, myFirstName, myLastName))
print ("There were %.2f members of %s %s." % (pythonCount, myFirstName, myLastName))

# You can multiply strings in a print statement.
print ("spam " * 2)
print ("spam " * 2, "sausage and spam")
print ("spam " * 8, "baked beans", "spam " * 2, "and spam")

# You can remove the newline character at the end of a print if you want to leave
# the curser or start the next print statement at the end of the string
# instead of having it start on the next line.
print ("spam " * 2, end="")
print ("sausage and spam")

# You can add lines by adding \n in your strings.
print ("I\'ll have ", end="")
print ("spam " * 6, end="")
print ("baked beans\n\n")

# https://docs.python.org/2/library/time.html
import time
time.sleep(3)
print ("...hmmmm...\n\n")
time.sleep(2)
print ("and spam.")
```
