import random  
import time

damage = True      # permet de choisir si je vais prendre des déguat ou non (utilisé pour aattaque2 de Carapuce)
Pokemon_health = 0 # valeur des PV du pockemon utilisé
choice = 0         # sélection du pockémon
attack_1 = 0       # attaque de base des pokémon
attack_2 = 0       # capacité spécial des pokémon

Pickachu = 60      # Pv de Pikachu
Salamèche = 70     # ...
Bulbizarre = 70    # ...
Carapuce = 70      # ...

# fonction qui permet de choisir le pockémon
def Pokemon_Choice():
    global choice, attack_1, attack_2
    while True:                         # Utilisé pour donné une seconde chance un incompétent
        choice = input("sélectionner un pockémon. Pikachu, Salamèche, Bulbizarre, Carapuce\n:")
        if choice == "Pikachu":
            attack_1 = 10 
            attack_2 = 0 
            print("Pika Pika")
            return
        elif choice == "Salamèche":
            attack_1 = 30
            attack_2 = 0 
            return
        elif choice == "Bulbizarre":
            attack_1 = 30
            attack_2 = 0 
            return
        elif choice == "Carapuce":
            attack_1 = 30
            attack_2 = 0 
            return
        else:
            print("NAAAAANNNNN")# message affiché si la réponse n'est pas valide

while True:
    Pokemon_Choice()
    Boss_HP = 100
    while True:
        attack_choice = input("sélectionner une attaque. 1(attaque de base), 2(capacité)\n:")
        if attack_choice == "1":
            print(attack_1)

        elif attack_choice == "2":

    # Capacité de Pikachu
            if choice == "Pikachu":
                Time = 0.001
                for i in range(25):                 # le for sert seulement a ajouter un impression de azard
                    print(random.randint(1, 2))
                    time.sleep(Time)
                    Time += 0.005

                time.sleep(0.5)                     # tout les valeur utilisable qui permet de seter l attaque 2 (repeter pour tous les autre capaciter)
                Secousse_Tonnerre = random.randint(1, 2)
                print(Secousse_Tonnerre)
                time.sleep(0.5)
                if Secousse_Tonnerre == 1:
                    attack_2 = 30 + 20
                    print(attack_2)
                elif Secousse_Tonnerre == 2:
                    attack_2 = 30
                    print(attack_2)

    # Capacité de Salamèche
            elif choice == "Salamèche":
                Time = 0.001
                for i in range(25):
                    print(random.randint(1, 2))
                    time.sleep(Time)
                    Time += 0.005

                print()
                time.sleep(0.5)
                cri_stident = random.randint(1, 2)
                print(cri_stident)
                if cri_stident == 1:
                    cri_stident = random.randint(3, 4)
                    print(cri_stident)
                    if cri_stident == 3:
                        attack_2 = 90
                        print(attack_2)
                    else:
                        attack_2 = 50
                        print(attack_2)
                elif cri_stident == 2:
                    attack_2 = 20
                    print(attack_2)
    # Capacité de Bulbizarre
            elif choice == "Bulbizarre":
                freeze = random.randint(1,2)
                print(freeze)
                if freeze == 1:
                    attack_2 = 10
                    print(attack_2)
                    print("bravo. tu a freeze l'adversaire")
                    continue
                else:
                    attack_2 = 10
                    print(attack_2)
    # Capcit
            elif choice == "Carapuce":
                repli = random.randint(1,3)
                if repli == 1:
                    attack_2 = 20
                    print(attack_2)
                    print("vous avez un blouclié")
                    damage = False
                else:
                    attack_2 = 20
                    print(attack_2)
        else:    
            print("NAAAAANNNNN")

        print("YEESSSSSS")# cette section permet de voir les PV de l'adversaire 
        if attack_choice == "1":
            Boss_HP -= attack_1
            print(Boss_HP)
        elif attack_choice == "2":
            Boss_HP -= attack_2
            print(Boss_HP)