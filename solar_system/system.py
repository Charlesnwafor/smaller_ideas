#Author: Ikenna
#Date: 10/23/2023
#Purpose: Assignment 11 &b 12

from math import *
class System:

    def __init__(self, body_list):

        self.body_list = body_list

    def draw(self, cx, cy, pixels_per_meter):

        for x in self.body_list:
            x.draw(cx, cy, pixels_per_meter)

    def update(self, timestep):
        for n in range (0, len(self.body_list)):
            self.body_list[n].update_position(timestep)
            (a_x, a_y) = self.compute_acceleration(n)
            self.body_list[n].update_velocity(a_x, a_y, timestep)


    def compute_acceleration(self, n):
        G =  6.67384e-11
        a_x = 0
        a_y = 0

        xn = self.body_list[n].x
        yn = self.body_list[n].y

        for i in range(0, len(self.body_list)):
            check = True
            xi = self.body_list[i].x
            yi = self.body_list[i].y
            mi = self.body_list[i].mass


            if i == n:
                check = False

            if check:
                dx = xi - xn
                dy = yi - yn
                r = sqrt((dx * dx) + (dy * dy))
                a = (G * mi)/(r*r)
                ax = a * (dx/r)
                ay = a * (dy/r)


                a_x = a_x + ax
                a_y = a_y + ay

        return a_x, a_y



