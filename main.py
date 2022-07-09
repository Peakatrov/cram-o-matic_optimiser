from pprint import pprint

from utils.combination_finding import find_combinations_to_hit_target
from utils.item_gathering import create_item_dataframe, list_unique_item_values


# Construct item/value dataframe
item_dataframe = create_item_dataframe()

# Pull list of item values
item_value_list = list_unique_item_values(item_dataframe)

# Pick target
bottle_cap_target = 142
bottle_cap_range = range(141, 150, 1)

# Find all possible combinations
bottle_cap_combos = find_combinations_to_hit_target(
    item_value_list,
    bottle_cap_target,
    unique_elements=False
)

print(f"Printing all {len(bottle_cap_combos)} combinations to reach Bottle Cap target:")
pprint(bottle_cap_combos)

