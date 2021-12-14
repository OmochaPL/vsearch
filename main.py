def search_for_vowels(phrase: str):
    """Zwraca samogłoski znalezione w frazie podanej jako argument"""
    vowels = set('aioue')
    return vowels.intersection(set(phrase))

def search_for_letters(phrase: str, letters: str):
    '''Zwraca zbiór liter ze zmiennej letters znalezionych w zmiennej phrase'''
    return set(letters).intersection(set(phrase))
