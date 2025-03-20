# ask for 2 nums, ask for operator , do computation, give results

#welcome statement and user guide
welcomeMessage = "Welcome to Kalwenzi's calculator. To use it, follow the simple instructions below."
print(welcomeMessage)

num1 = float(input("Enter Your First Number : "))
if not type(num1)==float:
    print("Please enter a valid number.")
#validate first number before taking second number

if not type(num1)==float:
    print("Please enter a valid number.")

num2 = float(input("Enter your second number : "))

if not type(num2)==float:
    print("Please enter a valid number.")
else:
    print("Good! Now select an operator from below ")


#print("+ : add\n- : subtract\n* : multiply\n/ : divide")"
print("operators : -,+,*,/")
operator = str(input("Enter the selected operator : "))



def doCalculation ():
    if operator == "+":
        result = num1+num2        
    elif operator == "-":
        result= num1-num2
    elif operator == "*":
        result = num1*num2
    else:
        result = num1/num2
    return result

if not operator in ["+","-","*","/"]:
    print("Please enter a valid operator.")
else:
    result = doCalculation()
    print("The result is : ", result)