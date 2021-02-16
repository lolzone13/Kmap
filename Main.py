"""
Current Objective: create checking class

samplemap = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]

"""


class check:
    def __init__(self):
        pass

    def two_group(self, kmap):
        # 2group = []

        # rows
        for row in kmap:
            for j in range(len(row)):
                if row[j] == row[j - 1] and (row[j] != ' '):
                    row[j] += '*'
                    row[j - 1] += '*'
        # columns
        for col in range(len(kmap)):
            for i in range(len(kmap)):
                if kmap[col][i] == kmap[col - 1][i] and (kmap[col][i] != ' ') and \
                        (('*' not in kmap[col][i]) or ('*' not in kmap[col - 1][i])):
                    kmap[col][i] += '$'
                    kmap[col - 1][i] += '$'

        return kmap

    def four_group(self, kmap):

        # box of four (works for diagonals too lmao)
        # 4group = []
        for row in range(len(kmap)):
            for col in range(len(kmap[row])):
                cell = kmap[row][col]
                if (cell == kmap[row - 1][col]) and (cell == kmap[row][col - 1]) and (cell == kmap[row - 1][col - 1]) \
                        and cell != ' ':
                    kmap[row][col] += '4g'
                    kmap[row - 1][col] += '4g'
                    kmap[row - 1][col - 1] += '4g'
                    kmap[row][col - 1] += '4g'
        return kmap


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
    Returns the index of a kmap cell and boolean values of kmap cells

    :return: indices of kmap cells
    """

    mintermarr = [[0, 1, 3, 2], [4, 5, 7, 6], [12, 13, 15, 14], [8, 9, 11, 10]]
    boolarr = [['0000', '0001', '0011', '0010'],
               ['0100', '0101', '0111', '0110'],
               ['1100', '1101', '1111', '1110'],
               ['1000', '1001', '1011', '1010']]
    return mintermarr, boolarr


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


testmap = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]

testmin = [0, 2, 5, 7, 8, 10, 13, 15]

displaymap(ass_minterms(testmap, testmin))

obj = check()
fcheck = obj.four_group(testmap)
final = obj.two_group(fcheck)
displaymap(final)
