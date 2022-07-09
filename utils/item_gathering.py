import math

from pandas import read_csv


def create_item_dataframe(item_csv_filepath="data/cram_o_matic_items.csv"):
    return read_csv(item_csv_filepath)


def list_unique_item_values(item_dataframe):
    # Pull dataframe column into set, and drop any NaN values
    item_value_set = set(filter(lambda x: x == x, item_dataframe["Value"]))

    # Remove convert set of floats into list of ints
    # WARNING - floor() converts each float element into the closest int no larger than the input
    item_value_list = [
        math.floor(num) for num in list(item_value_set)
    ]

    return item_value_list
