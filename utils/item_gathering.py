from pandas import read_csv


# TODO: remove dataframe usage for speed
def create_item_dataframe(item_csv_filepath="data/cram_o_matic_items.csv"):
    item_dataframe = read_csv(item_csv_filepath)
    item_dataframe["Value"].astype(int)
    return item_dataframe


def list_unique_item_values(item_dataframe):
    # Pull dataframe column into set
    item_value_set = set(item_dataframe["Value"])
    return list(item_value_set)


def list_unique_item_types(item_dataframe):
    # Pull dataframe column into set
    item_type_set = set(item_dataframe["Type"])
    return list(item_type_set)