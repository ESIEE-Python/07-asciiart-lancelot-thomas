"""Permet d'encoder une chaine ascii"""
#### Imports et définition des variables globales


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée 
    en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # votre code ici
    encode = []
    cmpt = 1
    for i in range(1, len(s)+1):
        if i == len(s):
            encode.append((s[i-1], cmpt))
            break
        if s[i] == s[i-1]:
            cmpt += 1
        else :
            encode.append((s[i-1], cmpt))
            cmpt = 1
    return encode


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici

    # cas de base
    # recherche nombre de caractères identiques au premier
    # appel récursif

    if len(s) > 250 :
        s1 = artcode_r(s[:250])
        s2 = artcode_r(s[250:])
        if s1 and s2 and s1[-1][0] == s2[0][0]:
            s1[-1] = (s1[-1][0], s1[-1][1] + s2[0][1])
            s2 = s2[1:]
        return s1 + s2

    if s == "":
        return []
    if len(s) == 1:
        return [(s, 1)]
    encode = artcode_r(s[1:])
    if encode[0][0] == s[0]:
        return [(s[0], encode[0][1]+1)] + encode[1:]

    return [(s[0], 1)] + encode

#### Fonction principale


def main():
    """
    main appelant les fonctions d'encodage
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
