def linear_search(list, key):

    for i, item in enumerate(list):
        if item == key:
            return i
    return -1