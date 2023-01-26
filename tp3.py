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
           opponent_strength = random.randint(5, 100) + random.randint(5, 100)
           print(f"Voici un combatant d'une force de : {opponent_strength}")
            
            
            
       else:
           opponent_strength = random.randint(100, 500) + random.randint(100, 500)
           print(f"Voici un combatant d'une force plus grande de : {opponent_strength}")
           strength_monster = False
            
            
            
   else:
       rule_show = False
       print(f"Voici un combatant d'une force de : {opponent_strength}")
   option_menu = int(input("""Qu'allez vous faire !?!?
1- Essayer de le vaincre ?
2- Faire montré les règle de la partie ?
3- L'éviter et aller a une autre porte ?
4- Quitter 
"""))
   
   
   
   if option_menu == 1:
       combat_nbr += 1
       print(f"Puissance du combatant : {opponent_strength} \n"
             f"Vie : {lvl_life} \n"
             f"Combat {combat_nbr} : {victory_nbr} vs {defeat_nbr}")
       dice_combat = random.randint(1, 6) + random.randint(1, 6)
       print(f"On lance le dice : {dice_combat} ")
      
      
      
       if dice_combat > opponent_strength:
           print("Votre combat qui décide si l'aventure est fini ou non = Victoire")
           lvl_life += opponent_strength
           number_of_consecutive_victories += 1
           victoire_strength_monster += 1
           victory_nbr += 1
           print(f"Vie : {lvl_life}\n"
                 f"Victoires à la suite : {number_of_consecutive_victories}")
            
            
            
       else:
           print("Votre combat qui décide si l'aventure est fini ou non = Défaite")
           number_of_consecutive_victories = 0
           lvl_life -= opponent_strength
           defeat_nbr += 1
           print(f"Vie : {lvl_life}")
            
            
            
   elif option_menu == 2:
       input(
           "Pour vaincre, il faut obtenir un résultat supérieur\n"
           "à la force de l’adversaire lors du jet de dés.\n"
           "Si l'usager gagne, son niveau de vie augmente.\n"
           "S'il perd, il diminue.\n"
           "La partie finit quand il tombe à 0.\n"
           "Il peut combattre ou éviter mais cela lui"
           "coute 1 point de vie.\n")
         
         
         
   elif option_menu == 3:
       lvl_life -= 1
       print(" - une vie\n"
             f"Vie : {lvl_life}")
   
       rule_show = True
      
      
      
   else:
       game_loop = False

         
         
   if victoire_strength_monster == 3:
       strength_monster = True
       victoire_strength_monster = 0

      
      
   if lvl_life <= 0:
       print(f"C'est la fin de l'aventure {victory_nbr} ")
       game_loop = False
