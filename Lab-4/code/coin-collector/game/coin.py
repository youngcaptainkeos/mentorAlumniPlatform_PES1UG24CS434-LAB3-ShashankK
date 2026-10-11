"""
Coin: a static collectible circle. Drawn as a circle, hit-tested as a
bounding square around it. Supports multiple coin types (Bronze, Silver, Gold).
"""

import random
import pygame


class Coin:
    TYPES = {
        "bronze": {"value": 1, "color": (205, 127, 50), "radius": 10, "name": "Bronze"},
        "silver": {"value": 3, "color": (192, 192, 192), "radius": 13, "name": "Silver"},
        "gold":   {"value": 5, "color": (255, 215, 0),   "radius": 16, "name": "Gold"},
    }

    def __init__(self, x, y, coin_type="bronze", radius=None, value=None, color=None):
        self.x = x
        self.y = y
        self.coin_type = coin_type
        
        cfg = self.TYPES.get(coin_type, self.TYPES["bronze"])
        self.value = value if value is not None else cfg["value"]
        self.color = color if color is not None else cfg["color"]
        self.radius = radius if radius is not None else cfg["radius"]

    def get_rect(self):
        return pygame.Rect(
            int(self.x - self.radius), int(self.y - self.radius),
            self.radius * 2, self.radius * 2,
        )

    @classmethod
    def random_coin(cls, x, y):
        """Creates a randomized coin (Bronze 50%, Silver 35%, Gold 15%)."""
        choice = random.choices(["bronze", "silver", "gold"], weights=[50, 35, 15], k=1)[0]
        return cls(x=x, y=y, coin_type=choice)
