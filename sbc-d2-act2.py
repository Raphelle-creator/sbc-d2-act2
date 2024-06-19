from random import randint

choice1 = "Fold"
choice2 = "Unfold"
hum = randint(0,1)
pyang = randint(0,1)

user = input("Choose Fold or Unfold :")
if user.capitalize() == "Fold":
    p1 = "Fold"
    print("P1 = ", user)
else:
    p1 = "Unfold"
    print("P1= Unfold")

com2 = hum
if com2 == 1:
    com2 = "Fold"
    print("C2 = Fold")
else:
    com2 = "Unfold"
    print("C2 = Unfold")
com3 = pyang
if com3 == 1:
    com3 = "Fold"
    print("C3 = Fold")
else:
    com3 = "Unfold"
    print("C3 = Unfold")

if (p1 == "Fold" and com2 == "Unfold" and com3 == "Unfold") or (p1 == "Unfold" and com2 == "Fold" and com3 == "Fold"):
    print("P1 Win!")

elif (p1 == "Unfold" and com2 == "Fold" and com3 == "Unfold") or (p1 == "Fold" and com2 == "Unfold" and com3 == "Fold"):
    print("C2 Win!")

elif (p1 == "Unfold" and com2 == "Unfold" and com3 == "Fold") or (p1 == "Fold" and com2== "Fold" and com3 == "Unfold"):
    print("C3 Win!")
else:
    print("No one wins!")