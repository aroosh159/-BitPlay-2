def checkIfSame(number1,number2):
    if((number1 ^ number2)!=0):
        print("Numbers are not equal")
    else:
        print("Numbers are equal")

number1 = int(input("First number to compare with"))
number2 = int(input("second number to compare with"))

checkIfSame(number1,number2)