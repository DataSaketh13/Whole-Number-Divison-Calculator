print("Welcome to the divisible calculator.")

num2 = int(input("What number do you want to check if a number is divided by, will return a whol number?"))
num1 = int(input("What is the number you want to divide by?"))

num3 = num1 % num2
num4 = num2 / num1


if num3 == 0:
      print("The number", num1, "is divisible by", num2,". Will return a whole number. The quotient is", num4) 

else:
    print("The number", num2, "divided by", num1, "will not return a whole number value. The quotient is", num4)

