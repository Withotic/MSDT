import pygame


dots = []
lines = []
EDGE_LENGTH = 90
clock = pygame.time.Clock()
mouse_position = (0, 0)


def generate_dots():
    for y in range(13):
        for x in range(25):
            dots.append(
                (int( x * EDGE_LENGTH * (3**0.5) / 2 ),
                 y*EDGE_LENGTH + (x%2==0)*EDGE_LENGTH//2 ))


def distance(d1, d2):
    return ( (d1[0]-d2[0])**2 + (d1[1]-d2[1])**2 )**0.5


def correct_mouse_pos_to_grid(pos):
    minimal_distance_dot = dots[0]
    minimal_distance = distance(pos, dots[0])
    for dot in dots:
        if distance(pos, dot) < minimal_distance:
            minimal_distance_dot = dot
            minimal_distance = distance(pos, dot)
    return minimal_distance_dot


def distance_between_dot_n_line(dot, line):
    a = distance(dot, line[0])
    b = distance(dot, line[1])
    c = distance(line[0], line[1])
    h = (((a+b+c) * (a+b-c) * (a-b+c) * (-a+b+c)) ** 0.5 / 4) * 2 // c
    am = (a**2 - h**2) ** 0.5
    bm = (b**2 - h**2) ** 0.5
    if am <= c and bm <= c:
        return h
    else:
        return min(am, bm)


def delete_nearest_line(pos):
    minimal_distance = 999999
    minimal_distance_line = None
    for line in lines:
        if not(minimal_distance_line)\
          or minimal_distance>distance_between_dot_n_line(pos, line):
            minimal_distance_line = line
            minimal_distance = distance_between_dot_n_line(pos, line)
    if minimal_distance_line:
        lines.remove(minimal_distance_line)

    
def draw_lines():
    for line in lines:
        pygame.draw.line(screen, (100, 100, 100), line[0], line[1], 5)


def draw_dots():
    for dot in dots:
        pygame.draw.circle(screen, (200, 0, 0), dot, 10)


pygame.init()
generate_dots()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
dot_1 = (0, 0)
dot_2 = None
is_mouse_drag = False


while True:
    screen.fill((200, 200, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                is_mouse_drag = True
                dot_1 = correct_mouse_pos_to_grid(event.pos)
                dot_2 = None
            if event.button == 3:
                delete_nearest_line(event.pos)
        if is_mouse_drag:
            mouse_position = correct_mouse_pos_to_grid(event.pos)
        if event.type==pygame.MOUSEBUTTONUP and event.button==1:
            is_mouse_drag = False
            if dot_1!=correct_mouse_pos_to_grid(mouse_position)\
              and (dot_1, mouse_position) not in lines:
                lines.append((dot_1, mouse_position))
    if is_mouse_drag:
        pygame.draw.line(screen, (100, 100, 100), dot_1, mouse_position, 5)
    draw_lines()
    draw_dots()
    pygame.display.flip()
    clock.tick(60)

