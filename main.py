
# import SortingAlgo
import ArrayToRectangles
import RandomArrays
import time
import Colors
import pygame

pygame.init()

screen_width = 300*2
screen_height = 300
screen_dimensions = (screen_width, screen_height)
screen = pygame.display.set_mode((screen_width, screen_height))

y_offset = 0
object_holder = []
array_lenght = 100
max_array_height = screen_height
min_array_height = 0
loop_count = 0
i = 0
delay = 0.01
halt = False
while True:
    time.sleep(delay)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if not halt:
        screen.fill(Colors.black)

    if loop_count == 0:
        # initialize everything
        # 1. create objects
        #   a. create array
        input_array = RandomArrays.random_array(array_lenght, screen_height)
        #   b. array_to_objects
        ArrayToRectangles.arrayToRectangles(screen, screen_dimensions, input_array, Colors.red, loop_count, 0)
        # 2. draw
        loop_count += 1
    elif loop_count >= screen_height:
        # base case achieved
        loop_count = 0
    else:
        # update everything
        # 1. update objects
        #   a. algo updates array
        #   b. updated_array_to_objects
        # 2. draw
        ArrayToRectangles.arrayToRectangles(screen, screen_dimensions, input_array, Colors.red, loop_count, 0)
        loop_count += 1

    pygame.display.flip()
