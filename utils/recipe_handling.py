import json
from typing import Any, Dict, List, Union
from itertools import chain


class ItemRecipe:
    def __init__(self,
                 value_range: range,
                 required_item_types: Union[bool, List[Union[bool, Any]]] = False,
                 required_items: Union[bool, List[Union[bool, Any]]] = False,
                 likelihood: Union[bool, float] = False
                 ):
        self.value_range = value_range
        self.required_item_types = required_item_types
        self.required_items = required_items
        self.likelihood = likelihood

    @classmethod
    def from_guarantee(
            cls,
            lowest_value,
            highest_value,
            required_item
    ):
        value_range = range(lowest_value, highest_value, 1)
        required_items = [required_item, "Any", required_item, required_item]
        return cls(value_range=value_range, required_items=required_items)

    @classmethod
    def from_type(
            cls,
            highest_value,
            required_item_type,
            likelihood=False
    ):
        value_range = range(highest_value - 9, highest_value, 1)
        required_item_types = [required_item_type, "Any", "Any", "Any"]
        return cls(value_range=value_range, required_item_types=required_item_types, likelihood=likelihood)


class Item:
    def __init__(self, name, recipes):
        self.name = name
        self.recipes = recipes

    def recipes(self):
        return self.recipes

    def print_all_recipes(self):

        print(f"\n---------------------------------------------------")
        print(f"Item: {self.name}\nRecipes: \n")
        for recipe in self.recipes:
            print(f"Value range: {recipe.value_range}")
            if recipe.required_item_types:
                print(f"Required item types: {recipe.required_item_types}\n")
            if recipe.required_items:
                print(f"Required items: {recipe.required_items}\n")
            if recipe.likelihood:
                print(f"Likelihood of occurrence: {recipe.likelihood}\n")


def gather_item_recipes_by_type(recipe_location='data/recipes_by_type.json'):
    recipe_dict = json.load(open(recipe_location))
    # recipe_dict is composed of type:type_dict pairs.
    # Each type_dict holds top_of_range:output_item pairs,
    # where some output_items can be dicts of output_item:likelihood

    item_list = []

    for item_type, tiered_list in recipe_dict.items():
        for highest_value, possible_output_items in tiered_list.items():
            if isinstance(possible_output_items, str):
                item_list.append(
                    Item(
                        name=possible_output_items,
                        recipes=[ItemRecipe.from_type(
                            required_item_type=item_type,
                            highest_value=int(highest_value)
                        )]
                    )
                )

            elif isinstance(possible_output_items, Dict):
                for output_item, likelihood in possible_output_items.items():
                    item_list.append(
                        Item(
                            name=output_item,
                            recipes=[ItemRecipe.from_type(
                                required_item_type=item_type,
                                highest_value=int(highest_value),
                                likelihood=likelihood
                            )]
                        )
                    )

            else:
                raise ValueError(f"Object possible_output_items is of type: {type(possible_output_items)}")

    return item_list


def gather_item_recipes_for_guaranteed(recipe_location='data/recipes_for_guaranteed.json'):
    item_recipe_dict = json.load(open(recipe_location))

    item_list = [
        Item(
            name=item,
            recipes=[ItemRecipe.from_guarantee(**recipe)]
        ) for item, recipe in item_recipe_dict.items()
    ]

    return item_list


def simplify_items(item_list):
    # Expects List of Item objects with a single recipe in self.recipes List
    # Return a single Item with one to multiple recipes in self.recipes List
    if len(item_list) == 1:
        simplified_recipes = item_list[0].recipes
    elif len(item_list) < 1:
        raise ValueError(f"No item_list should have a length less than 1")
    else:
        if not all(item.name == item_list[0].name for item in item_list):
            raise ValueError(f"All items should have consistent self.name, not: {[item.name for item in item_list]}")
        else:
            simplified_recipes = [recipe for recipes in [item.recipes for item in item_list] for recipe in recipes]

    return Item(
        name=item_list[0].name,
        recipes=simplified_recipes
    )


def gather_item_recipes():
    item_list_by_type = gather_item_recipes_by_type()
    item_list_by_guaranteed = gather_item_recipes_for_guaranteed()

    # Restructure data to highlight items by name
    item_dict = {}
    for item in chain(item_list_by_type, item_list_by_guaranteed):
        item_dict.setdefault(item.name, []).append(item)

    # Simplify recipes
    item_dict = {item_name: simplify_items(item_list) for (item_name, item_list) in item_dict.items()}

    return item_dict


def search_item_recipes(recipes: Dict, desired_item):
    if desired_item in recipes.keys():
        return recipes[desired_item]
    else:
        raise ValueError(f"Recipe list contains no recipe for: {desired_item}. Please check spelling")
