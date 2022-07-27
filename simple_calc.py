#TODO: Write the functions for arithmatic operations here
#These functions should cover Task 2

#this function add two numbers.
def add(x, y):
    return x + y

#this function substracts numbers.
def substract(x, y):
    return x - y
    
#this function multiply numbers.
def multiply(x, y):
    return x * y
    
#this function devide numbers.
def devide(x, y):
#checks y is zero to prevent zero division error    
    if y == 0:
        print("float division by zero")
    else:
        return x / y
    
#this function gives power of x.
def power(x, y):
    return x ** y
    
#this function gives remainder of x numbers.
def remainder(x, y):
    return x % y

#gets two float inputs and make sure it is a float.
def get_two_floats():
    while True:
        try:
            num1 = float(input ("Enter first number: "))
            print(int(num1))
            num2 = float(input ("Enter second number: "))
            print(int(num2))
        except ValueError:
            print("When I ask for a number, give me a number.")
        else:
            return num1, num2


#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3

def select_op(choice):

  if choice in ('+','-','*','/','^','%',"#","$"):
      if choice == "+":
        num1, num2 = get_two_floats()
        print(num1, "+", num2, "=", add(num1,num2))
          
      elif choice == "-":
        num1, num2 = get_two_floats()
        print(num1, "-", num2, "=", substract(num1,num2))
          
      elif choice == "*":
        num1, num2 = get_two_floats()
        print(num1, "*", num2, "=", multiply(num1,num2))
              
      elif choice == "/":
        num1, num2 = get_two_floats()
        print(num1, "/", num2, "=", devide(num1,num2))    
          
      elif choice == "^":
        num1, num2 = get_two_floats()
        print(num1, "^", num2, "=", power(num1,num2))
          
      elif choice == "%":
        num1, num2 = get_two_floats()
        print(num1, "%", num2, "=", remainder(num1,num2))
      
      elif choice == '#':
        print("Done. Terminating")
        exit()
    
  else:
    print("Unrecognized operation")

#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(select_op(choice) == '-1'):
    break
  #program ends here
  #print("Done. Terminating")
    #exit()

else:
  select_op(choice)
  