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

#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3

def select_op(choice):
  if (choice == "#"):                               #if the choice is "#" exit the program.
    return -1
  elif (choice == "$"):                             #if the choice is $ reset
    return 0
  elif choice in ('+','-','*','/','^','%'):
    while (True):
      num1str = str(input("Enter first number: "))      
      print(num1str)
      if num1str.endswith('#'):                       #check the input contains "# or $"
        return -1
      if num1str.endswith('$'):
        return 0
      try:
        num1 = float(num1str)                           # handling value error if invalid input is entered.
        break
      except ValueError:
        print("Not a valid number,please enter again")
        continue

    while (True):
      num2str = str(input("Enter second number: "))
      print(num2str)
      if num2str.endswith('#'):
        return -1
      if num2str.endswith('$'):
        return 0
      try:
        num2 = float(num2str)
        break
      except ValueError:
        print("Not a valid number,please enter again")
        continue    
      
    if choice == "+":
      print(num1, "+", num2, "=", add(num1,num2))
        
    elif choice == "-":
      print(num1, "-", num2, "=", substract(num1,num2))
        
    elif choice == "*":
      print(num1, "*", num2, "=", multiply(num1,num2))
            
    elif choice == "/":
      print(num1, "/", num2, "=", devide(num1,num2))    
        
    elif choice == "^":
      print(num1, "^", num2, "=", power(num1,num2))
        
    elif choice == "%":
      print(num1, "%", num2, "=", remainder(num1,num2))
    
    else:
      print("Something Went Wrong")
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
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()