# Dictionary of Operations
operation_dict = {
    'a' : '+',
    'b' : '-',
    'c' : '*',
    'd' : '/',
    'e' : '%',
    'f' : '**',
    'g' : '//'
}
while True:
    while True: # Ensures a loop if ever user inputted a non-valid value for the first number
        first_number = str(input("Enter your first non-negative integer: "))
        if not first_number.isdigit() or int(first_number) < 0:
            print("Invalid Input. Must input non-negative integer only.\n")
            continue
        break
    while True: # Ensures a loop if ever user inputted a non-valid value for the second number
        second_number = str(input("Enter your second non-negative integer: "))
        if not second_number.isdigit() or int(second_number) < 0 :
            print("Invalid Input. Must input non-negative integer only.\n")
            continue
        break
    while True: # Ensures a loop if ever user inputted a non-valid value for the operation
        user_choice = input("Please choose the letter of the corresponding operation you want to apply:\na). Addition\nb). Subtraction\nc). Multiplication\nd). Division\ne). Modulus Division\nf). Exponent\ng). Floor Division\nUser Input: ")
        if user_choice not in operation_dict:
            print("Invalid Input. Must only enter and pick selection from given options.")
            continue
        print(f'The answer is {eval(first_number+operation_dict[user_choice]+second_number)} !') # eval is used for evaluating the value of the string that will be created by the merging of strings
        break
    user_input = input("Do you want to continue [any key] or exit the program[x]?\nUser Input: ") 
    if user_input == 'x':
        print("Thank you for using the program!")
        quit()
    else:
        continue