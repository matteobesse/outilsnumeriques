import random

#1. Paramètres du jeu
TAILLE = 5
ESSAIS_MAX = 10

#2. Création de la grille (liste de listes)
# "_" = case vide, "O" = tir raté, "X" = bateau coulé
grille = [["_"] * TAILLE for _ in range(TAILLE)]

#3. Position aléatoire du bateau
bateau_ligne = random.randint(0, TAILLE - 1)
bateau_colonne = random.randint(0, TAILLE - 1)

# (pour tester : décommenter pour tricher)
# print(f"DEBUG: Bateau en {bateau_ligne + 1}, {bateau_colonne + 1}")

print("=== 🚢 BATAILLE NAVALE 5x5 ===")
print("Tu as 10 essais pour couler le bateau !")

#Fonction pour afficher la grille
def afficher_grille():
    print("\n  ", " ".join([str(i+1) for i in range(TAILLE)]))  # numéros de colonnes
    for i, ligne in enumerate(grille):
        print(f"{i+1} {' '.join(ligne)}")

#4. Boucle de jeu
essais_restants = ESSAIS_MAX

while essais_restants > 0:
    afficher_grille()
    print(f"\nEssais restants : {essais_restants}")
    
    try:
        ligne = int(input("Ligne (1-5) : ")) - 1
        colonne = int(input("Colonne (1-5) : ")) - 1
    except ValueError:
        print("⚠️ Entrez des nombres valides !")
        continue
    
    #Vérifie la validité du tir
    if not (0 <= ligne < TAILLE and 0 <= colonne < TAILLE):
        print("❌ En dehors de la grille !")
        continue
    
    #Vérifie si déjà tiré ici
    if grille[ligne][colonne] != "_":
        print("⚠️ Tu as déjà tiré sur cette case !")
        continue
    
    #Vérifie si touché
    if ligne == bateau_ligne and colonne == bateau_colonne:
        print("\n💥 Coulé ! Bravo, tu as gagné !")
        grille[ligne][colonne] = "X"
        afficher_grille()
        break
    else:
        print("🌊 À l'eau !")
        grille[ligne][colonne] = "O"
        essais_restants -= 1

#Fin du jeu
if essais_restants == 0:
    print("\n💣 Tu as perdu ! Le bateau était en ligne", bateau_ligne + 1, "colonne", bateau_colonne + 1)
    grille[bateau_ligne][bateau_colonne] = "X"
    afficher_grille()
