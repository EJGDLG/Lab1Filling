from utils import initialize_framebuffer
from drawing import draw_line, fill_polygon
from bmp import save_framebuffer_to_bmp

def generate_image(filename):
    width, height = 800, 600
    background_color = [0, 0, 0]  # Negro
    framebuffer = initialize_framebuffer(width, height, background_color)

    # Define los polígonos con sus puntos
    polygons = [
        [(165, 380), (185, 360), (180, 330), (207, 345), (233, 330), (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)],
        [(321, 335), (288, 286), (339, 251), (374, 302)],
        [(377, 249), (411, 197), (436, 249)],
        [(413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37), (660, 52), (750, 145), (761, 179), (672, 192),
         (659, 214), (615, 214), (632, 230), (580, 230), (597, 215), (552, 214), (517, 144), (466, 180)],
        [(682, 175), (708, 120), (735, 148), (739, 170)]
    ]

    colors = [
        [0, 255, 0],  # Verde
        [0, 255, 0],
        [0, 255, 0],
        [0, 255, 0],
        [0, 0, 0]    # Negro (agujero)
    ]

    # Rellenar los polígonos
    for i, polygon in enumerate(polygons):
        fill_polygon(polygon, framebuffer, colors[i])

    # Guardar la imagen en formato BMP
    save_framebuffer_to_bmp(filename, framebuffer)

generate_image("output.bmp")
