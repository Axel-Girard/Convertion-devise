import networkx as nx

# Récupération de trois valeurs  d'une lignes séparées par des ;
def recuperation_valeurs(ligne):
    vals = ligne.split(';')
    if len(vals) != 3:
        return None
    else:
        return vals[0], vals[1], vals[2]

# Permet de savoir si le noeud existe dans le graph
def trouver_noeud(graph, noeud):
    for liaison in graph:
        if noeud in liaison:
            return True
    return False

# lecture du fichier
fichier = open("test.txt", "r")
# suppression des \n
strip= [ligne.strip('\n\r') for ligne in fichier.readlines()]
#initialisation des variables
compteur = 0
depart = ""
fin = ""
montant = 0
graph = nx.DiGraph()
# on parcours les lignes du fichier
for ligne in strip:
    # Récupération des valeurs de la lignes
    val = recuperation_valeurs(ligne)
    if ligne and val:
        compteur += 1
        if compteur == 1:
            depart = val[0]
            fin = val[2]
            montant = float(val[1].rstrip())
        else:
            try:
                # verification que le taux est un chiffre
                taux = float(val[2].rstrip())
                # ajout dans le graph de la liaison directionnelle dans les deux sens
                graph.add_edge(val[0], val[1], weight=taux)
                graph.add_edge(val[1], val[0], weight=1/taux)
            except ValueError:
                print (val[2], ' n\'est pas un chiffre.')
fichier.close()

if not(trouver_noeud(graph, depart) and trouver_noeud(graph, fin)):
    print ('Il n\'y a pas de convertion pour ses devises.')
else:
    resultat = 1
    if not(resultat):
        print ('Il n\'y a pas de convertion pour ses devises.')
    else:
        try:
            # utilisation de l'algorithme de dijkstra pour trouver le plus court chemin d'un graph
            nodes = nx.dijkstra_path(graph,"EUR","USD")
            for cptNodes in range(len(nodes) -1):
                # calcul du montant pour chaque liaison
                taux = float(graph[nodes[cptNodes]][nodes[cptNodes + 1]]['weight'])
                montant = montant * taux
            print('%.2f' % montant)
        except nx.NetworkXNoPath:
            print ('Il n\'y a pas de convertion pour ses devises.')
