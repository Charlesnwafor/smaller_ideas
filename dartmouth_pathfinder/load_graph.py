#Author: Ikenna
#Date: 11/10/2023
#Purpose: Dartmouth finder

from vertex import Vertex

def create_vertex_dictionary(file_name):

    fp = open(file_name, "r")

    vertex_dict = {}

    for line in fp:
        #get the components of every line in a list
        wlist = line.split(";")
        for i in range(len(wlist)):
            wlist[i] = wlist[i].strip()

        #get the x and y in a list
        clist = wlist[2].split(",")
        for i in range(len(clist)):
            clist[i] = clist[i].strip()

        x = int(clist[0])
        y = int(clist[1])

        v_obj = Vertex(wlist[0], x, y)
        vertex_dict[wlist[0]] = v_obj

    fp.close()

    fp = open(file_name, "r")

    for line in fp:
        wlist = line.split(";")
        for i in range(len(wlist)):
            wlist[i] = wlist[i].strip()

        #get the adjacent vertices in a list
        nlist = wlist[1].split(",")
        for i in range(len(nlist)):
            nlist[i] = nlist[i].strip()


        current_v = vertex_dict[wlist[0]]
        for k in nlist:
            current_v.adj_list.append(vertex_dict[k]) #For each adjacent vertex, append a reference to its Vertex object to the adjacency list in the Vertex object of the current vertex.

    fp.close()

    return vertex_dict


