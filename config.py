__authors__    = "Lennon", "Sali"
__license__    = "Free"
__emails__     = "lennonh45@kprschools.ca", "salmahs24@kprschools.ca"

with open("config.txt", "r") as file:
    data = []
    for pair in file.read().split("\n"):
        data.append(pair.split(":")[1])
        
pixel_size = int(data[0])
volume = float(data[1])
mute = bool(data[2])
up = int(data[3])
down = int(data[4])
left = int(data[5])
right = int(data[6])

# stores all important global values
title = "Shadows Of War"
fps = 60
width, height = 16, 9
chunk_dimensions = width, height
tile_size = 16*pixel_size
tile_dimensions = tile_size, tile_size
window_width, window_height = width*tile_size, height*tile_size
window_dimensions = window_width, window_height


