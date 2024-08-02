import random

upper_bound = 100


secret_number = random.randint(0, upper_bound)
#print(secret_number)

print("Es wurde soeben eine Zufallszahl zwischen 0 und "+str(upper_bound) +" generiert.")
print("Deine Aufgabe ist es zu erraten, welche Zahl es ist.")
print("Viel Erfolg!")

guess = None
count = 1

while guess != secret_number:

    guess = int(input("Waehle eine Ganzzahl zwischen 0 und " +str(upper_bound) + ":"))

    if guess == secret_number:
        print("Yeahhh, das ist richtig!")
    elif guess < secret_number:
        print("Die gesuchte Zahl ist groesser als deine geratene Zahl!")
        count = count + 1
    else:
        print("Die gesuchte Zahl ist kleiner als deine geratene Zahl!")
        count = count + 1
print("Du hast " + str(count) + " Versuche gebraucht, um die richtige Zahl zu erraten!")