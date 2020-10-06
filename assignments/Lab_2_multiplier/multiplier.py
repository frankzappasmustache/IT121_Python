# Store the user input as integers in two separate variables
numeroUno = int(input("Enter any number: "))
numeroDos = int(input("Enter another number: "))

# Perform the four standard arithmetic operations on the two variables
# and store the result of each operation in its own variable
producto = numeroUno * numeroDos
cotiente = numeroUno / numeroDos
suma = numeroUno + numeroDos
diferencia = numeroUno - numeroDos

# Print the result of each operation by pulling in the variable for each
# entered number and the result of each operation
print("The product of", numeroUno, "and", numeroDos, "is", producto)
print("The quotient of", numeroUno, "and", numeroDos, "is", cotiente)
print("The sum of", numeroUno, "and ", numeroDos, "is", suma)
print("The difference of", numeroUno, "and", numeroDos, "is", diferencia)
