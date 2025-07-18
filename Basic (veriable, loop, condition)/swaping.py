number1 = int(input("Enter fist number: "))
number2= int(input("Enter second number: "))

#swap without third veriable
number1 += number2
number2 = number1 - number2
number1 -= number2
print("number1 is",number1,"and", "number2 is",number2) 