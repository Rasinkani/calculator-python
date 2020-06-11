while True:
    print("Options:")
    print("Enter 'add to add two numbers")
    print("Enter 'substract' to substract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to quit the program")
    u_input = input(":")
     
    if u_input == "quit":
        break
    elif u_input == "add":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 + num2)
        print("Answer : "+ result)
     
    elif u_input == "substract":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 - num2)
        print("Answer : "+ result)
    
    elif u_input == "multiply":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 * num2)
        print("Answer : "+ result)
        
    elif u_input == "divide":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 / num2)
        print("Answer : "+ result)
    elif u_input == "mod":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 % num2)
        print("Answer : "+ result)
    else:
        print("try again !")
