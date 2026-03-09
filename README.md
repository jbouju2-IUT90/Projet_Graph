# Projet_Graph
BOUJU Jarod S2 A1 \n
Theme : **labyrinthe**


# Concepts :
Ce projet de graphe consiste à générer un labyrinthe aléatoire. L'utilisateur peut fournir plusieurs paramètres comme la taille du labyrinthe, le point de début et le point de fin.
Quand tout est paramétré, on peut donc avoir un affichage d'un chemin qui se dessine entre les deux points entrés par l'utilisateur.

**Etape 1 : Création du terrain (page ~22 à ~32)**
Dans un premier temps, j'ai créé une grille pour pouvoir créer les fondations du labyrinthe.
J'ai utilisé la *commande nx.grid_2d_graph(Taille, Taille)*. Grâce à la variable Taille, je peux donc choisir les dimensions du labyrinthe. J'ai préféré garder une seule variable pour les deux dimensions car je me suis dit qu'un carré rendrait mieux à l'affichage.

**Etape 2 : Spanning Tree (page 165)**
Maintenant que j'ai la base, il faut que je crée un chemin. Pour cela, j'ai utilisé l'algorithme de l'arbre couvrant (spanning tree) qui, comme son nom l'indique, permet dans mon cas de créer un chemin sans boucle, à l'image des branches d'un arbre.

Donc, dans un premier temps, pour que tous les murs de mon labyrinthe ne soient pas fermés, j'attribue un poids aléatoire à chaque arête de la grille avec la commande *G[u][v]['weight'] = random.random()*.
Ensuite, j'utilise la fonction *nx.minimum_spanning_tree(G)* pour créer mon labyrinthe en lui donnant le poids minimum. En effet, avec des murs générés de façon totalement aléatoire, il n'y a aucune garantie d'avoir un chemin praticable à chaque création du graphe (c'est même très rare).
Grâce à la fonction *nx.minimum_spanning_tree(G)*, l'algorithme détruit stratégiquement des murs pour garantir que toutes les cases soient accessibles sans créer de boucle. Avec cette méthode, je n'ai donc pas besoin de faire de boucle complexe basée sur l'aléatoire pour créer un labyrinthe avec un chemin garanti et fonctionnel.

**Etape 3 : Résolution et Affichage (Le plus court chemin)**
Une fois le labyrinthe parfaitement généré, il me reste à trouver la solution pour aller du point de départ au point d'arrivée que l'utilisateur a choisis.

Pour ça, je me suis servi du principe de recherche du plus court chemin (shortest path). J'utilise la commande *nx.shortest_path(T, source=depart, target=arrive)*. Cette fonction va analyser mon arbre et calculer automatiquement l'itinéraire exact pour relier l'entrée à la sortie. Je convertis ensuite ce résultat en une liste d'arêtes (aretes_chemin) pour pouvoir tracer des lignes continues.

Je dessine d'abord toute la structure de mon arbre T avec des traits blancs épais pour faire les murs et les couloirs du labyrinthe.

Je dessine par-dessus uniquement la liste aretes_chemin avec un trait rouge plus fin pour tracer la solution.

Je rajoute deux gros point de couleur (un vert et un rouge) pour bien marquer visuellement le départ et l'arrivée.
