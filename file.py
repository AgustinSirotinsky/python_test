import random
import os
import time

clear =lambda: os.system('cls')

while True:
    gamemode = input("Welcome! What would you like to do? \n 1. Let AI solve your number \n 2. Solve the number \n 3. See how many tries a RNG takes in order to discover your number\n 4. Exit \n")

    if gamemode == "1":
        tries = 0

        a = int(input("Enter a minimum number: "))
        b = int(input("Enter a maximum number: "))
        number = int(input("Enter a number to solve: "))
        while number>b or number<a or a>b: #in case the user enters a number outside the range
            print("Invalid input!")
            a = int(input("Enter a minimum number: "))
            b = int(input("Enter a maximum number: "))
            number = int(input("Enter a number to solve: "))
        clear() #clears the screen
        while True:
            time.sleep(0.25)
            random_number = random.randint(a+1, b-1)
            if number == random_number:
                print(random_number, "is the correct number, it took", tries, "tries")
                user_continue = input("Press enter to return to the menu")
                clear () #clears the screen
                break
            else:
                tries+=1
                if random_number > number:
                    b = random_number
                    print (random_number, "is higher than selected number, now the minimum is", a, "and the maximum is", b)
                else:
                    a = random_number
                    print (random_number, "is lower than selected number, now the minimum is", a, "and the maximum is", b)

    elif gamemode=="2":
        tries = 0

        a = int(input("Enter a minimum number: "))
        b = int(input("Enter a maximum number: "))
        while a>b: #in case the user enters a number outside the range
            print("Invalid input!")
            a = int(input("Enter a minimum number: "))
            b = int(input("Enter a maximum number: "))
        clear() #clears the screen
        continue_game=True
        while continue_game:
            time.sleep(0.25)
            random_number = random.randint(a+1, b-1)
            clear()
            while True:
                number = int(input("Select a number:"))
                if number<a:
                    print(number, "is lower than the minimum established")
                elif number>b:
                    print(number, "is higher than maximum established")
                elif number>random_number:
                    print(number, "is higher than the randomized number")
                    tries+=1
                elif number<random_number:
                    print(number, "is lower than the randomized number")
                    tries +=1
                elif number==random_number:
                    print("Congratulations!", random_number, "was the correct number, it took you", tries, "tries")
                    user_continue = input("Press enter to return to the menu")
                    continue_game=False #BreaKs outer loop
                    clear () #clears the screen
                    break
    elif gamemode=="3":
        tries = 0

        a = int(input("Enter a minimum number: "))
        b = int(input("Enter a maximum number: "))
        number = int(input("Enter a number to solve: "))
        while number>b or number<a or a>b: #in case the user enters a number outside the range
            print("Invalid input!")
            a = int(input("Enter a minimum number: "))
            b = int(input("Enter a maximum number: "))
            number = int(input("Enter a number to solve: "))
        clear() #clears the screen
        while True:
            time.sleep(0.10)
            random_number = random.randint(a+1, b-1)
            if number == random_number:
                print(random_number, "is the correct number, it took", tries, "tries")
                user_continue = input("Press enter to return to the menu")
                clear () #clears the screen
                break
            else:
                tries+=1
                print("Random number:", random_number)
    elif gamemode=="4":
            print("Bye!")
            break
