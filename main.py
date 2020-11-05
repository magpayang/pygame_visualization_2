
import prefabArrays
import modes
import time
import Colors
import pygame

pygame.init()

screen_width = 300*2
screen_height = 300
screen_dimensions = (screen_width, screen_height)
screen = pygame.display.set_mode((screen_width, screen_height))

array_length = 100
input_array = prefabArrays.descending_array(100, screen_height)
# mode = "default"
# mode = "buble"
mode = "selection_sort"
stick = array_length  # initial stick value, init value does not matter
preFab = False

loop_count = 0
delay = 0.1
halt = False
while True:
    time.sleep(delay)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if not halt:
        screen.fill(Colors.black)

    if mode.lower() == "default":
        loop_count, input_array = modes.default_mode(loop_count, screen, screen_dimensions, array_length, screen_height,
                                                     Colors.red, input_array=input_array)
    elif mode.lower() == "buble":
        loop_count, input_array = modes.buble_one_pass(loop_count, screen, screen_dimensions, array_length,
                                                       screen_height, Colors.red, input_array=input_array,
                                                       preFab=preFab)
    elif mode.lower() == "selection_sort":
        loop_count, input_array, stick = modes.selection_sort_one_pass(loop_count, screen, screen_dimensions, array_length,
                                                       screen_height, Colors.red, input_array=input_array,
                                                       preFab=preFab, stick=stick)

    pygame.display.flip()
