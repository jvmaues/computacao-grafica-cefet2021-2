from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from Sphere import Sphere, rotate, set_angle, angle
import numpy

sun = Sphere(0,0,0,1, color = (160, 100,  -300))
earth = Sphere(4,0,0,0.3, color = (0, 0, 200))
moon = Sphere(4.8,0,0,0.1, color = (200, 200, 200))


stars = []
total_stars = 1000
starts_range = 50



def load_random_stars():

    x  = list(numpy.random.rand(1, total_stars)[0])
    y  = list(numpy.random.rand(1, total_stars)[0])
    stars.append(x)
    stars.append(y)

def draw_stars():
    
    glPushMatrix()

    glTranslatef(0,0,-30)

    glBegin(GL_POINTS)
    for i in range(total_stars):
        x = stars[0][i]*starts_range
        y = stars[1][i]*starts_range
        glVertex3fv((x, y, 0))
        glVertex3fv((-y, -x, 0))
        glVertex3fv((-x, y, 0))
        glVertex3fv((y, -x, 0))
    glEnd()
    
    glPopMatrix()	

def draw():

	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	
	draw_stars()

	sun.draw(rotation = (angle['sun']['translation'],1,1,1))
	rotate('sun')
	
	earth.draw(rotation = (angle['earth']['translation'],1,1,1))
	moon.draw(rotation = (angle['moon']['translation'],1,1,1))

	pos_earth = earth.get_orbit_position(sun, 3, angle['earth']['rotation'])
	earth.move_to(*pos_earth)
	rotate('earth')

	pos_moon = moon.get_orbit_position(earth, 0.5, angle['moon']['rotation'])
	moon.move_to(*pos_moon)
	rotate('moon')

	glutSwapBuffers()

def timer(i):
	glutPostRedisplay()
	glutTimerFunc(50,timer,1)

if __name__ == '__main__':
	load_random_stars()	
	set_angle('sun', rotation = (0,0.1), translation = (0,0.9))
	set_angle('earth', rotation = (0,0.02), translation = (0,0.9))
	set_angle('moon', rotation = (0,0.1), translation = (0,0.2))
	
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
	glutInitWindowSize(1000,800)
	glutCreateWindow('Solar System')
	glutDisplayFunc(draw)
	glEnable(GL_MULTISAMPLE)
	glEnable(GL_DEPTH_TEST)
	glClearColor(0.,0.,0.,1.)
	gluPerspective(45,800.0/600.0,0.1,100.0)
	glTranslatef(0.0,0.0,-15)
	glutTimerFunc(50,timer,1)
	glutMainLoop()