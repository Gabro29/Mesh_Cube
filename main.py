import pygame
from OpenGL.GL import *
from OpenGL.GLU import *


def load_texture(filename):
    textureSurface = pygame.image.load(filename)
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()
    ID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, ID)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE,
                 textureData)
    return ID


def face(translate: list, rotate: list):

    # Create a Square
    vertices = (
        (1, -1, -1),
        (1, 1, -1),
        (1, 1, 1),
        (1, -1, 1)
    )

    line_between_vertices = (
        (0, 1),
        (0, 3),
        (2, 3),
        (2, 1)
    )

    texcoord = (
        (0, 0),
        (1, 0),
        (1, 1),
        (0, 1)
    )

    glTranslated(translate[0], translate[1], translate[2])
    glRotated(rotate[0], rotate[1], rotate[2], rotate[3])
    glBegin(GL_QUADS)
    for vertex in range(4):
        glTexCoord2fv(texcoord[vertex])
        glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for line in line_between_vertices:
        for point in line:
            glTexCoord2fv(texcoord[point])
            glVertex3fv(vertices[point])
    glEnd()

    glRotated(-rotate[0], rotate[1], rotate[2], rotate[3])


def face_pos(translate: list, rotate: list):
    face(translate, rotate)
    glTranslated(-translate[0], -translate[1], -translate[2])


def mesh_cube():

    front = load_texture("1.jpg")
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, front)
    face_pos(translate=[0, 3, 0], rotate=[90, 0, -1, 0])

    back = load_texture("2.jpg")
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, back)
    face_pos(translate=[0, 3, 0], rotate=[90, 0, 1, 0])

    up = load_texture("3.jpg")
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, up)
    face_pos(translate=[0, 3, 0], rotate=[90, 0, 0, 1])

    down = load_texture("4.jpg")
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, down)
    face_pos(translate=[0, 3, 0], rotate=[90, 0, 0, -1])

    left = load_texture("5.jpg")
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, left)
    face_pos(translate=[0, 3, 0], rotate=[180, 0, 1, 1])

    right = load_texture("6.jpg")
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, right)
    face_pos(translate=[0, 3, 0], rotate=[90, 1, 0, 0])



def render_scene(R):

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0, 0, -5)
    glRotatef(R, 1, 0, 0)
    mesh_cube()


def main():
    pygame.init()
    pygame.display.set_mode((600, 480), pygame.DOUBLEBUF | pygame.OPENGL)
    pygame.display.set_caption("Cube Gabro YT")
    clock = pygame.time.Clock()
    done = False
    R = 0

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    display = (800, 600)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(3.5, -4.0, -4)
    glRotatef(45, 1, 1, 1)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)


    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        render_scene(R)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
