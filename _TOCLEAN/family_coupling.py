""" Associate one member of each family with another without having two member
of the same family together.

Source :
https://www.reddit.com/r/france/comments/7gfznv/un_tirage_au_sort_avec_limitations_en_python/
"""

from random import sample
from typing import List, Dict, Tuple
from pprint import pprint


FAMILIES = [("Hervé", "Corinne"),
            ("Thierry", "Nadine", "Lucas", "Alex", "Clara"),
            ("Mumu", "Léo", "Marin"),
            ("Sylvie", "Vincent", "Benjamin", "Juju"),
            ("Sandrine", "Mélu")]


def try_again(func):
    """ Decorator retrying everytime the script fail. """
    def wrapper(*args, **kwaargs):
        resultat = None
        while resultat is None:
            try:
                resultat = func(*args, **kwaargs)
            except ValueError:
                pass
        return resultat
    return wrapper


def main():
    global FAMILIES

    couples = family_coupling(FAMILIES)
    pprint(couples)


@try_again
def family_coupling(families: List[Tuple[str]]) -> Dict[str, str]:
    couples = dict()
    for family in families:
        for member in family:
            member2 = choose_member(families, couples.values(), family)
            couples[member] = member2
    return couples


def choose_member(families: List[Tuple[str]], already_choses: List[str],
                  current_family: Tuple[str]) -> str:
    """ Chose randomly a family member which has not already been chosed. """
    # Building the set of all members from all families
    everybody = set()
    for family in families:
        for member in family:
            everybody.add(member)

    # We delete the family members and the people already coupled
    everybody -= set(already_choses)
    everybody -= set(current_family)

    return sample(everybody, 1)[0]


if __name__ == '__main__':
    main()
