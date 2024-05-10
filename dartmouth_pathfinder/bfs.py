#Author: Ikenna
#Date: 11/11/2022
#Purpose: A19

from vertex import *
from collections import deque

def bfs(start_vertex, goal_vertex):

    backpointer_dict = {}
    frontier = deque()

    frontier.append(start_vertex)
    if len(backpointer_dict) == 0:
        backpointer_dict[start_vertex] = None

    while not goal_vertex in backpointer_dict and len(frontier) != 0:
        V = frontier.popleft()
        for U in V.adj_list:
            if not U in backpointer_dict:
                frontier.append(U)
                backpointer_dict[U] = V

    path = []
    V = goal_vertex
    while V != None:
        path.append(V)
        V = backpointer_dict[V]

    return path