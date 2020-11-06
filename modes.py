
import RandomArrays
import ArrayToRectangles
import SortingAlgo
import prefabArrays


def default_mode(loop_count, surface, surface_dimension, array_length, screen_height, color, input_array=None, preFab=False):
    if loop_count == 0:  # initial settings
        if preFab:
            input_array = prefabArrays.descending_array(array_length, screen_height)
        else:
            input_array = RandomArrays.random_array(array_length, screen_height)
        ArrayToRectangles.arrayToRectangles(surface, surface_dimension, input_array, color, 0, 0)
        loop_count += 1
    elif loop_count >= screen_height:  # base cases
        loop_count = 0
    else:  # loops
        ArrayToRectangles.arrayToRectangles(surface, surface_dimension, input_array, color, 0, 0)
        loop_count += 1

    return loop_count, input_array


def bubble_one_pass(loop_count, surface, surface_dimension, array_length, screen_height, color, input_array=None, preFab=False):
    if loop_count == 0:
        if preFab:
            input_array = prefabArrays.descending_array(array_length, screen_height)
        else:
            input_array = RandomArrays.random_array(array_length, screen_height)
        ArrayToRectangles.arrayToRectangles(surface, surface_dimension, input_array, color, 0, 0)
        loop_count += 1
    elif loop_count == array_length:
        # base case case. need to pass at least equal to array_length to fully sort the list
        loop_count = 0
    else:
        input_array = SortingAlgo.bubble_sort_one_pass(input_array)
        ArrayToRectangles.arrayToRectangles(surface, surface_dimension, input_array, color, 0, 0)
        loop_count += 1
    return loop_count, input_array


def selection_sort_one_pass(loop_count, surface, surface_dimension, array_length, screen_height, color, input_array=None, preFab=False, stick=0):
    if loop_count == 0:
        if preFab:
            input_array = prefabArrays.descending_array(array_length, screen_height)
        else:
            input_array = RandomArrays.random_array(array_length, screen_height)
        stick = array_length
        ArrayToRectangles.arrayToRectangles(surface, surface_dimension, input_array, color, 0, 0)
        loop_count += 1
    elif stick == 1:
        loop_count = 0
    else:
        input_array, stick = SortingAlgo.selection_sort_one_pass(input_array, stick)
        ArrayToRectangles.arrayToRectangles(surface, surface_dimension, input_array, color, 0, 0)
        loop_count += 1
    return loop_count, input_array, stick


def insertion_sort_one_pass(loop_count, surface, surface_dimension, array_length, screen_height, color, input_array=None, preFab=False, idx=0):
    if loop_count == 0:
        if preFab:
            input_array = prefabArrays.descending_array(array_length, screen_height)
        else:
            input_array = RandomArrays.random_array(array_length, screen_height)
        idx = 1  # for insertion sort, always start at idx 1 up to less than array.length()
        ArrayToRectangles.arrayToRectangles(surface, surface_dimension, input_array, color, 0, 0)
        loop_count += 1
    elif idx == len(input_array):
        loop_count = 0
    else:
        input_array, idx = SortingAlgo.insertion_sort_one_pass(input_array, idx)
        ArrayToRectangles.arrayToRectangles(surface, surface_dimension, input_array, color, 0, 0)
        idx += 1
        loop_count += 1
    return loop_count, input_array, idx


def Shell_sort_one_pass(loop_count, surface, surface_dimension, array_length, screen_height, color, input_array=None, preFab=False, idx=0, gap=0, gaps=[], gap_idx=0):
    if loop_count == 0:
        if preFab:
            input_array = prefabArrays.descending_array(array_length, screen_height)
        else:
            input_array = RandomArrays.random_array(array_length, screen_height)
        gaps=gaps
        gap = gaps[gap_idx]
        idx = gap
        ArrayToRectangles.arrayToRectangles(surface, surface_dimension, input_array, color, 0, 0)
        loop_count += 1
    elif idx == len(input_array) and gap != 1:
        gap_idx += 1
        gap = gaps[gap_idx]
        idx = 0
    elif gap == 1:
        if idx == len(input_array):
            gap_idx = 0
            gap = gaps[gap_idx]
            idx = 0
            loop_count = 0
        else:
            input_array, idx, gap = SortingAlgo.Shell_sort_one_pass(input_array, idx, gap)
            ArrayToRectangles.arrayToRectangles(surface, surface_dimension, input_array, color, 0, 0)
            idx += 1
    else:
        input_array, idx, gap = SortingAlgo.Shell_sort_one_pass(input_array, idx, gap)
        ArrayToRectangles.arrayToRectangles(surface, surface_dimension, input_array, color, 0, 0)
        idx += 1
    return loop_count, input_array, idx, gap, gaps, gap_idx