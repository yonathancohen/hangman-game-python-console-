from donnees_pendu import *
from fonctions_pendu import *

afficher_regles_du_jeu()		# affiche les regles du jeu

nom_utilisateur = entrez_nom()	# on enregistre dans une variable nom_utilisateur la valeur retournee par la fonction qui demande a rentrer le nom
score[nom_utilisateur] = 0		# on initialise le score de l'utilisateur a zero (on s'embete pas avec les histoire de conserver les scores)

count=0							# ce compteur va nous permettre de jouer trois manches
i=1								# ce compteur est utilise pour indiquer le numero de la manche qui va etre jouee
while count < 3:				# boucle qui va permettre de jouer des manches tant qu'on en a fait moins de 3
	mot_genere = mot_choisi()	# on enregistre dans une variable le mot genere aleatoirement depuis notre liste de mots

	mot_a_trouver = afficher_premiere_lettre(mot_genere) + afficher_caracteres_partiels(mot_genere) + afficher_derniere_lettre(mot_genere)	# on enregistre dans une variable le mot incomplet qui contient juste la premiere et la derniere lettre avec au milieu le symbole " _ "
	mot_partiel_caracteres = afficher_caracteres_partiels(mot_genere)																		# on enregistre dans une variable les caracteres " _ " qu'il y a dans notre mot a trouver au depart
	mot_partiel_lettres = mot_genere_sans_premiere_et_derniere_lettre(mot_genere)															# on enregistre dans une variable les lettres du mot genere sans compter la premiere et la derniere lettre

	lettres_justes = []		# on cree une liste vide dans laquelle on va ajouter toutes les lettres justes trouvees

	nombre_tentatives = 8	# on initialise le nombre de chances a 8 pour trouver des lettres ou le mot
	while mot_a_trouver != mot_genere and nombre_tentatives>0:	# boucle qui va permettre de repeter le processus de trouvage de lettre ou du mot correct tant qu'il reste des chances et d'afficher a chaque fois le mot partiel
		print(mot_a_trouver)	# affiche le mot sous la forme E _ _ _ _ _ _ T
		lettre_choisie = donnez_lettre_mot()	# on enregistre dans une variable la lettre qui va etre donnee par l'utilisateur

		if lettre_choisie == mot_genere:		# si cette lettre n'est en fait pas une lettre mais plutot le mot que l'on veut trouver
			score[nom_utilisateur] += nombre_tentatives		# on ajoute au score le nombre de tentatives restantes
			print("\nGood Job, you found the word !! your temporary score: ", score[nom_utilisateur], "\n")		# et on affiche : ...
			i+=1		# cette indentation de i permet d'enregistrer que l'on joue la 2e ou 3e manche
			count += 1	# cette indentation de count permet de jouer encore une manche si on en a pas fait 3. Je suis conscient qu'on aurait pu se passer de i ou de count et utiliser deux fois la meme variable pour les deux fonctionnalites, mais chai pas, pas la force de revenir dans le code pour arranger ca. On aurait gagne 3 ou 4 lignes
			if count == 3:	# si count = 3 on sort de cette boucle et on ne repetera pas le while qui precede celui dans lequel on se trouve.
				break
			else:
				print("\n\nC'est parti pour la " + str(i) +"e manche:\n\n")		# sinon, on annonce le numero de la prochaine manche et on sort de ce while pour lancer une prochaine manche
			break
		elif len(lettre_choisie) != 1 and len(lettre_choisie) != len(mot_genere):	# sinon, si on entre une saisie qui n'est ni une lettre ni un mot de la taille du mot a trouver. On annonce que la saisie est incorrecte et il donne une autre lettre ou mot
			print("Votre saisie n'est pas correcte, recommencez !")
		elif lettre_choisie in lettres_justes:		# si la lettre a deja ete trouvee, on lui demande de resaisir une lettre
			print("Vous avez deja trouve cette lettre !")
		elif lettre_choisie in mot_partiel_lettres:		# si la lettre fait partie des lettres a trouver, on ajoute cette lettre a la liste lettres justes qui etait initialisee vide et on indique que la lettre est une bonne lettre
			lettres_justes.append(lettre_choisie)
			print("Bonne lettre: ", lettre_choisie)
		else:
			nombre_tentatives -= 1		# sinon, la lettre est fausse et il perd une chance
			if nombre_tentatives == 0:	# si il n'a plus de chances on sort de ce while et on n'y re rentre plus car c'est un tnai pour repeter la saisie de lettre que le nombre de chances soit superieur a zero
				break
			else:
				print("Rate ! Il te reste ", nombre_tentatives, " chances\n")	# sinon on lui indique le nombre de chances qu'il lui reste
		mot_a_trouver = afficher_premiere_lettre(mot_genere) + " " + recup_mot_masque(mot_genere_sans_premiere_et_derniere_lettre(mot_genere), lettres_justes) + " " + afficher_derniere_lettre(mot_genere)		# on affiche le mot partiel mis a jour
		if mot_a_trouver.replace(" ", "") == mot_genere:	# si le mot partiel duquel on enleve les espaces est egal au mot genere, on affiche le mot a trouver et on lui donne la valeur du mot genere donc on ne rentrera plus dans le while de la saisie de lettre car le mot a ete trouve
			print("\n" + mot_a_trouver)
			mot_a_trouver = mot_genere

	if mot_genere == mot_a_trouver:		# si on est rentre dans le tout dernier if, on arrive dans ce if juste apres et on annonce que la manche a ete gagnee et si cetait la 3e manche on sarrete et on donne le score final. C'est fini. Sinon, on lance la manche suivante
		score[nom_utilisateur] += nombre_tentatives
		print("\nBRAVO, vous avez trouve le mot ! Votre score partiel: ", score[nom_utilisateur], " points\n")
		i+=1
		count += 1
		if count == 3:
			break
		else:
			print("\n\nC'est parti pour la " + str(i) +"e manche:\n\n")

	elif nombre_tentatives == 0:
		print("\nPENDU !! Le mot etait " + mot_genere + "\n" + "C'est fini, vous avez perdu. Votre score partiel est: 0 et votre score cumule est:", score[nom_utilisateur])
		i+=1
		count += 1
		if count == 3:
			break
		else:
			print("\n\nC'est parti pour la " + str(i) +"e manche:\n\n")

print("\n\nVOTRE SCORE FINAL EST: ", score[nom_utilisateur], " ! Comparez le avec celui d'un pote ...\n\n")
