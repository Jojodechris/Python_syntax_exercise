def print_upper_words():
    """ turn lower case into upper case"""

list_of_words = ["good","bad","great","jordan","hey","elephant","Eagle"]
for word in list_of_words:
    Word = word.upper()
    print(Word)

   
def print_upper_words2(words):
        """Print each word on sep line, uppercased, if starts with E or e.

        >>> print_upper_words2(["eagle", "Edward", "Alfred"])
        EAGLE
        EDWARD
    """

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


def print_upper_words3(words, must_start_with):
    """Print each word on sep line, uppercased, if starts with one of given

        >>> print_upper_words3(["eagle", "Edward", "Alfred", "zope"],
        ...                   must_start_with=["A", "E"])
        EDWARD
        ALFRED
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break


