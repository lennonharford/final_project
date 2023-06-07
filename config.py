# from pygame.math import Vector2 as Vector
from vector import Vector


title: str = "The Shadows Of War"
chunk_dimensions: Vector = Vector(16, 9)
fps: int = 60
pixel_size: int = 3
tile_size: int = 16*pixel_size
window_margin: int = 5*pixel_size
window_width: int = chunk_dimensions.x*tile_size + 2*window_margin
window_height: int = chunk_dimensions.y*tile_size + 2*window_margin
margin_left: int = window_margin
margin_right: int = window_width - window_margin
margin_top: int = window_margin
margin_bottom: int = window_height - window_margin
window_dimensions: Vector = Vector(window_width, window_height)
tick: int = 0
gamestates: tuple[str, ...] = 'menu', 'main', 'end'
gamestate: str = gamestates[0]