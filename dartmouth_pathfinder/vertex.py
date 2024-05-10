#Author: Ikenna
#Date: 11/10/2023
#Purpose: Vertex Class

from cs1lib import *

WIDTH = 3
RADIUS = 8
class Vertex:

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.adj_list = []

    def __str__(self): #PROBLEM HERE

        str_list = []
        for adj_vertex in self.adj_list:
            vertex_name = adj_vertex.name
            str_list.append(vertex_name)

        return (self.name + "; " + "Location:" + str(self.x) + ", " + str(self.y) + "; " + "Adjacent vertices: " + str(str_list))

    def draw_vertex(self, r, g, b):

        disable_stroke()
        set_fill_color(r, g, b)
        draw_circle(self.x, self.y, RADIUS)

    def draw_edge(self, vertex, r, g, b):

        enable_stroke()
        set_stroke_width(WIDTH)
        set_stroke_color(r, g, b)
        draw_line(self.x, self.y, vertex.x, vertex.y)


    def draw_all_edges(self, r, g, b):

        enable_stroke()
        set_stroke_width(WIDTH)
        set_stroke_color(r, g, b)
        for other_vertex in self.adj_list:
            draw_line(self.x, self.y, other_vertex.x, other_vertex.y)

    def is_clicked(self, x, y):

        if self.x - RADIUS <= x <= self.x + RADIUS and self.y - RADIUS <= y <= self.y + RADIUS:
            return True
        else:
            return False