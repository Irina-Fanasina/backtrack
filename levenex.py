alphabet = ['a','b','d','e','f','g','h','i','j',
            'k','l','m','n','o','p','r','s',
            't','v','y','z']

def voisins(mot):

    resultat = set()

    # Suppression
    for i in range(len(mot)):
        resultat.add(mot[:i] + mot[i+1:])

    # Insertion
    for i in range(len(mot)+1):
        for c in alphabet:
            resultat.add(mot[:i] + c + mot[i:])

    # Substitution
    for i in range(len(mot)):
        for c in alphabet:
            if c != mot[i]:
                resultat.add(mot[:i] + c + mot[i+1:])

    return resultat


def enumeration(M, k):

    mots = {M}
    frontiere = {M}

    for _ in range(k):

        nouveaux = set()

        for mot in frontiere:
            nouveaux.update(voisins(mot))

        mots.update(nouveaux)
        frontiere = nouveaux

    return mots


M = "vato"
k = 2

resultat = enumeration(M, k)

print("Nombre de mots :", len(resultat))
print(resultat)