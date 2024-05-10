#Author: Ikenna
#Date: 10/30/2023
#Purpose: City driver


from city import *
from random import randint
from quicksort import sort

FRAMERATE = 5
MAX_CITIES = 100

in_file = open("world_cities.txt", "r")
city_reference  = []
for line in in_file:

    s = line.strip()
    z = s.split(",")
    x = City(z[0], z[1], z[2], int(z[3]), float(z[4]), float(z[5]))
    city_reference.append(x)

#Write to text file ~ the output
out_file = open("cities_out.txt", "w")

for x in range(len(city_reference)):

    out_file.write(str(city_reference[x]) + "\n")

out_file.close()


img = load_image("world.png")
num_drawn = 1

def compare_alpha(city1, city2): # function to sort city according to names
    return city1.city_name.lower() <= city2.city_name.lower() #returns True if a <= b

def compare_population(city1, city2):
    return city1.population >= city2.population #returns True if a >= b

def compare_latitude(city1, city2):
    return city1.latitude <= city2.latitude #returns True if a <= b

#sorting cities according to names and writing to file
c1 = sort(city_reference, compare_alpha)
f = open("cities_alpha.txt", "w")
for x in c1:
    f.write(str(x) + "\n")
f.close()

#sorting cities according to latitude
c2 = sort(city_reference, compare_latitude)
f = open("cities_latitude.txt", "w")
for x in c2:
    f.write(str(x) + "\n")
f.close()

#sorting cities according to population
c3 = sort(city_reference, compare_population)
f = open("cities_population.txt", "w")
for x in c3:
    f.write(str(x) + "\n")
f.close()


def mydraw():
    global num_drawn

    clear()

    draw_image(img, 0, 0)
    i = 0
    while i <= num_drawn:
        disable_stroke()
        set_fill_color(randint(0, 2),randint(0, 2),randint(0, 2))
        city_reference[i].draw(WIN_H,WIN_H/2)
        i = i + 1

    if num_drawn < MAX_CITIES:
        num_drawn = num_drawn + 1

start_graphics(mydraw, height=WIN_H, width=WIN_W, framerate=FRAMERATE)

