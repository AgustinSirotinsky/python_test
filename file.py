import random


gamemode = input("Welcome! what would you like to do? \n 1. Let AI solve your number \n 2. Solve the number \n 3. Exit \n")

if gamemode == "1":
    number = int(input("Enter a number to solve: "))

    a = 0
    b = 1000000000000
    tries = 0
    while True:
        random_number = random.randint(a+1, b-1)
        if number == random_number:
            print(random_number, "is the correct number, it took ", tries, " tries")
            break
        else:
            tries+=1
            if random_number > number:
                b = random_number
                print (random_number, " is higher than selected number, now the minimum is ", a, "and the maximum is ", b)
            else:
                a = random_number
                print (random_number, " is lower than selected number, now the minimum is ", a, "and the maximum is ", b)
elif gamemode=="2":
        print("lol!")
