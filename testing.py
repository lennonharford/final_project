import old_shit.config as conf
from old_shit.vector import Vector
from old_shit.tile import Tile
    
def populate_tiles():
    tiles = []
    rows, cols = conf.chunk_dimensions
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(Tile(i, j))
        tiles.append(col)
    return tiles


l = [
    "xxxx",
    "xxxx",
    "xxxx"
]

def transpose(array: list) -> list:
    return map(lambda *x: list(x), *array)


for x in l:
    print(x)
    
for x in transpose(l):
    print(x)