def group_by(key_func, data):
    grouped_data = {}
    for item in data:
        key = key_func(item)
        if key not in grouped_data:
            grouped_data[key] = []
        grouped_data[key].append(item)
    return grouped_data

def count_by(data):
    counted_data = {}
    for key, values in data.items():
        counted_data[key] = len(values)
    return counted_data
