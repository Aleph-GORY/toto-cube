class Steve:
    orientations = [[3, 2, 2], [2, 3, 2], [2, 2, 3]]


class Carmen:
    orientations = [[1, 2, 4], [1, 4, 2], [2, 1, 4], [2, 4, 1], [4, 2, 1], [4, 1, 2]]


class Unit:
    orientations = [[1, 1, 1]]


def get_block(id):
    if id == 0:
        return Steve()
    if id == 1:
        return Carmen()
    else:
        return Unit()
