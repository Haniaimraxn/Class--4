# Exceptional Handling (try, except, else, finally)

def divide_numbers():
    try:
        num1 = int(input("Enter the numerator: "))
        num2 = int(input("Enter the denominator: "))
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: You can't divide by zero.")
    except ValueError:
        print("Error: Please enter valid integers.")
    else:
        print("Division successful. Result is:", result)
    finally:
        print("End of program. Thank you!")

# Call the function
divide_numbers()
    

