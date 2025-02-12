import random
import time


Pokemon_health = 0
choice = 0
attack_1 = 0
attack_2 = 0

Pickachu = 60
Salamèche = 70
Bulbizarre = 70
Carapuce = 70


def Pokemon_Choice():
    global choice, attack_1, attack_2
    while True:
        choice = input()
        if choice == "Pikachu":
            attack_1 = 10
            attack_2 = 0 #Secousse_Tonnerre()
            print("allo")
            return
        elif choice == "Salamèche":
            attack_1 = 30
            attack_2 = 0 #crie_stident()
            return
        elif choice == "Bulbizarre":
            attack_1 = 20
            attack_2 = 0 #freeze()
            return
        elif choice == "Carapuce":
            attack_1 = 20
            attack_2 = 0 #Repli()
            return
        else:
            print("NAAAAANNNNN")


Pokemon_Choice()
while True:
    attack_choice = input()
    if attack_choice == "1":
        print(attack_1)

    elif attack_choice == "2":

        if choice == "Pikachu":
            Time = 0.001
            for i in range(25):
                print(random.randint(1, 2))
                time.sleep(Time)
                Time += 0.005

            time.sleep(0.5)
            Secousse_Tonnerre = random.randint(1, 2)
            print()
            print(Secousse_Tonnerre)
            time.sleep(0.5)
            if Secousse_Tonnerre == 1:
                attack_2 = 30 + 10
                print(attack_2)
            elif Secousse_Tonnerre == 2:
                attack_2 = 30
                print(attack_2)
            if choice == "Salamèche":
                Time = 0.001
            for i in range(25):
                print(random.randint(1, 2))
                time.sleep(Time)
                Time += 0.005
    else:   
        print("NAAAAANNNNN")