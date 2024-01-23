#Program for simple calculator

#Function to display the options of operations
def display_operations():

    print("\n!!!!!!!!!!    OPERATIONS       !!!!!!!!!!!!!")
    print("\n1. Addition of two numbers")
    print("\n2. Subtraction of two numbers")
    print("\n3. Multiplication of two numbers")
    print("\n4. Division of two numbers")
    print("\n5. Remainder of two numbers")
    print("\n6. Exponentiation of two numbers")
    print("\n7. Floor division of two numbers")
    print("\n8. Exit")

#End of display_operations() function


#The Function to perform addition operation
def addition():
    print("\nADDITION:")
    #Get the input numbers from the user
    number_add1 = float(input("\nEnter First Number : "))  
    number_add2 = float(input("\nEnter Second Number : "))
    #A var that stores and calculate the addition of two numbers 
    addition_numbers=number_add1+number_add2
    #A print statement to display the added numbers
    print('\nAddition of Given Numbers is : ',addition_numbers)
    return addition_numbers
#End of addition() function

       
#The Function to perform subtraction operation
def subtract():
    print("\nSUBTRACTION:")
    #Get the input numbers from the user
    number_sub1=float(input("\nEnter First Number : "))
    number_sub2=float(input("\nEnter Second Number : "))
     #A var that stores and calculate the subtraction of two numbers 
    result_sub=number_sub1-number_sub2
    #A print statement to display the subtracted numbers
    print("\nSubtraction of Given Numbers is : ",result_sub)
    return result_sub
#End of subtract() function


#The Function to perform multiplication operation
def multiply():
    print("\nMULTIPLICATION:")
    #Get the input numbers from the user
    number_mul1=float(input("\nEnter First Number :"))
    number_mul2=float(input("\nEnter Second  Number :"))
     #A var that stores and calculate the multiplication of two numbers 
    result_mul=number_mul1*number_mul2
    #A print statement to display the multiplied numbers
    print("\nMultiplication of Given Numbers is : ",result_mul)
    return result_mul
#End of multiply() function


#The Function to perform division operation
def divide():
    print("\nDIVISION:")
     #Get the input numbers from the user
    number_div1=float(input("\nEnter First Number :"))
    number_div2=float(input("\nEnter Second Number :"))
    if number_div2==0:
        print("\nError! Division by zero is not allowed.")
        print("Division of Given Numbers :",number_div2)
        exit()
    else:
     #A var that stores and calculate the division of two numbers 
        result_div=number_div1/number_div2
    
     #A print statement to display the divided numbers
    print("\nDivision of Given Numbers is : ",result_div)
    return result_div
#End of division() function


#The Function to get the remainder
def remainder():
    print("\nREMAINDER:")
    #Get the input numbers from the user
    number_rem1=float(input("\nEnter First Number :"))
    number_rem2=float(input("\nEnter Second Number :"))
    if number_rem2==0:
        print("\nError! Division by zero is not allowed.")
        print("Division of Given Numbers :",number_rem2)
        exit()
    else:
         #A var that stores and calculate the remainder of two numbers 
        result_rem=number_rem1%number_rem2
         #A print statement to display the remainder
    print("\nRemainder of Given Numbers is : ",result_rem)
    return result_rem
#End of remainder() function


#The Function to get the exponentiation
def exponentiation():
    print("\nEXPONENTIATION:")
    #Get the input numbers from the user
    number_base = float(input("\nEnter the Base Value : "))
    number_power = int(input("\nEnter the Power : "))
    #A var that stores and calculate the exponentiation of two numbers 
    result_exp = number_base**number_power
    #A print statement to display the exponentiation
    print("\nExponentiation of Given Numbers is : ",result_exp)
    return result_exp
#End of exponentiation() function


#The Function to get the floor division
def floordivision(): 
    print("\nFLOOR DIVISION:")
    #Get the input numbers from the user
    number_fd1 = float(input("\nEnter the Dividend :"))
    number_fd2 = float(input("\nEnter the Divisor :"))
     #A var that stores and calculate the floordivision of two numbers 
    result_fd = number_fd1 // number_fd2
    #A print statement to display the floordivision
    print("\nFloor Division Result :",result_fd)
    return result_fd
#End of floordivision() function

#Function to call the calulator operations
def operation():

    #Calling the display_operations() function for displaying the choices   
    
    display_operations()
    
    #Get the input from the user
    
    option=int(input("\nEnter A Number For Choosing the Operation:"))
    while option !=8:
        #A  statement 'match' for calling the operations
        match option:
            case 1:
               addition() 
            case 2:
               subtract()
            case 3:
               multiply()
            case 4:
               divide()
            case 5:
               remainder()
            case 6:
               exponentiation()
            case 7:
               floordivision()
            case 8:
               exit() 
            case 9 :
                print("Please Enter a Valid Option!!")
                exit()
        display_operations()
        option=int(input("\nEnter A Number For Choosing the Operation:"))

#End of operation() function
        
#Calling the function operation() to start the program
operation()