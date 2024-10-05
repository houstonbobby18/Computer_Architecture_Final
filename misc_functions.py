def get_fruit_index_names(fruit_index_document = 'fruit_indexes.txt'):
    fruit_index_name = []
    with open(fruit_index_document, 'r') as f:
        for line in f:
            fruit_index_name.append(line.strip())
    return fruit_index_name