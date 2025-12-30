"""
Wave Superposition Simulation

This script visualizes the superposition of multiple waves to demonstrate
how individual wave components combine to form a resultant wave.

The simulation is intended for conceptual understanding and visualization
of wave behavior rather than for high-precision physical modeling.
"""


import math
import random
import sys

import pygame

Clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1200, 600))
vec = pygame.Vector2
debug = False
path = False

font = pygame.font.Font('freesansbold.ttf', 20)

s = pygame.Surface(screen.get_size())


class Wave:
    def __init__(self, amp, period, phase):
        self.amp = amp
        self.period = period
        self.phase = phase

    def calc(self, x):
        self.phase += 0.00005
        return math.sin(self.phase + (x / self.period) * 2 * math.pi) * self.amp


wave = Wave(random.randint(10, 150), random.randint(100, 200), random.randint(1, 628) / 100)
waves = []
for i in range(5):
    waves.append(Wave(random.randint(5, 100), random.randint(300, 1600), random.randint(1, 628) / 100))

while True:
    dt = Clock.tick(60) * 60 / 1000
    # screen.fill((0, 0, 0))
    screen.blit(s, [0, 0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                debug = not debug
    pygame.draw.line(screen, 'blue', [0, screen.get_height() / 2], [screen.get_width(), screen.get_height() / 2], 3)
    pygame.draw.line(screen, 'red', [0, 0], [0, screen.get_height()], 5)
    for x in range(0, screen.get_width()):
        y = 0
        for wave in waves:
            y += wave.calc(x)
        pygame.draw.circle(screen, 'green', [x, y + screen.get_height() / 2], 2)
    pygame.display.set_caption(str(Clock.get_fps()))
    pygame.display.update()
