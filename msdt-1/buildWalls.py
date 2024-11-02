import pygame as pg


screen = pg.display.set_mode((800, 800))
player_position = (30, 30)
player_radius = 20
player_speed = 10
lines = []
building_line_dot = None  #buildlinedot
is_debug = False


#---------------------------------------------------------EVENTS HANDLING(done)
def events_handling():
    global player_position, building_line_dot, lines, is_debug
    keys = pg.key.get_pressed()
    player_move_x = 0
    player_move_y = 0
    if keys[pg.K_UP]:
        player_move_y -= 1
    if keys[pg.K_DOWN]:
        player_move_y += 1
    if keys[pg.K_LEFT]:
        player_move_x -= 1
    if keys[pg.K_RIGHT]:
        player_move_x += 1
    if player_move_x!=0 and player_move_y!=0:
        player_position = (player_position[0] + player_speed*player_move_x/(2**0.5),
                           player_position[1] + player_speed*player_move_y/(2**0.5))
    else:
        player_position = (player_position[0] + player_speed*player_move_x,
                     player_position[1] + player_speed*player_move_y)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_e:
                if not (building_line_dot):
                    building_line_dot = player_position
                elif building_line_dot:
                    lines.append((building_line_dot, player_position))
                    if not is_debug:
                        player_position = (player_position[0] + player_radius,
                                     player_position[1] + player_radius)
                    building_line_dot = None
            if event.key == pg.K_r:
                building_line_dot = None
            if event.key == pg.K_k:
                lines = []
            if event.key == pg.K_c:
                is_debug = not is_debug
            if event.key == pg.K_q:
                exit()


#---------------------------------------------------------COLLISION(almostdone)
def line_length(line):
    return ( (line[0][0]-line[1][0])**2 + (line[0][1]-line[1][1])**2 ) ** 0.5


def distance_to_line(line):
    global player_position
    a = line_length((line[0], player_position))
    b = line_length((line[1], player_position))
    c = line_length(line)
    if c==0:
        return (line[0], player_position)
    h = abs( (a+b+c) * (a+b-c) * (a-b+c) * (-a+b+c) ) ** 0.5 / 2 / c
    am = (abs(a**2 - h**2)) ** 0.5
    bm = (abs(b**2 - h**2)) ** 0.5
    if am<=c and bm<=c:
        return ((player_position[0] + h * (line[1][1]-line[0][1]) / c,
                 player_position[1] + h * (line[0][0]-line[1][0]) / c),
                 player_position)
    else:
        if line_length((line[0], player_position)) == min(line_length((line[0], player_position)),
                                                line_length((line[1], player_position))):
            return (line[0], player_position)
        else:
            return (line[1], player_position)


def set_line_length(line, length, multiplier):
    if line_length(line) > 0:
        if multiplier:
            return (line[0],
                    (line[0][0] + (line[1][0]-line[0][0]) * length,
                     line[0][1] + (line[1][1]-line[0][1]) * length))
        else:
            return (line[0],
                   (line[0][0] + (line[1][0]-line[0][0]) * length / line_length(line),
                    line[0][1] + (line[1][1]-line[0][1]) * length / line_length(line)))
    else:
        return line


def collision():
    global player_position, player_radius
    screen_sizes = pg.display.get_window_size()
    if player_position[0] - player_radius < 0:
        player_position = (player_radius, player_position[1])
    if player_position[1] - player_radius < 0:
        player_position = (player_position[0], player_radius)
    if player_position[0] + player_radius > screen_sizes[0]:
        player_position = (screen_sizes[0] - player_radius, player_position[1])
    if player_position[1] + player_radius > screen_sizes[1]:
        player_position = (player_position[0], screen_sizes[1] - player_radius)

    for line in lines:
        distance_to_line = distance_to_line(line)
        if(line_length(distance_to_line) < player_radius):
            player_position = set_line_length(distance_to_line, player_radius, False)[1]


#-------------------------------------------------------------RENDER(linesplit)
def draw_wall(line):
    pg.draw.line(screen, (255, 255, 255), line[0], line[1])
    pg.draw.line(screen, (255, 0, 0), line[0],
                 set_line_length((
                                line[0],
                                (
                                    line[0][0] + (line[1][1]-line[0][1]),
                                    line[0][1] + (line[0][0]-line[1][0])
                                )
                            ),
                            10, False)[1])
    pg.draw.line(screen, (255, 0, 0), line[1],
                 set_line_length((
                                line[1],
                                (
                                    line[1][0] + (line[1][1]-line[0][1]),
                                    line[1][1] + (line[0][0]-line[1][0])
                                )
                            ),
                            10, False)[1])


def sign(n):
    if n < 0:
        return -1
    if n == 0:
        return 0
    return 1


def is_dot_in_triangle(a, b, c, D):
    z1 = sign((a[0]-D[0]) * (b[1]-a[1]) - (b[0]-a[0]) * (a[1]-D[1]))
    z2 = sign((b[0]-D[0]) * (c[1]-b[1]) - (c[0]-b[0]) * (b[1]-D[1]))
    z3 = sign((c[0]-D[0]) * (a[1]-c[1]) - (a[0]-c[0]) * (c[1]-D[1]))
    return z1==z2 and z2==z3 and z1!=0


def is_dot_on_line(d, l):
    if l[0][0] == l[1][0]:
        return (  (l[0][1]<=d[1] and d[1]<=l[1][1])
               or (l[0][1]>=d[1] and d[1]>=l[1][1]))\
               and (line_length((l[0], d))+line_length((l[1], d)) < line_length(l)*1.001)
    if l[0][1] == l[1][1]:
        return ((l[0][0]<=d[0] and d[0]<=l[1][0])
             or (l[0][0]>=d[0] and d[0]>=l[1][0]))\
             and (line_length((l[0], d))+line_length((l[1], d)) < line_length(l)*1.001)
    return (    (l[0][0]<=d[0] and d[0]<=l[1][0])
             or (l[0][0]>=d[0] and d[0]>=l[1][0]))\
           and ((l[0][1]<=d[1] and d[1]<=l[1][1])
             or (l[0][1]>=d[1] and d[1]>=l[1][1]))


