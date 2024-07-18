def draw_line(x0, y0, x1, y1, framebuffer, color):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        framebuffer[y0][x0] = color
        if x0 == x1 and y0 == y1:
            break
        e2 = err * 2
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

def fill_polygon(polygon, framebuffer, color):
    if not polygon:
        return

    min_y = min(polygon, key=lambda p: p[1])[1]
    max_y = max(polygon, key=lambda p: p[1])[1]

    for y in range(min_y, max_y + 1):
        nodes = []
        j = len(polygon) - 1
        for i in range(len(polygon)):
            if polygon[i][1] < y and polygon[j][1] >= y or polygon[j][1] < y and polygon[i][1] >= y:
                nodes.append(int(polygon[i][0] + (y - polygon[i][1]) / (polygon[j][1] - polygon[i][1]) * (polygon[j][0] - polygon[i][0])))
            j = i
        nodes.sort()
        for i in range(0, len(nodes), 2):
            if i + 1 < len(nodes):
                draw_line(nodes[i], y, nodes[i + 1], y, framebuffer, color)

