"""
Current Objective: change map from minterms

samplemap = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]

"""


def displaymap(kmap):
    """

    :param kmap: 2D list of kmap values
    :return: null
    """

    for i in kmap:
        print("-" * 17)
        print('| ', end='')
        for j in i:
            print(j, end=' | ')
        print('')
    print("-" * 17)


def reset():
    return [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]


def indices():
    """
    Returns the index of a kmap cell

    :return: indices of kmap cells
    """
    return [[0, 1, 3, 2], [4, 5, 7, 6], [12, 13, 15, 14], [8, 9, 11, 10]]


def ass_minterms(kmap, minterm_list):
    """
    Assigning values to cells in the kmap according to the given minterms

    :param kmap: Unassigned 2D list of kmap values
    :param minterm_list: list of minterms to be assigned
    :return: modified kmap
    """

    cell_index = indices()
    for i in minterm_list:

        if i in cell_index[0]:
            kmap[0][cell_index[0].index(i)] = '1'
        elif i in cell_index[1]:
            kmap[1][cell_index[1].index(i)] = '1'
        elif i in cell_index[2]:
            kmap[2][cell_index[2].index(i)] = '1'
        else:
            kmap[3][cell_index[3].index(i)] = '1'
    return kmap


displaymap(ass_minterms([[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']], [0, 3, 4, 7, 9, 12, 14]))
