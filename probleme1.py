def lengthOfLastWord(s):
    if s == "":
        return 0

    # on separe au niveau de l'esoace et on a un tableau de tous les mots
    mots = s.split(" ")

    # on  accede au dernier element du tableau
    dernier_mot = mots[-1]
    taille = len(dernier_mot)

    return taille
