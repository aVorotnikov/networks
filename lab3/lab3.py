#!/bin/python3


from config import *
from topology import Topology
import pygame
import random


SOURCE_INDEX = 0
DESTINATION_INDEX = 1

WIDTH = 800
HEIGHT = WIDTH

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
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


def step(routers):
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
    return connections, paths[DESTINATION_INDEX]


def render(screen, routers, connections, path):
    screen.fill(BLACK)

    for connection in connections:
        pygame.draw.line(screen, LIGHT_GREY, to_screen(routers[connection[0]].coord), to_screen(routers[connection[1]].coord))

    if len(path) != 0:
        for i in range(len(path) - 1):
            pygame.draw.line(screen, GREY, to_screen(routers[path[i]].coord), to_screen(routers[path[i + 1]].coord), 3)

    for router in routers:
        pygame.draw.circle(screen, WHITE, to_screen(router.coord), 1)

    pygame.draw.circle(screen, BLUE, to_screen(routers[SOURCE_INDEX].coord), 5)
    pygame.draw.circle(screen, YELLOW, to_screen(routers[DESTINATION_INDEX].coord), 5)



pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
done = False
clock = pygame.time.Clock()
routers = initialize()


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        connections, path = step(routers)
        render(screen, routers, connections, path)
        pygame.display.flip()
        clock.tick(FPS)
