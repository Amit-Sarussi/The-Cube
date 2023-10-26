import os
import numpy as np
import platform
import ctypes

points = [
    np.array([1, 1, 1]),
    np.array([-1, 1, 1]),
    np.array([-1, -1, 1]),
    np.array([1, -1, 1]),
    np.array([1, 1, -1]),
    np.array([-1, 1, -1]),
    np.array([-1, -1, -1]),
    np.array([1, -1, -1])
]

lines = [
    [0, 1],
    [1, 5],
    [5, 4],
    [4, 0],

    [3, 2],
    [2, 6],
    [6, 7],
    [7, 3],

    [0, 3],
    [1, 2],
    [5, 6],
    [4, 7]
]

sin = np.sin
cos = np.cos

if platform.system() == 'Windows':
    ctypes.windll.kernel32.SetConsoleTitleW("The Cube - Amit Sarussi")
else:
    print(f"\033]0;{'The Cube - Amit Sarussi'}\a", end="", flush=True)

# Rotate, a: z, b: y, c: x
def rotate(p, a, b, c):
    rotationMatrix = [
        [cos(a)*cos(b), cos(a)*sin(b)*sin(c)-sin(a)*cos(c), cos(a)*sin(b)*cos(c)+sin(a)*sin(c)],
        [sin(a)*cos(b), sin(a)*sin(b)*sin(c)+cos(a)*cos(c), sin(a)*sin(b)*cos(c)-cos(a)*sin(c)],
        [-sin(b), cos(b)*sin(c), cos(b)*cos(c)]
    ]
    return np.matmul(p, rotationMatrix)

def drawLine(image, x1, y1, x2, y2, thickness, character='#'):
    def plot(x, y):
        image[y][x] = character

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    if dx > dy:
        if x1 > x2:
            x1, x2, y1, y2 = x2, x1, y2, y1

        for i in range(-thickness // 2, thickness // 2 + 1):
            y1_thick = y1 + i
            m = (y2 - y1) / (x2 - x1)

            for x in range(x1, x2 + 1):
                y = int(round(y1_thick + m * (x - x1)))
                plot(x, y)
    else:
        if y1 > y2:
            x1, x2, y1, y2 = x2, x1, y2, y1

        for i in range(-thickness // 2, thickness // 2 + 1):
            x1_thick = x1 + i
            try:
                m = (x2 - x1) / (y2 - y1)
            except:
                m = 0

            for y in range(y1, y2 + 1):
                x = int(round(x1_thick + m * (y - y1)))
                plot(x, y)

def clearScreen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

while True:
    screen = [[" " for _ in range(40)] for _ in range(40)]

    for index, point in enumerate(points):
        points[index] = rotate(point, 0.07, 0.02, 0.04)

    for line in lines:
        p1 = (points[line[0]][0]*10+19, points[line[0]][1]*10+19)
        p2 = (points[line[1]][0]*10+19, points[line[1]][1]*10+19)
        drawLine(screen, int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]), 1)

    clearScreen()
    print("\n"*3, flush = True)
    for row in screen:
        print(" "*10 + "".join(row), flush=True)
