import networkx as nx
import matplotlib.pyplot as plt
import random

print("=======================================================")

valide1 = False

while valide1 != True:

    rep0 = input("Donner la Taille du labyrinthe : ")
    Taille = int(rep0)

    if(Taille >= 1 and Taille <=50): valide1 = True
    else:
        print("")
        print("*********************************************************")
        print("La taille doit etre une donner valide plus petit que 51 et plus grand que 0!")
        print("*********************************************************")
        print("")

print("-----------------------------")
print("Donner la position du point de depart et d'arrivée ( entre 1 et",Taille-1,")")
print("-----------------------------")

valide2 = False

while valide2 != True:

    rep1 = input("Donner le point de debut : ")
    print("-----------------------------")
    rep2 = input("Donner le point d'arrivée : ")
    print("-----------------------------")

    departY = int(rep1)
    arriveY = int(rep2)

    if ((departY >= 0 and departY <= Taille - 1)and(arriveY >= 0 and arriveY <= Taille - 1)):
        valide2 = True
    else:
        print("")
        print("*********************************************************")
        print("Vous devez donner une coordonnée valide entre 0 et ", Taille - 1)
        print("*********************************************************")
        print("")
        valide2 = False
print("=======================================================")


G = nx.grid_2d_graph(Taille, Taille)
pos = dict((n,n) for n in G.nodes())

for u, v in G.edges():
    G[u][v]['weight'] = random.random() 

T = nx.minimum_spanning_tree(G)

depart = (0, departY)
arrive = (Taille-1, arriveY)

chemin = nx.shortest_path(T, source= depart, target= arrive)

aretes_chemin = list(zip(chemin, chemin[1:]))

print("Chemin trouvé ! Longueur :", len(chemin), "cases.")
aretes_chemin = list(zip(chemin, chemin[1:]))


plt.figure(figsize=(12, 12), facecolor="black")
ax = plt.gca()
ax.set_facecolor("black")


nx.draw_networkx_edges(T, pos, edge_color='white', width= int(300 / Taille))

nx.draw_networkx_edges(T, pos, edgelist=aretes_chemin,edge_color='red', width=3)

nx.draw_networkx_nodes(T, pos, nodelist=[(0,departY)], node_color='lime', node_size=100)
nx.draw_networkx_nodes(T, pos, nodelist=[(Taille-1, arriveY)], node_color='red', node_size=100)

plt.title("Labyrinthe", color="white")

plt.show()
