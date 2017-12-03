""" Effectue un couplage entre plusieurs familles sans coupler deux membres
d'une même famille.

Source du sujet :
https://www.reddit.com/r/france/comments/7gfznv/un_tirage_au_sort_avec_limitations_en_python/
"""
from random import random, sample
from typing import List, Dict, Tuple
from pprint import pprint


FAMILLES = [("Hervé", "Corinne"),
            ("Thierry", "Nadine", "Lucas", "Alex", "Clara"),
            ("Mumu", "Léo", "Marin"),
            ("Sylvie", "Vincent", "Benjamin", "Juju"),
            ("Sandrine", "Mélu")]


def une_erreur_on_recommence(func):
    """ Un bon decorateur bien sale. Mais qui fait le travail. """
    def wrapper(*args, **kwaargs):
        resultat = None
        while resultat is None:
            try:
                resultat = func(*args, **kwaargs)
            except ValueError:
                pass
        return resultat
    return wrapper


def shuffle(iterable: iter) -> iter:
    """ Shuffle un itérable.
    Fonctionne comme la fonction random.shuffle, mais retourne un résultat au
    lieu de modifier l'itérable sur-place.
    """
    return sorted(iterable, key=lambda k: random())


def choisir_membre(familles: List[Tuple[str]], deja_choisis: List[str],
                   famille_actuelle: Tuple[str]) -> str:
    """ Choisi aléatoirement un membre d'une famille qui n'a pas déjà été
    choisi.
    """
    # Construction de l'ensemble des membres des familles
    tout_le_monde = set()
    for famille in familles:
        for membre in famille:
            tout_le_monde.add(membre)

    # On retire les membres de la famille et les gens déjà choisis
    tout_le_monde -= set(deja_choisis)
    tout_le_monde -= set(famille_actuelle)

    return sample(tout_le_monde, 1)[0]


@une_erreur_on_recommence
def assigner_membres(familles: List[Tuple[str]]) -> Dict[str, str]:
    assignations = dict()
    for famille in familles:
        for membre in famille:
            membre2 = choisir_membre(familles, assignations.values(), famille)
            assignations[membre] = membre2
    return assignations


def main():
    global FAMILLES

    assignations = assigner_membres(FAMILLES)

    pprint(assignations)


if __name__ == '__main__':
    main()
