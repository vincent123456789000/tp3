import random
game_loop = True
combat_nbr = 20
defeat_nbr = 24
number_of_consecutive_victories = 0
victory_nbr = 30
lvl_life = 300
rule_show = False
victoire_strength_monster = 0
strength_monster = False
opponent_strength = 0

while game_loop:
   if not rule_show:
       if not strength_monster:
           opponent_strength = random.randint(1, 5) + random.randint(1, 5)
           print(f"Vous tombez face à face avec un adversaire de difficulté : {opponent_strength}")
       else:
           opponent_strength = random.randint(4, 5) + random.randint(4, 5)
           print(f"Vous tombez face à face avec un adversaire de haut niveau : {opponent_strength}")
           strength_monster = False
   else:
       rule_show = False
       print(f"Vous tombez face à face avec un adversaire de difficulté : {opponent_strength}")

   option_menu = int(input("""Que voulez-vous faire ?
1- Combattre cet adversaire
2- Contourner cet adversaire et aller ouvrir une autre porte
3- Afficher les règles du jeu
4- Quitter la partie
"""))

   if option_menu == 1:
       combat_nbr += 1
       print(f"Force de l'adversaire : {opponent_strength} \n"
             f"Niveau de vie : {lvl_life} \n"
             f"Combat {combat_nbr} : {victory_nbr} vs {defeat_nbr}")
       dice_combat = random.randint(1, 6) + random.randint(1, 6)
       print(f"Lancer du dé : {dice_combat} ")

       if dice_combat > opponent_strength:
           print("Dernier combat = Victoire")
           lvl_life += opponent_strength
           number_of_consecutive_victories += 1
           victoire_strength_monster += 1
           victory_nbr += 1
           print(f"Niveau de vie : {lvl_life}\n"
                 f"Nombre de victoires consécutives : {number_of_consecutive_victories}")

       else:
           print("Dernier combat = Défaite")
           number_of_consecutive_victories = 0
           lvl_life -= opponent_strength
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
       rule_show = True
   else:
       game_loop = False

   if victoire_strength_monster == 3:
       strength_monster = True
       victoire_strength_monster = 0

   if lvl_life <= 0:
       print(f"La partie est terminée, vous avez vaincu {victory_nbr} monstres")
       game_loop = False
