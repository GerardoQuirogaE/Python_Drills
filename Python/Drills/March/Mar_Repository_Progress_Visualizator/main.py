import pygame
import pygame.gfxdraw
from sys import exit
import math
import random
import time


class FileNode:
    def __init__(self, name, x, y, created_at, parent=None, angle=0):
        self.name = name

        self.parent = parent
        self.angle = angle  # preferred angular position
        self.distance = 100  # preferred distance from parent

        self.x = x
        self.y = y

        self.vx = 0
        self.vy = 0

        self.radius = 1
        self.target_radius = 20

        self.created_at = created_at
        self.birth_time = time.time()

        self.float_offset = random.uniform(0, 2 * math.pi)

    def update(self):
        t = time.time() - self.birth_time

        # 🌊 Small floating force
        float_fx = math.sin(t + self.float_offset) * 0.02
        float_fy = math.cos(t + self.float_offset) * 0.02

        self.vx += float_fx
        self.vy += float_fy

        # 🔗 Parent attraction
        if self.parent:
            target_x = self.parent.x + math.cos(self.angle) * self.distance
            target_y = self.parent.y + math.sin(self.angle) * self.distance

            dx = target_x - self.x
            dy = target_y - self.y

            self.vx += dx * 0.01
            self.vy += dy * 0.01

        # Damping
        self.vx *= 0.93
        self.vy *= 0.93

        self.x += self.vx
        self.y += self.vy

        # 🌱 Smooth growth
        if self.radius < self.target_radius:
            self.radius += (self.target_radius - self.radius) * 0.1

    def draw(self, surface):
        pygame.gfxdraw.filled_circle(surface, int(self.x), int(self.y), int(self.radius), (70,130,180))
        pygame.gfxdraw.aacircle(surface, int(self.x), int(self.y), int(self.radius), (70,130,180))

        # Draw connection line if parent exists
        if self.parent:
            pygame.draw.line(surface, (180,180,180),
                             (int(self.x), int(self.y)),
                             (int(self.parent.x), int(self.parent.y)), 1)

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Repo Visualizer")
clock = pygame.time.Clock()

font = pygame.font.Font("./font/Pixeltype.ttf",50)

# Title text and surface
text_surf = font.render("Repo Data Visualizer", False, (64,64,64)).convert_alpha()
text_rec = text_surf.get_rect(center = (400, 50))

# 
parent = FileNode("Drills", 400, 200, time.time())

children = []
num_children = 5

for i in range(num_children):
    angle = (2 * math.pi / num_children) * i
    child = FileNode(
        f"file_{i}.py",
        400,
        200,
        time.time(),
        parent=parent,
        angle=angle
    )
    children.append(child)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((255, 255, 255)) 
    screen.blit(text_surf, text_rec)

    parent.update()
    parent.draw(screen)

    for child in children:
        child.update()
        child.draw(screen)

    pygame.display.update()
    clock.tick(120)