def dot_of_crossing_lines(l1, l2):
    A = l1[1][0] - l1[0][0]
    B = l2[1][0] - l2[0][0]
    C = l1[1][1] - l1[0][1]
    D = l2[1][1] - l2[0][1]
    if (A*D - C*B) == 0:
        return None
    q = ( C*(l2[0][0]-l1[0][0]) - A*(l2[0][1]-l1[0][1]) ) / (A*D - C*B)
    d = (l2[0][0] + B*q, l2[0][1] + D*q)
    return (d, is_dot_on_line(d, l1), is_dot_on_line(d, l2))


def is_line_fullblocked_by_another_line(blocked_line, blocking_line):
    global player_position
    n1 = dot_of_crossing_lines((player_position, blocked_line[0]), blocking_line)
    n2 = dot_of_crossing_lines((player_position, blocked_line[1]), blocking_line)
    n3 = dot_of_crossing_lines(blocked_line, blocking_line)
    return n1 and n2 and n1[1] and n1[2] and n2[1] and n2[2]


def is_line_doublesplited_by_another_line(l, d1, d2):
    a = line_length((l[0], d1))
    b = line_length((l[0], d2))
    if a == b:
        return [l]
    if a < b:
        return [(l[0], d1), (d2, l[1])]
    else:
        return [(l[0], d2), (d1, l[1])]


def is_line_partblocked_by_another_line(blocked_line, blocking_line):
    global player_position
    if (    is_dot_in_triangle(player_position, blocked_line[0], blocked_line[1], blocking_line[0])
        and is_dot_in_triangle(player_position, blocked_line[0], blocked_line[1], blocking_line[1])):
        print('hi')
        return is_line_doublesplited_by_another_line(blocked_line,
               dot_of_crossing_lines(blocked_line, (player_position, blocking_line[0]))[0],
               dot_of_crossing_lines(blocked_line, (player_position, blocking_line[1]))[0])
    if (    dot_of_crossing_lines((player_position, blocked_line[0]), blocking_line)
        and dot_of_crossing_lines((player_position, blocked_line[0]), blocking_line)[1]
        and dot_of_crossing_lines((player_position, blocked_line[0]), blocking_line)[2]):
        print('hi1')
        if is_dot_in_triangle(player_position, blocked_line[0], blocked_line[1], blocking_line[0]):
            return [(dot_of_crossing_lines((player_position, blocking_line[0]), blocked_line)[0], blocked_line[1])]
        else:
            return [(dot_of_crossing_lines((player_position, blocking_line[1]), blocked_line)[0], blocked_line[1])]
    if (    dot_of_crossing_lines((player_position, blocked_line[1]), blocking_line)
        and dot_of_crossing_lines((player_position, blocked_line[1]), blocking_line)[1]
        and dot_of_crossing_lines((player_position, blocked_line[1]), blocking_line)[2]):
        print('hi2')
        if is_dot_in_triangle(player_position, blocked_line[0], blocked_line[1], blocking_line[0]):
            return [(dot_of_crossing_lines((player_position, blocking_line[0]), blocked_line)[0], blocked_line[0])]
        else:
            return [(dot_of_crossing_lines((player_position, blocking_line[1]), blocked_line)[0], blocked_line[0])]
    return None


def is_line_notblocked(dl, bl):
    global player_position
    n1 = dot_of_crossing_lines((player_position, dl[0]), bl)
    n2 = dot_of_crossing_lines((player_position, dl[1]), bl)
    n3 = dot_of_crossing_lines(dl, bl)
    return    (not(n3) or (not(n3[1]) and not(n3[2])))\
          and (not(n2) or (not(n2[1]) and not(n2[2])))\
          and (not(n1) or (not(n1[1]) and not(n1[2])))\
          and not(is_dot_in_triangle(player_position, dl[0], dl[1], bl[0]))\
          and not(is_dot_in_triangle(player_position, dl[0], dl[1], bl[1]))


def splitted_lines():#должен вернуть массив из разрезанной стены
    global player_position,lines
    blocked_lines = lines.copy()
    i = 0
    while i < len(blocked_lines):
        blocking_lines = blocked_lines.copy()
        blocking_lines.remove(blocked_lines[i])
        while len(blocking_lines) > 0:
            if is_line_fullblocked_by_another_line(blocked_lines[i], blocking_lines[0]):
                blocked_lines.pop(i)
                i -= 1
                blocking_lines.pop(0)
                break
            pb = is_line_partblocked_by_another_line(blocked_lines[i], blocking_lines[0])
            if pb:
                blocked_lines.pop(i)
                blocked_lines += pb
            blocking_lines.pop(0)
        i += 1
    return blocked_lines


def render():
    if building_line_dot:
        draw_wall((building_line_dot, player_position))
    if is_debug:
        for line in lines:
            draw_wall(line)
    else:
        for line in splitted_lines():
            pg.draw.line(screen, (255, 255, 255), line[0], line[1])


#--------------------------------------------------------------------MAIN(done)
clock = pg.time.Clock()
pg.init()
while True:
    screen.fill((0, 0, 0))
    events_handling()
    if not is_debug:
        collision()
    render()
    pg.draw.circle(screen, (255, 255, 255), player_position, player_radius)
    pg.display.flip()
    clock.tick(60)
    pg.display.set_caption(f'FPS: {clock.get_fps() :.2f}')
