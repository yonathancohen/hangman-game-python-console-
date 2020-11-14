"""Ici, on va definir toutes les variables que l'on va utiliser dans notre jeu de pendu"""

nombre_tentatives = 8

liste_mots = ['ANGLE', 'ARMOIRE', 'BANC', 'BUREAU', 'CABINET', 'CARREAU', 'CHAISE', 'CLASSE', 'CLEF', 'COIN', 'COULOIR', 'DOSSIER', 'EAU',
'ECOLE', 'ENTRER', 'ESCALIER', 'ETAGERE']

regles_du_jeu ="				LE PENDU\n\nBonjour, voici les regles: \n\nL'algorithme va generer un mot et vous allez essayer de le trouver.\n\
Si vous donnez 8 fausses lettres ou faux mots, vous avez perdu et votre score est 0.\n\
Si vous trouvez le mot avant d'avoir epuise vos chances, chaque coup restant vous rapportera 1 point.\n\n\
Au bout de 3 manches, vous aurez votre score final.\n\n\n"

score = dict()