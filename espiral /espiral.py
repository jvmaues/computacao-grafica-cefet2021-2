from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

import math

radius = float(0.1)

glBegin(GL_POINTS)

for angle in range(1440):
    x = math.cos(1)
    y = math.sin(1)
    radius += 0.1
    glVertex2f(x, y)
glEnd()