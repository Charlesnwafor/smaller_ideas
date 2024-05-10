#Author: Ikenna
#Date: 30/10/2023
#Purpose: Sorting it all out

from cs1lib import *

RAD = 5
SCALE = 2
WIN_H = 360
WIN_W = 720

class City:

    def __init__(self, country_code, city_name, region, population, latitude, longitude):

        self.country_code = country_code
        self.city_name = city_name
        self.region = region
        self.population = int(population)
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def __str__(self):
        return self.city_name + "," + str(self.population) + "," + str(self.latitude) + "," + str(self.longitude)

    def draw(self, cx, cy):

        px = self.longitude * SCALE + cx
        py = WIN_H - ((self.latitude * SCALE) + cy)

        draw_circle(px, py, RAD)


