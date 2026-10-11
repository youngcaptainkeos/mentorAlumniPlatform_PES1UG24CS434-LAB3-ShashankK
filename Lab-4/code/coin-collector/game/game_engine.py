"""
GameEngine: owns the player, coins, obstacles, lives, timer, and round state.
"""

import random
import pygame

from game.player import Player
from game.coin import Coin
from game.obstacle import Obstacle
from game.collection import check_collection
from game.renderer import WIDTH, HEIGHT

NUM_COINS = 8
NUM_OBSTACLES = 3
ROUND_DURATION = 30.0
INITIAL_LIVES = 3
INVULNERABILITY_DURATION = 1.5


class GameEngine:
    def __init__(self):
        self.title_font = None
        self.reset()

    def reset(self):
        """Resets the game state for a new round."""
        self.player = Player(x=WIDTH / 2, y=HEIGHT / 2)
        safe_zone = self.player.get_rect().inflate(80, 80)
        self.coins = [self._random_coin() for _ in range(NUM_COINS)]
        self.obstacles = [
            Obstacle.random_obstacle(WIDTH, HEIGHT, safe_zone=safe_zone)
            for _ in range(NUM_OBSTACLES)
        ]
        self.score = 0
        self.lives = INITIAL_LIVES
        self.time_remaining = ROUND_DURATION
        self.invulnerability_timer = 0.0
        self.frame_count = 0
        self.game_over = False
        self.game_over_reason = ""

    def _random_coin(self):
        """Spawns a random coin (Bronze, Silver, or Gold) within boundaries."""
        x = random.randint(35, WIDTH - 35)
        y = random.randint(45, HEIGHT - 35)  # Avoid top HUD area
        return Coin.random_coin(x=x, y=y)

    def handle_input(self, keys_pressed):
        # Restart check on game over
        if self.game_over:
            if keys_pressed[pygame.K_r]:
                self.reset()
            return

        dx = dy = 0
        if keys_pressed[pygame.K_UP]:
            dy -= self.player.speed
        if keys_pressed[pygame.K_DOWN]:
            dy += self.player.speed
        if keys_pressed[pygame.K_LEFT]:
            dx -= self.player.speed
        if keys_pressed[pygame.K_RIGHT]:
            dx += self.player.speed
        self.player.move(dx, dy, WIDTH, HEIGHT)

    def update(self, dt=1.0 / 60.0):
        if self.game_over:
            return

        self.frame_count += 1

        # 1. Update round countdown timer (Task 4)
        self.time_remaining -= dt
        if self.time_remaining <= 0:
            self.time_remaining = 0
            self.game_over = True
            self.game_over_reason = "Time's Up!"
            return

        # 2. Update invulnerability cooldown
        if self.invulnerability_timer > 0:
            self.invulnerability_timer = max(0.0, self.invulnerability_timer - dt)

        # 3. Task 1 & 2: Coin Collection (each coin collected exactly once and removed)
        collected = check_collection(self.player, self.coins)
        for coin in collected:
            self.score += coin.value
            self.coins.remove(coin)

        # Respawn coins to maintain dynamic play area
        while len(self.coins) < NUM_COINS:
            self.coins.append(self._random_coin())

        # 4. Task 3: Update obstacles and handle collisions
        player_rect = self.player.get_rect()
        for obstacle in self.obstacles:
            obstacle.update(WIDTH, HEIGHT)

            # Check obstacle collision with invulnerability cooldown
            if self.invulnerability_timer <= 0 and player_rect.colliderect(obstacle.get_rect()):
                self.lives -= 1
                self.invulnerability_timer = INVULNERABILITY_DURATION
                if self.lives <= 0:
                    self.lives = 0
                    self.game_over = True
                    self.game_over_reason = "Out of Lives!"
                    return

    def draw(self, surface, font):
        from game import renderer

        if self.title_font is None:
            self.title_font = pygame.font.SysFont("consolas", 34, bold=True)

        is_invuln = self.invulnerability_timer > 0
        renderer.draw_scene(
            surface,
            self.player,
            self.coins,
            self.obstacles,
            invulnerable=is_invuln,
            flicker_frame=self.frame_count,
        )
        renderer.draw_hud(surface, font, self.score, self.lives, self.time_remaining)

        if self.game_over:
            renderer.draw_game_over(
                surface, self.title_font, font, self.score, self.game_over_reason
            )

