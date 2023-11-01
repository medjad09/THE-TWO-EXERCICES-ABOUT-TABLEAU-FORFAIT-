def abonnement(m):
    t = []
    t.append(m*2)
    a1 = m - 30
    if a1 >= 0 :
        b1 = 20 + a1 * 1.5
        t.append(b1)
    else :
        t.append(20)
    a2 = m - 60
    if a2 >= 0 :
        b2 = 50 + a2 * 1
        t.append(b2)
    else :
        t.append(50)
    a3 = m - 120
    if a3 >= 0 :
        b3 = 100 + a3 * 0.5
        t.append(b3)
    else :
        t.append(100)
    return t
m = int(input("entrer le nombre d'heurs :"))
a = int(input("entrer le nombre de minutes :"))
m = m * 60 + a
print("Les 4 plans est :")
t = abonnement(m)
T2 = [0,20,50,100]
for i in range (4):
    print("Le plan ",i+1," à un montant de ",t[i],"MAD","si vous vous abonnez à un montant de :",T2[i],"MAD")
for i in range(4):
    for j in range(i+1,4):
        if t[j] < t[i]:
            min = t[j]
print("l’offre la plus intéressante :",min,"MAD")
print("vous payez 200DH et vous beneficiez d'un temps de communication infini")