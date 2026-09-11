import random
from random import randint


#from tests.test_wave_01 import LETTER_POOL

def draw_letters():
    """Draws 10 random letters and returns them as a hand."""

    LETTER_POOL = {
        'A': 9,
        'B': 2,
        'C': 2,
        'D': 4,
        'E': 12,
        'F': 2,
        'G': 3,
        'H': 2,
        'I': 9,
        'J': 1,
        'K': 1,
        'L': 4,
        'M': 2,
        'N': 6,
        'O': 8,
        'P': 2,
        'Q': 1,
        'R': 6,
        'S': 4,
        'T': 6,
        'U': 4,
        'V': 2,
        'W': 2,
        'X': 1,
        'Y': 2,
        'Z': 1
    }

    letters = [
       letter 
       for letter,count in LETTER_POOL.items() 
       for _ in range(count)
    ]
    n = 0
    letter_hand =[]

    while n < 10:
        random_index = random.randint(0, len(letters) - 1)
        letter_hand.append(letters.pop(random_index))
        n += 1
    return letter_hand


def uses_available_letters(word, letter_bank):
    """Checks whether a word can be made using the available letters."""

    word = word.upper()
    count_dict = {}

    for char in word:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    for letter in letter_bank:
        if letter in count_dict:
            count_dict[letter] -= 1

    return all(count == 0 for count in count_dict.values())


def score_word(word):
    """Calculates and returns the score of a word."""

    score_dict = {
        "A": 1,
        "B": 3,
        "C": 3,
        "D": 2,
        "E": 1,
        "F": 4,
        "G": 2,
        "H": 4,
        "I": 1,
        "J": 8,
        "K": 5,
        "L": 1,
        "M": 3,
        "N": 1,
        "O": 1,
        "P": 3,
        "Q": 10,
        "R": 1,
        "S": 1,
        "T": 1,
        "U": 1,
        "V": 4,
        "W": 4,
        "X": 8,
        "Y": 4,
        "Z": 10
    }

    word = word.upper()
    total_score = 0

    if 7 <= len(word) <= 10:
        total_score += 8

    for char in word:
        score = score_dict[char]
        total_score += score

    return total_score



def get_highest_word_score(word_list):
    """Finds the highest-scoring word and returns it with its score."""

    max_score = float("-inf")
    max_word = ""

    for word in word_list:
        score = score_word(word)

        if score > max_score:
            max_score = score
            max_word = word

        elif score == max_score:
            if len(word) == 10 and len(max_word) != 10:
                max_word = word
            elif len(word) != 10 and len(max_word) != 10:
                if len(word) < len(max_word):
                    max_word = word

    return (max_word, max_score)

draw_letters()