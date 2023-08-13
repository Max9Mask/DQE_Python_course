import random
from typing import List, Dict, Set


# function that creates random dicts
def get_random_dict(qty: List, length: List) -> List:
    # container for created random dicts
    output_list_of_dicts = []
    for i in range(random.randint(*qty)):
        # create random number of keys (3-15 keys)
        elementary_dict = {}
        for j in range(random.randint(*length)):
            # to get letters in lower case use unicode codes of letters a-z: 97-122
            elementary_dict[chr(random.randint(97, 122))] = random.randint(0, 100)
        # append items to each created above dict
        output_list_of_dicts.append(elementary_dict)
    return output_list_of_dicts


list_of_dicts = get_random_dict([2, 10], [3, 15])


# get unique keys that present in all created before dicts
# for this purpose use set() to avoid duplicates of keys from different dicts
def get_set_of_keys(input_dict: List) -> Set:
    output_set = set()

    for elem in input_dict:
        output_set = output_set.union(elem.keys())

    return output_set


set_of_keys = get_set_of_keys(list_of_dicts)


# prepare staging dict where all keys and their values are collected in one dict
# format unique key: list of value
def get_staging_dict(input_set: Set, input_list_dict: List) -> Dict:

    output_staging_dict = {}

    for key in input_set:
        key_values = []
        for dict_elem in input_list_dict:
            if key in dict_elem:
                key_values.append(dict_elem[key])
            else:
                key_values.append(0)
        output_staging_dict[key] = key_values

    return output_staging_dict


staging_dict = get_staging_dict(set_of_keys, list_of_dicts)


# prepare result dict where considered the following condition:
# if key has only one value -> dict[key] = value
# if key has 2 or more values -> dict[key_{number of list where max(value) contains}] = max(value)
def get_result(input_dict: Dict) -> Dict:
    result_dict = {}

    for (key, value) in staging_dict.items():
        # for keys that have more than 1 value
        if sum(value) != max(value):
            result_dict[f'{key}_{value.index(max(value)) + 1}'] = max(value)
        else:
            result_dict[key] = max(value)

    return result_dict
