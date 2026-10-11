"""
Obstacle: dynamic hazards in the play area that damage the player on contact.
"""

import random
import pygame


class Obstacle:
    def __init__(self, x, y, width=28, height=28, vx=2, vy=2, color=(230, 57, 70)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vx = vx
        self.vy = vy
        self.color = color

    def update(self, bounds_width, bounds_height):
        """Move the obstacle and bounce off boundary walls."""
        self.x += self.vx
        self.y += self.vy

        half_w = self.width / 2
        half_h = self.height / 2

        if self.x - half_w <= 0:
            self.x = half_w
            self.vx = abs(self.vx)
        elif self.x + half_w >= bounds_width:
            self.x = bounds_width - half_w
            self.vx = -abs(self.vx)

        if self.y - half_h <= 0:
            self.y = half_h
            self.vy = abs(self.vy)
        elif self.y + half_h >= bounds_height:
            self.y = bounds_height - half_h
            self.vy = -abs(self.vy)

    def get_rect(self):
        return pygame.Rect(
            int(self.x - self.width / 2),
            int(self.y - self.height / 2),
            self.width,
            self.height,
        )

    @classmethod
    def random_obstacle(cls, bounds_width, bounds_height, safe_zone=None):
        """Creates a randomized obstacle outside the player's initial safe zone."""
        while True:
            x = random.randint(40, bounds_width - 40)
            y = random.randint(40, bounds_height - 40)
            rect = pygame.Rect(x - 14, y - 14, 28, 28)
            if safe_zone is None or not rect.colliderect(safe_zone):
                break

        # Random velocity between 1.5 and 3.0 in each axis
        vx = random.choice([-2.5, -2.0, -1.5, 1.5, 2.0, 2.5])
        vy = random.choice([-2.5, -2.0, -1.5, 1.5, 2.0, 2.5])
        return cls(x=x, y=y, vx=vx, vy=vy)
