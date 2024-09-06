from puv import PUV
while True:
    user_type = input("What kind of passenger are you? (Select one among the following)\n1. Regular\n2. Student\n3. Senior Citizen\n")
    if user_type.strip().isdigit():
        if int(user_type) == 1:
            user_type = "regular"
        elif int(user_type) == 2:
            user_type = 'student'
        elif int(user_type) == 3:
            user_type = 'senior citizen'
    if user_type.lower() not in ['regular', 'student', 'senior citizen']:
        print("Invalid Passenger Type. Please select only among the option")
        continue
    
    passenger = PUV(user_type)
    break
while True:
    user_choice = input("What mode of transportation would you like to ride?\n1.\tJeep\n2.\tTricycle\n3.\tBus\n[x].\tClose Program\n")
    if user_choice == '1' or user_choice.lower == 'jeep':
        passenger.jeep_rate()
    elif user_choice == '2' or user_choice.lower == 'tricycle':
        passenger.tricycle_rate()
    elif user_choice == '3' or user_choice.lower == 'bus':
        passenger.bus_rate()
    elif user_choice.lower() == 'x':
        print("Thank you for riding with us!")
        quit()
    else:
        print("Invalid Mode of Transportation. Please select only from the option")