from PIL import Image
import io



# Imports
from PIL import Image
import os
import random
import numpy as np

# Function
def image_to_tiles(im, tile_size = 4):
    """
    Function that splits an image into tiles
    :param im: image: image path
    :param tile_size: width in pixels of a tile
    :return tiles:
    """
    image = Image.open(im)
        
    w = image.width
    h = image.height
    
    row_count = np.int64((h-h%tile_size)/tile_size)
    col_count = np.int64((w-w%tile_size)/tile_size)
    
    n_slices = np.int64(row_count*col_count)
    
    # Image info
    print(f'Image: {im}')
    print(f'Dimensions: w:{w} h:{h}')
    print(f'Tile count: {n_slices}')


    r = np.linspace(0, w, row_count+1)
    r_tuples = [(np.int64(r[i]), np.int64(r[i])+tile_size) for i in range(0, len(r)-1)]
    q = np.linspace(0, h, col_count+1)
    q_tuples = [(np.int64(q[i]), np.int64(q[i])+tile_size) for i in range(0, len(q)-1)]
    
    #print(f'r_tuples:{r_tuples}\n\nq_tuples:{q_tuples}\n')
    
    tiles = []
    for row in range(row_count):
        for column in range(col_count):
            [y1, y2, x1, x2] = *r_tuples[row], *q_tuples[column]
            x2 = x1+tile_size
            y2 = y1+tile_size
            tile_image = image.crop((x1,y1,x2,y2))
            tile_coords = {'x1':x1,'y1':y1,'x2':x2,'y2':y2}
            tiles.append({'image':tile_image,'coords':tile_coords})

    return tiles

# Testing:
img_path ="legacy/images/tileset_v1.png"
tiles = image_to_tiles(img_path)

for i in range(20):
    tile = random.choice(tiles)
    tile['image'].show()











# def image_to_byte_array(image: Image) -> bytes:
#   # BytesIO is a file-like buffer stored in memory
#   imgByteArr = io.BytesIO()
#   # image.save expects a file-like as a argument
#   image.save(imgByteArr, format=image.format)
#   # Turn the BytesIO object back into a bytes object
#   imgByteArr = imgByteArr.getvalue()
#   return imgByteArr

# x = Image.open("legacy/images/tileset_v1.png", mode='r', formats=None)
# thing = image_to_byte_array(x)

# print(thing)



# infile = "legacy/images/tileset_v1.png"
# chopsize = 16

# img = Image.open(infile)
# width, height = img.size

# # Save Chops of original image
# for x0 in range(0, width, chopsize):
#    for y0 in range(0, height, chopsize):
#       box = (x0, y0,
#              x0+chopsize if x0+chopsize <  width else  width - 1,
#              y0+chopsize if y0+chopsize < height else height - 1)
#       print('%s %s' % (infile, box))
#       img.crop(box).save('zchop.%s.x%03d.y%03d.jpg' % (infile.replace('.jpg',''), x0, y0))