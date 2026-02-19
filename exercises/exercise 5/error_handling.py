

while True:     
    try:
        number = float(input("Give  a number: "))
        break 
    except ValueError:
        print("That is not a valid number. Please try again.")  

    
print("You entered a valid number :", number)
    