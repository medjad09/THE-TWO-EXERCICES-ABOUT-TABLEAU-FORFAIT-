def sousTableau(tab, index1, index2):
    sous_tab = []
    for i in range(index1, index2 + 1):
        sous_tab.append(tab[i])
    return sous_tab
def saisirTableau():
    tab = []
    for i in range(10):
        element = int(input(f"Entrez l'élément {i + 1} : "))
        tab.append(element)
    return tab
while True:
    Tab = saisirTableau()
    index1 = int(input("Entrez le premier index : "))
    index2 = int(input("Entrez le deuxième index : "))
    if index1 > index2:
        print("ERROR.")
        continue
    resultat = sousTableau(Tab, index1, index2)
    if resultat:
        print("Le nouveau tableau est :", resultat)
    else:
        print("ERROR.")
    reponse = input("Voulez-vous saisir une nouvelle liste ? (O/N) : ").upper()
    if reponse != 'O':
        break
