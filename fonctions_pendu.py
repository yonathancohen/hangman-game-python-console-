from donnees_pendu import *
import random

def afficher_regles_du_jeu():				# affiche les regles du jeu
	print(regles_du_jeu)

def entrez_nom():							# demande a l'utilisateur de rentrer son nom et verifie que la saisie est correcte
	nom = input("Veuillez entrer votre NOM puis taper entree: ")
	if len(nom) <= 2:
		print("Votre nom doit contenir au moins 3 lettres !")
		entrez_nom()
	nom = nom.upper()
	return nom

def mot_choisi():								# renvoie un mot choisi aleatoirement parmi la liste de mots contenue dans le fichier donnees
	 b = random.choice(liste_mots)
	 return b

def afficher_premiere_lettre(mot_genere):		# renvoie la premiere lettre du mot genere qui va etre devoilee a l'utilisateur
	a = mot_genere[0]
	return a

def afficher_derniere_lettre(mot_genere):		# renvoie la derniere lettre du mot genere qui va etre devoilee a l'utilisateur
	taille_mot = len(mot_genere)
	a = mot_genere[taille_mot - 1]
	return a

def afficher_caracteres_partiels(mot_genere):	# renvoie " _ " pour chaque lettre a trouver dans le mot
	taille_mot = len(mot_genere)
	a = " _ " *(taille_mot - 2)
	return a

def mot_genere_sans_premiere_et_derniere_lettre(mot_genere):	# Ca renvoie les lettres du mot a trouver (hormis la premiere et la derniere qui vont etre donnees de base
	taille_mot = len(mot_genere)
	a = mot_genere[1:(taille_mot - 1)]
	return a


def donnez_lettre_mot():	#ici on recoit une lettre ou un mot et on verifie si la saisie est correcte ou fausse.
	x=0
	while x==0:
		a = input("\nEntrez une lettre ou un mot: ")
		a = a.upper()
		x=1
		if a.isalpha() == False:
			print("Vous devez ne rentrer qu'une lettre ou un mot! ")
			x=0
		else:
			break
	return a

def recup_mot_masque(mot_partiel, lettre_choisie):	# On definit la fonction la plus compliquee, celle qui remplace le caractere par une lettre dans le mot partiel lorsque la lettre choisie est juste.
					# AN			# A
  
    mot_masque = ""
    for lettre in mot_partiel:			# Pour chaque lettre du mot genere partiel
        if lettre in lettre_choisie:	# Si le lettre du mot genere est egale a la lettre choisie (juste)
            mot_masque += (" " + lettre + " ")		# Le mot masque sera egal a lui meme plus la lettre correcte (avec un espace).
        else:							# Sinon:
            mot_masque += " _ "			# Le mot masque est egal a lui meme plus un caractere inconnu.
    return mot_masque	






