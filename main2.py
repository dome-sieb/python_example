#Vergleichsoperatoren
1 < 5 #1 kleiner als 5 -> True
1 > 5 #1 größer als 5 -> False
1 <= 5 #1 kleiner gleich 5 -> True
1 >= 5 #1 größer gleich 5 -> False
1 == 5 #1 gleich 5 -> False
1 != 5 #1 ungleich 5 -> True
print(1 < 5)
print(1 > 5)
print(1 <= 5)
print(1 >= 5)
print(1 == 5)
print(1 != 5)

age = int(input("Bitte gebe dein Alter ein:"))
if age < 18:
    print("Du bist noch nicht Volljährig")
elif age == 18:
    print("Du bist gerade Volljährig geworden")    
else:
    print("Du bist Volljährig")

    