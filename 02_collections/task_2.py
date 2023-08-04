import random


# container for created random dicts
list_of_dicts = []

# create random dicts
for i in range(random.randint(2, 10)):
    # create random number of keys (3-15 keys)
    elementary_dict = {}
    for j in range(random.randint(3, 15)):
        # to get letters in lower case use unicode codes of letters a-z: 97-122
        elementary_dict[chr(random.randint(97, 122))] = random.randint(0, 100)
    # append items to each created above dict
    list_of_dicts.append(elementary_dict)

# get unique keys that present in all created before dicts
# for this purpose use set() to avoid duplicates of keys from different dicts
set_of_keys = set()

for elem in list_of_dicts:
    set_of_keys = set_of_keys.union(elem.keys())

# prepare staging dict where all keys and their values are collected in one dict
# format unique key: list of value
staging_dict = {}

for key in set_of_keys:
    key_values = []
    for list in list_of_dicts:
        if key in list:
            key_values.append(list[key])
    staging_dict[key] = key_values

# prepare result dict where considered the following condition:
# if key has only one value -> dict[key] = value
# if key has 2 or more values -> dict[key_{number of list where max(value) contains}] = max(value)
result_dict = {}

for (key, value) in staging_dict.items():
    if len(value) > 1:
        result_dict[f'{key}_{value.index(max(value)) + 1}'] = max(value)
    else:
        result_dict[key] = value[0]

# alternative method
# result_dict2 = {(f'{key}_{value.index(max(value))+1}' if len(value)>1 else key): (max(value) if len(value)>1 \
#                 else value[0]) for (key,value) in staging_dict.items()}

print(result_dict)
# print(result_dict2)
