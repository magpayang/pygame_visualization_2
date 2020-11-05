
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

array_length = 50
input_array = prefabArrays.descending_array(100, screen_height)
mode = "buble"
# mode = "default"
preFab = True

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

    pygame.display.flip()
