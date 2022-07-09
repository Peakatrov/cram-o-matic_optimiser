from typing import List
from itertools import islice

from recipe_handling import ItemRecipe


def confirm_recipe_eligibility(
    item_recipe: ItemRecipe,
    chosen_items: List[str],
    chosen_item_weights: List[int],
    chosen_item_types: List[str]
):
    # Check types
    assert(isinstance(item_recipe, ItemRecipe))
    assert(isinstance(chosen_items, List) and len(chosen_items) == 4)
    assert(isinstance(chosen_item_weights, List) and len(chosen_items) == 4)

    # Check weights sum to be within range
    assert(sum(chosen_item_weights) in item_recipe.value_range)

    # Check chosen items match first item type
    if item_recipe.required_first_type:
        assert(chosen_item_types[0] in item_recipe.required_first_type)

    # Check chosen items contain 3x required item
    if item_recipe.required_item:
        assert(
            check_n_occurrences_in_list(chosen_items, item_recipe.required_item, 3)
        )

    return True


def check_n_occurrences_in_list(checking_list, desired_entry, n_occurrences):
    generator = (True for entry in checking_list if entry == desired_entry)
    return next(islice(generator, n_occurrences-1, None), False)