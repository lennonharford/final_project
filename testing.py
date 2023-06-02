import config as conf
from vector import Vector
from tile import Tile
    
def populate_tiles():
    tiles = []
    rows, cols = conf.chunk_dimensions
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(Tile(i, j))
        tiles.append(col)
    return tiles

x = populate_tiles()

for thing in x:
    print(thing)
    
    
print("\n\n | {} |".format(x[3][4]))
