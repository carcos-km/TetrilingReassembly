def generate_shape_matrix(shape_id):
    """
    Generates matrix representing each shape for use in convolution
    """
    shape = None
    if shape_id == 1:
        shape = [[0, 0, 0],
                 [0, 1, 1],
                 [0, 1, 1]]
    elif shape_id == 2:
        shape = [[0],
                 [0],
                 [0],
                 [1],
                 [1],
                 [1],
                 [1]]
    elif shape_id == 3:
        shape = [[0, 0, 0, 1, 1, 1, 1]]
    elif shape_id == 4:
        shape = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 1, 0],
                 [0, 1, 0],
                 [0, 1, 1]]
    elif shape_id == 5:
        shape = [[0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0],
                 [1, 1, 1, 0, 0]]
    elif shape_id == 6:
        shape = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 1, 1],
                 [0, 0, 1],
                 [0, 0, 1]]
    elif shape_id == 7:
        shape = [[0, 0, 0, 0, 0],
                 [0, 0, 1, 1, 1],
                 [0, 0, 1, 0, 0]]
    elif shape_id == 8:
        shape = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 1, 0],
                 [0, 1, 0],
                 [1, 1, 0]]
    elif shape_id == 9:
        shape = [[0, 0, 0, 0, 0],
                 [0, 0, 1, 1, 1],
                 [0, 0, 0, 0, 1]]
    elif shape_id == 10:
        shape = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 1, 1],
                 [0, 1, 0],
                 [0, 1, 0]]
    elif shape_id == 11:
        shape = [[0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0],
                 [0, 0, 1, 1, 1]]
    elif shape_id == 12:
        shape = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 1, 0],
                 [0, 1, 1],
                 [0, 1, 0]]
    elif shape_id == 13:
        shape = [[0, 0, 0],
                 [0, 1, 0],
                 [1, 1, 1]]
    elif shape_id == 14:
        shape = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 1, 0],
                 [1, 1, 0],
                 [0, 1, 0]]
    elif shape_id == 15:
        shape = [[0, 0, 0, 0, 0],
                 [0, 0, 1, 1, 1],
                 [0, 0, 0, 1, 0]]
    elif shape_id == 16:
        shape = [[0, 0, 0],
                 [0, 1, 1],
                 [1, 1, 0]]
    elif shape_id == 17:
        shape = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 1, 0],
                 [0, 1, 1],
                 [0, 0, 1]]
    elif shape_id == 18:
        shape = [[0, 0, 0, 0, 0],
                 [0, 0, 1, 1, 0],
                 [0, 0, 0, 1, 1]]
    elif shape_id == 19:
        shape = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 1, 0],
                 [1, 1, 0],
                 [1, 0, 0]]
    return shape