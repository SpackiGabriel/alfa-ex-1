def group_by(key_func, data):
    """
    Groups the items in the given data based on the result of the key function.

    Args:
        key_func (function): A function that takes an item from the data and returns a key.
        data (iterable): The data to be grouped.

    Returns:
        dict: A dictionary where the keys are the result of the key function and the values are lists of items that have the same key.
    """
    grouped_data = {}
    for item in data:
        key = key_func(item)
        if key not in grouped_data:
            grouped_data[key] = []
        grouped_data[key].append(item)
    return grouped_data

def count_by(data):
    """
    Counts the number of values for each key in the given data dictionary.

    Args:
        data (dict): A dictionary containing keys and values.

    Returns:
        dict: A dictionary where the keys are the same as the input data dictionary,
              and the values are the counts of the corresponding values in the input data.
    """
    counted_data = {}
    for key, values in data.items():
        counted_data[key] = len(values)
    return counted_data
