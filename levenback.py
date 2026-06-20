alphabet = ['a','b','d','e','f','g','h','i','j','k',
            'l','m','n','o','p','r','s','t','v','y','z']

def generer_mots(M, k):
    solutions = set()

    def backtrack(i, mot, cout):
        if cout > k:
            return

        # Fin du mot de référence
        if i == len(M):
            solutions.add(mot)

            # Insertion éventuelle de caractères restants
            if cout < k:
                for c in alphabet:
                    backtrack(i, mot + c, cout + 1)
            return

        # 1. Conservation
        backtrack(i + 1, mot + M[i], cout)

        # 2. Substitution
        if cout < k:
            for c in alphabet:
                if c != M[i]:
                    backtrack(i + 1, mot + c, cout + 1)

        # 3. Suppression
        if cout < k:
            backtrack(i + 1, mot, cout + 1)

        # 4. Insertion
        if cout < k:
            for c in alphabet:
                backtrack(i, mot + c, cout + 1)

    backtrack(0, "", 0)
    return solutions


# Exemple
M = "vato"
k = 2

resultat = generer_mots(M, k)

print("Nombre de mots :", len(resultat))
for mot in sorted(list(resultat))[:50]:
    print(mot)