class Exercice3:
    def __init__(self, capacite):
        self.capacite = capacite
        self.cache = {}
        # pour stocker les cles dans
        self.ordre = []

    def get(self, cle):
        # on met la cle  au debut, a la tete de la pile
        self.ordre.remove(cle)
        self.ordre.append(cle)

        return self.cache[cle]

    def put(self, cle, valeur):
        # on change la position de la cle si elle existe deja
        if cle in self.cache:
            self.cache[cle] = valeur
            self.ordre.remove(cle)
            self.ordre.append(cle)
        else:
            # on insere alors la cle et la valeur
            self.cache[cle] = valeur
            self.ordre.append(cle)

    def free(self):
        for i in self.cache.keys():
            del i