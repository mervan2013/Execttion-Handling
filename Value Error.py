
try:
    number = int(input("Enter A Number: "))
    print("The Number Enterd is", number)
except ValueError as ex:
    print("Exception", ex)