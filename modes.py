
import RandomArrays
import ArrayToRectangles
import SortingAlgo
import prefabArrays


def default_mode(loop_count, surface, surface_dimension, array_length, screen_height, color, input_array=None):
    if loop_count == 0:
        # initialize everything
        # 1. create objects
        #   a. create array
        input_array = RandomArrays.random_array(array_length, screen_height)
        #   b. array_to_objects
        ArrayToRectangles.arrayToRectangles(surface, surface_dimension, input_array, color, 0, 0)
        # 2. draw
        loop_count += 1
    elif loop_count >= screen_height:
        # base case achieved
        loop_count = 0
    else:
        # update everything
        # 1. update objects
        #   a. algo updates array:
        #   b. updated_array_to_objects
        # 2. draw
        ArrayToRectangles.arrayToRectangles(surface, surface_dimension, input_array, color, 0, 0)
        loop_count += 1

    return loop_count, input_array


def buble_one_pass(loop_count, surface, surface_dimension, array_length, screen_height, color, input_array=None, preFab=False):
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
        input_array = SortingAlgo.buble_sort_one_pass(input_array)
        ArrayToRectangles.arrayToRectangles(surface, surface_dimension, input_array, color, 0, 0)
        loop_count += 1
    return loop_count, input_array
