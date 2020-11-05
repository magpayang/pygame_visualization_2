# accepts array
# draws the rectangles

import pygame


class arrayToRectangles:
    def __init__(self, surface, surface_dimensions, input_array, color, x_offset = 0, y_offset = 0):
        self.surface = surface
        self.surface_dimension = surface_dimensions  # tuple
        self. input_array = input_array
        self.color = color  # 3 item tupple

        # calculate other variables
        self.surface_width, self.surface_height = self._calculate_surface_dimensions()
        self.red, self.green, self.blue = self._calculate_indiviual_colors()

        # individual_rectangle properties
        self.rectangle_width = self._calculate_rectangle_widht()
        self.rectangle_height = 0
        self.x_position = self._calculate_x_position(x_offset)
        self.y_offset = y_offset  # position is also dependent on array value

        # draw
        self._draw()

    def _calculate_indiviual_colors(self):
        red, green, blue = self.color
        return red, green, blue

    def _calculate_surface_dimensions(self):
        surface_width, surface_height = self.surface_dimension
        return surface_width, surface_height

    def _calculate_rectangle_widht(self):
        return self.surface_width//len(self.input_array)

    def _calculate_x_position(self, offset=0):
        return offset

    def _calculate_y_position(self, array_value=0, offset=0):
        # think of offset as the y value on the normal x-y coordinate plane
        return self.surface_height - array_value - self.y_offset

    def _draw(self):
        for entry in self.input_array:
            pygame.draw.rect(self.surface, (self.red, self.green, self.blue), (self.x_position, self._calculate_y_position(entry), self.rectangle_width, entry))
            self.x_position += self.rectangle_width

    def update(self, input_array, color, x_offset = 0, y_offset = 0):
        self.input_array = input_array
        self.red, self.green, self.blue = self._calculate_indiviual_colors(color)
        self.x_position = self._calculate_x_position(x_offset)
        self.y_offset = y_offset

        self._draw()