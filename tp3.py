import random
game_loop = True
lvl_life = 300
combat_nbr = 20
victory_nbr = 30
defeat_nbr = 24
nombre_victoires_consecutives = 0
afficher_regle = False
force_adversaire = 0
monstre_fort = False
victoire_monstre_fort = 0

while game_loop:
   if not afficher_regle:
       if not monstre_fort:
           force_adversaire = random.randint(1, 5) + random.randint(1, 5)
           print(f"Vous tombez face à face avec un adversaire de difficulté : {force_adversaire}")
       else:
           force_adversaire = random.randint(4, 5) + random.randint(4, 5)
           print(f"Vous tombez face à face avec un adversaire de haut niveau : {force_adversaire}")
           monstre_fort = False
   else:
       afficher_regle = False
       print(f"Vous tombez face à face avec un adversaire de difficulté : {force_adversaire}")

   option_menu = int(input("""Que voulez-vous faire ?
1- Combattre cet adversaire
2- Contourner cet adversaire et aller ouvrir une autre porte
3- Afficher les règles du jeu
4- Quitter la partie
"""))

   if option_menu == 1:
       combat_nbr += 1
       print(f"Force de l'adversaire : {force_adversaire} \n"
             f"Niveau de vie : {lvl_life} \n"
             f"Combat {combat_nbr} : {victory_nbr} vs {defeat_nbr}")
       dice_combat = random.randint(1, 6) + random.randint(1, 6)
       print(f"Lancer du dé : {dice_combat} ")

       if dice_combat > force_adversaire:
           print("Dernier combat = Victoire")
           lvl_life += force_adversaire
           nombre_victoires_consecutives += 1
           victoire_monstre_fort += 1
           victory_nbr += 1
           print(f"Niveau de vie : {lvl_life}\n"
                 f"Nombre de victoires consécutives : {nombre_victoires_consecutives}")

       else:
           print("Dernier combat = Défaite")
           nombre_victoires_consecutives = 0
           lvl_life -= force_adversaire
           defeat_nbr += 1
           print(f"Niveau de vie : {lvl_life}")

   elif option_menu == 2:
       lvl_life -= 1
       print("Vous avez une pénalité de 1 point de vie\n"
             f"Niveau de vie : {lvl_life}")

   elif option_menu == 3:
       input(
           "Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.\n"
           "Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.\n"
           "Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure "
           "ou égale à la force de l’adversaire.\n"
           "Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\n"
           "La partie se termine lorsque les points de vie de l’usager tombent sous 0.\n"
           "L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, "
           "il y a une pénalité de 1 point de vie.\n")
       afficher_regle = True
   else:
       game_loop = False

   if victoire_monstre_fort == 3:
       monstre_fort = True
       victoire_monstre_fort = 0

   if lvl_life <= 0:
       print(f"La partie est terminée, vous avez vaincu {victory_nbr} monstres")
       game_loop = False
