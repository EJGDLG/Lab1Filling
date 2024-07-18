import struct

def char(c):
    return struct.pack("=c", c.encode("ascii"))

def word(w):
    return struct.pack("=h", w)

def dword(d):
    return struct.pack("=l", d)

def initialize_framebuffer(width, height, color):
    return [[[color for _ in range(3)] for _ in range(width)] for _ in range(height)]
