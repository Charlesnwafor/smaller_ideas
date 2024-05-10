#Author: Ikenna
#Date: 11/10/2023
#Purpose: Displaying the graph

from cs1lib import *
from load_graph import create_vertex_dictionary
from bfs import bfs

WIN_WIDTH = 1012
WIN_HEIGHT = 811
mx = 0
my = 0
start_vertex = None
goal_vertex = None
mpressed = False

vertex_dict = create_vertex_dictionary("dartmouth_graph.txt")
def main_draw():

    global mx, my, mpressed, start_vertex, goal_vertex, vertex_dict

    img = load_image("dartmouth_map.png")
    draw_image(img, 0, 0)

    for vertices in vertex_dict:
        vertex_dict[vertices].draw_vertex(0, 0, 1)
        vertex_dict[vertices].draw_all_edges(0, 0, 1)

    for vertex in vertex_dict:
        if vertex_dict[vertex].is_clicked(mx, my) and mpressed == True:
            start_vertex = vertex_dict[vertex]

    for vert in vertex_dict:
        if vertex_dict[vert].is_clicked(mx, my) and mpressed == False:
            goal_vertex = vertex_dict[vert]

    if start_vertex != None:
        start_vertex.draw_vertex(1, 0, 0)

    if goal_vertex != None:
        goal_vertex.draw_vertex(1, 0, 0)

    if start_vertex != None and goal_vertex != None:
        path = bfs(start_vertex, goal_vertex)

        i = len(path) - 1
        while i > 0:
            path[i].draw_vertex(1, 0, 0)
            path[i].draw_edge(path[i-1], 1, 0, 0)

            i = i - 1


def m_pressed(x, y):
    global mx, my, mpressed

    mpressed = True
    mx = x
    my = y

def m_released(x, y):
    global mx, my, mpressed

    mpressed  = False
    mx = x
    my = y

def m_moved(x, y):
    global mx, my

    mx = x
    my = y



start_graphics(main_draw, height=WIN_HEIGHT, width=WIN_WIDTH, mouse_move=m_moved, mouse_press=m_pressed, mouse_release=m_released)




