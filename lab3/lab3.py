#!/bin/python3


from config import *
from topology import Topology
import srp
import pygame
import random
from math import sqrt


SOURCE_INDEX = 0
DESTINATION_INDEX = 1

WIDTH = 800
HEIGHT = WIDTH

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (127, 127, 127)
LIGHT_GREY = (32, 32, 32)

FPS = 60


class Router:
    def __init__(self, coord, velocity):
        self.coord = coord
        self.velocity = velocity


    def update(self, delta):
        self.coord = [self.coord[0] + self.velocity[0] * delta, self.coord[1] + self.velocity[1] * delta]
        for i in range(2):
            if self.coord[i] > 1:
                self.coord[i] = 2 - self.coord[i]
                self.velocity[i] = -self.velocity[i]
            elif self.coord[i] < -1:
                self.coord[i] = -2 - self.coord[i]
                self.velocity[i] = -self.velocity[i]


def metrics(coord1, coord2):
    dx = coord1[0] - coord2[0]
    dy = coord1[1] - coord2[1]
    return sqrt(dx * dx + dy * dy)


def to_screen(coord):
    return [(coord[0] + 1) / 2 * WIDTH, (1 - coord[1]) / 2 * HEIGHT]


def is_connected(r1, r2):
    dx = r1.coord[0] - r2.coord[0]
    dy = r1.coord[1] - r2.coord[1]
    return dx * dx + dy * dy < DISTANCE_2


def initialize():
    routers = []
    for i in range(ROUTER_NUMBER):
        coord = [random.uniform(-1, 1), random.uniform(-1, 1)]
        velocity = [random.uniform(-MAX_VELOCITY, MAX_VELOCITY), random.uniform(-MAX_VELOCITY, MAX_VELOCITY)]
        routers.append(Router(coord, velocity))
    return routers


prev_path = []


def step(routers):
    class Streaming:
        def __init__(self):
            self.reciever = srp.SrpReceiver(WINDOW_SIZE)
            self.sender = srp.SrpSender(WINDOW_SIZE, PACKAGE, TIMEOUT)


        def progress(self):
            if self.sender.is_done():
                return 1.0
            return  self.sender.ans_count / (self.sender.max_number + 1)


        def send_msg(self):
            if self.sender.send_msg_queue.has_msg():
                self.reciever.recieve_msg_queue.send_message(self.sender.send_msg_queue.get_message())
            if self.reciever.send_msg_queue.has_msg():
                self.sender.recieve_msg_queue.send_message(self.reciever.send_msg_queue.get_message())


        def update(self):
            self.sender.update()
            self.reciever.update()


    global prev_path
    global stream

    for router in routers:
        router.update(1 / FPS)
    topology = Topology()
    for i in range(len(routers)):
        topology.add_new_node(i)
    connections = []
    for i in range(len(routers)):
        router = routers[i]
        for j in range(i):
            if is_connected(router, routers[j]):
                topology.add_new_link(i, j)
                topology.add_new_link(j, i)
                connections.append((i, j))
    paths = topology.get_shortest_ways(SOURCE_INDEX)
    path = paths[DESTINATION_INDEX]
    if len(path) == 0:
        stream = None
        return connections, path, 0
    if len(path) == len(prev_path) and 0 == len([i for i in range(len(path)) if path[i] != prev_path[i]]):
        stream.update()
        stream.send_msg()
    else:
        prev_path = path
        stream = Streaming()
    return connections, path, stream.progress()


def render(screen, routers, connections, path, rate=0.0):
    screen.fill(BLACK)

    for connection in connections:
        pygame.draw.line(screen, LIGHT_GREY, to_screen(routers[connection[0]].coord), to_screen(routers[connection[1]].coord))

    if len(path) != 0:
        dists = []
        dist = 0.0
        for i in range(len(path) - 1):
            dists.append(metrics(routers[path[i]].coord, routers[path[i + 1]].coord))
            dist += dists[-1]
        green_dist = dist * rate
        cur_dist = 0.0
        not_filled_color = GREY
        if rate == 0.0:
            not_filled_color = RED
        for i in range(len(path) - 1):
            if cur_dist >= green_dist:
                pygame.draw.line(screen, not_filled_color, to_screen(routers[path[i]].coord), to_screen(routers[path[i + 1]].coord), 3)
            elif cur_dist + dists[i] <= green_dist:
                pygame.draw.line(screen, GREEN, to_screen(routers[path[i]].coord), to_screen(routers[path[i + 1]].coord), 5)
            else:
                alpha1 = (green_dist - cur_dist) / dists[i]
                alpha2 = 1 - alpha1
                coord0 = routers[path[i]].coord
                coord2 = routers[path[i + 1]].coord
                coord1 = [alpha2 * coord0[i] + alpha1 * coord2[i] for i in range(2)]
                pygame.draw.line(screen, GREEN, to_screen(coord0), to_screen(coord1), 5)
                pygame.draw.line(screen, not_filled_color, to_screen(coord1), to_screen(coord2), 3)
            cur_dist += dists[i]

    for router in routers:
        pygame.draw.circle(screen, WHITE, to_screen(router.coord), 1)

    source_color = GREEN
    destination_color = BLUE
    if rate == 0.0:
        source_color = RED
        destination_color = RED
    elif rate == 1.0:
        destination_color = GREEN

    pygame.draw.circle(screen, source_color, to_screen(routers[SOURCE_INDEX].coord), 5)
    pygame.draw.circle(screen, destination_color, to_screen(routers[DESTINATION_INDEX].coord), 5)



pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
done = False
clock = pygame.time.Clock()
routers = initialize()


while not done:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True
    connections, path, rate = step(routers)
    render(screen, routers, connections, path, rate)
    pygame.display.flip()
    clock.tick(FPS)
