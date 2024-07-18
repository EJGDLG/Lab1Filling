from utils import char, word, dword

def save_framebuffer_to_bmp(filename, framebuffer):
    height = len(framebuffer)
    width = len(framebuffer[0])
    
    with open(filename, "wb") as file:
        # Header
        file.write(char("B"))
        file.write(char("M"))
        file.write(dword(14 + 40 + (width * height * 3)))
        file.write(dword(0))
        file.write(dword(14 + 40))

        # Info Header
        file.write(dword(40))
        file.write(dword(width))
        file.write(dword(height))
        file.write(word(1))
        file.write(word(24))
        file.write(dword(0))
        file.write(dword(width * height * 3))
        file.write(dword(0))
        file.write(dword(0))
        file.write(dword(0))
        file.write(dword(0))

        # Color table
        for y in range(height):
            for x in range(width):
                color = framebuffer[y][x]
                # Asegurarnos de que el color es una lista de 3 elementos
                if isinstance(color, list) and len(color) == 3:
                    file.write(bytes([color[2], color[1], color[0]]))
                else:
                    print(f"Error en el color en ({x}, {y}): {color}")
