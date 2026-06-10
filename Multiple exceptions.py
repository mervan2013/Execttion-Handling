try:
    num1, num2 = eval(input("Enter 2 numbers seperated by only a comma : "))
    result = num1/num2
    print("Result is :", result)


except ZeroDivisionError:
    print("Divsion by Zero is an error!!!")

except SyntaxError:
    print("Comma is missing between numbers please enter a , between them")

except:
    print("Wrong Input")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what")