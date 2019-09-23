# ####################################################
# DE2-COM2 Computing 2
# Individual project
#
# Title: The Tetriling Reassembly - MAIN
# Author: Clara Arcos
# ####################################################

from collections import namedtuple
from copy import deepcopy
import cProfile
from itertools import chain
from pprint import pprint
from random import sample, random
import sys
import time

import scipy.signal
import numpy as np

import utils
from shape_matrices import generate_shape_matrix

placement_dtype = np.dtype([('shapeID', np.uint8), ('row', np.uint16), ('col', np.uint16), ('score', np.uint8)])

def Tetris(target, limit_tetris):
    """
    This function uses the input target matrix and input shapes, and outputs a
    solution matrix
    :param target: target matrix
    :param limit_tetris: a limited number of 19 types of Tetris
    :return: solution matrix
    """
    target_size = sum(chain(*target))
    if target_size < 1000:
        placement_count = 1
    elif target_size > 100000:
        placement_count = target_size // 50
    else:
        placement_count = target_size // 100

    return solve(partial_sol=convert_to_sol(target), 
                 limit_tetris=limit_tetris,
                 placement_count=placement_count)


def convert_to_sol(target):
    """
    This function converts the target matrix to the format of the solution matrix
    :param target: target matrix
    :return: converted target matrix
    """
    return [[None if col == 1 else (0,0) for col in row] for row in target]

def get_neighbours_matrix(partial_sol):
    """
    This function gets the neighbours matrix of the target matrix
    :param partial_sol: solution matrix with Nones where we have to place a piece
    :return: neighbours matrix
    """
    target = [[1 if col is None else 0 for col in row] for row in partial_sol]
    kernel = [[0,1,0],
              [1,0,1],
              [0,1,0]]
    neighbours_matrix = np.multiply(scipy.signal.convolve2d(target, kernel, mode='same'), target)
    return neighbours_matrix

def get_score_matrix(neighbours_matrix, shape_id):
    """
    Create a matrix giving the score of placing a given shape id at every position on the board.
    A score < 0 indicates that the shape can't be placed in that position
    """
    shape_matrix = generate_shape_matrix(shape_id)
    neighbours_matrix[neighbours_matrix==0] = -20
    score_matrix = scipy.signal.convolve2d(neighbours_matrix, np.flip(shape_matrix), mode='same', fillvalue=-20)   
    return score_matrix

def generate_placements(neighbours_matrix, limit_tetris, placements):
    """
    :return: How many placements were generated
    """
    i = 0
    for shape_id in (id for id, count in limit_tetris.items() if count > 0):
        score_matrix = get_score_matrix(neighbours_matrix, shape_id)
        for row_n, row in enumerate(score_matrix):
            for col_n, score in enumerate(row):
                if score > 0:
                    placements[i] = (shape_id, row_n, col_n, score)
                    i += 1
    return i

def check_placement(partial_sol, limit_tetris, placement):
    if limit_tetris[placement['shapeID']] == 0:
        return False
    for sq_row, sq_col in utils.generate_shape(placement['shapeID']):
        row = placement['row'] + sq_row
        col = placement['col'] + sq_col
        if partial_sol[row][col] is not None:
            return False
    return True

def apply_placement(partial_sol, limit_tetris, placement, piece_id):
    for sq_row, sq_col in utils.generate_shape(placement['shapeID']):
        row = placement['row'] + sq_row
        col = placement['col'] + sq_col
        partial_sol[row][col] = (placement['shapeID'], piece_id)


def solve(partial_sol, limit_tetris, placement_count):
    """
    This function uses the input partial solution and input shapes, and outputs a
    solution matrix
    :param partial_sol: solution matrix with Nones where we need to place a piece
    :param limit_tetris: a limited number of 19 types of Tetris
    :return: solution matrix
    """

    current_piece_id = 1
    placements = np.zeros(19*len(partial_sol)*len(partial_sol[0]), dtype=placement_dtype)

    while len([None for v in limit_tetris.values() if v > 0]) != 0:
        neighbours_matrix = get_neighbours_matrix(partial_sol)
        pl_count = generate_placements(neighbours_matrix, limit_tetris, placements)
        placements = np.resize(placements, pl_count)
        placements.sort(kind='mergesort', order='score')
        
        # --------------------- PLACE PIECES -------------------------------------------------
        count = 0
        for chosen_placement in placements:
            if count >= placement_count: break

            if check_placement(partial_sol, limit_tetris, chosen_placement):
                apply_placement(partial_sol, limit_tetris, chosen_placement, current_piece_id)
                limit_tetris[chosen_placement['shapeID']] -= 1
                current_piece_id += 1
                count += 1
        # ------------------------------------------------------------------------------------

        if len(placements) == 0: break

    solution = [[el if el is not None else (0,0) for el in row] for row in partial_sol]
    return solution