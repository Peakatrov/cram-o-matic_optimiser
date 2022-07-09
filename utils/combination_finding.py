from itertools import combinations, combinations_with_replacement
from operator import itemgetter
from typing import List


def find_combinations_to_hit_target(
        potential_numbers: List[int],
        target: int,
        count_of_numbers: int = 4,
        unique_elements=True
) -> List[List[int]]:
    """
    :param potential_numbers:
    :param target:
    :param count_of_numbers:
    :param unique_elements: indicates whether combinations must contain unique elements, or not
    :return:
    """
    confirmed_combinations = set()

    # Create all possible combinations
    if unique_elements:
        possible_combinations = combinations(potential_numbers, count_of_numbers)
    else:
        possible_combinations = combinations_with_replacement(potential_numbers, count_of_numbers)

    # Identify combinations that can add up to
    for i in possible_combinations:
        if sum(i) == target:
            # Turns the tuple of numbers into list of strings
            # Then joins them into a single string
            # This allows hashing for the set
            confirmed_combinations.add(" ".join(sorted(list([str(x) for x in i]))))
        # Splits the strings into lists of ints

    list_of_combinations = list([[int(z) for z in x.split()] for x in confirmed_combinations])

    # Sort each combination into descending order, then sort list of combinations by first element
    list_of_combinations = sorted(
        [sorted(i, reverse=True) for i in list_of_combinations],
        key=itemgetter(0),
        reverse=True
    )

    return list_of_combinations
