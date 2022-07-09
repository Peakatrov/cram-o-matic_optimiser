from pprint import pprint

from data.game_variables import item_values
from utils.combination_finding import find_combinations_to_hit_target
from utils.item_gathering import create_item_dataframe, list_unique_item_values
from utils.recipe_handling import gather_item_recipes, search_item_recipes


# SET UP
# Instantiate item recipes
all_item_recipes = gather_item_recipes()

# Construct item/value dataframe
item_dataframe = create_item_dataframe()


# USER INPUT
# TODO: upgrade to accept user input for target item
target_item = "Bottle Cap"


# IDENTIFY COMBINATIONS
# Find recipes for target item
target_item_recipes = search_item_recipes(all_item_recipes, target_item)

for recipe in target_item_recipes.recipes:
    target_item_range = recipe.value_range

    # Find all possible combinations
    unfiltered_combinations = find_combinations_to_hit_target(
        item_values,
        target_item_range,
    )

    print(f"Printing all {len(unfiltered_combinations)} combinations to reach {target_item} target:")
    pprint(unfiltered_combinations)


# OPTIMISE
