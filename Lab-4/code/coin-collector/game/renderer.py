"""
renderer: all pygame drawing lives here, kept separate from game logic.
"""

import pygame

WIDTH, HEIGHT = 700, 500
WINDOW_SIZE = (WIDTH, HEIGHT)

COLOR_BG = (28, 32, 38)
COLOR_PLAYER = (80, 180, 255)
COLOR_PLAYER_INVULN = (160, 220, 255)
COLOR_TEXT = (255, 255, 255)
COLOR_OBSTACLE = (235, 60, 60)
COLOR_OBSTACLE_BORDER = (255, 120, 120)


def draw_scene(surface, player, coins, obstacles=None, invulnerable=False, flicker_frame=0):
    surface.fill(COLOR_BG)

    # Draw border around the play area
    pygame.draw.rect(surface, (45, 55, 65), (0, 0, WIDTH, HEIGHT), width=3)

    # Draw coins with outer rim
    for coin in coins:
        cx, cy, r = int(coin.x), int(coin.y), coin.radius
        pygame.draw.circle(surface, coin.color, (cx, cy), r)
        pygame.draw.circle(surface, (255, 255, 255), (cx, cy), r, width=1)
        # Inner highlight
        pygame.draw.circle(surface, (255, 255, 255, 80), (cx - r // 3, cy - r // 3), max(2, r // 4))

    # Draw obstacles
    if obstacles:
        for obs in obstacles:
            r = obs.get_rect()
            pygame.draw.rect(surface, COLOR_OBSTACLE, r, border_radius=6)
            pygame.draw.rect(surface, COLOR_OBSTACLE_BORDER, r, width=2, border_radius=6)
            # Hazard cross in center
            pygame.draw.line(surface, (255, 255, 255), (r.left + 5, r.top + 5), (r.right - 5, r.bottom - 5), width=2)
            pygame.draw.line(surface, (255, 255, 255), (r.left + 5, r.bottom - 5), (r.right - 5, r.top + 5), width=2)

    # Draw player (flickers if invulnerable)
    if not invulnerable or (flicker_frame % 2 == 0):
        color = COLOR_PLAYER_INVULN if invulnerable else COLOR_PLAYER
        pygame.draw.rect(surface, color, player.get_rect(), border_radius=5)
        pygame.draw.rect(surface, (255, 255, 255), player.get_rect(), width=1, border_radius=5)


def draw_hud(surface, font, score, lives, time_remaining):
    # Top bar background panel
    hud_bg = pygame.Surface((WIDTH, 42), pygame.SRCALPHA)
    hud_bg.fill((15, 20, 25, 200))
    surface.blit(hud_bg, (0, 0))

    # Score
    draw_text(surface, font, f"Score: {score}", (16, 10), (255, 215, 0))

    # Timer (turns red when under 5s)
    timer_color = (255, 80, 80) if time_remaining <= 5.0 else (255, 255, 255)
    timer_str = f"Time: {max(0.0, time_remaining):.1f}s"
    t_surf = font.render(timer_str, True, timer_color)
    surface.blit(t_surf, (WIDTH // 2 - t_surf.get_width() // 2, 10))

    # Lives
    hearts = "♥ " * lives
    lives_str = f"Lives: {hearts.strip() if lives > 0 else 'None'}"
    l_surf = font.render(lives_str, True, (255, 80, 80) if lives <= 1 else (100, 255, 120))
    surface.blit(l_surf, (WIDTH - l_surf.get_width() - 16, 10))


def draw_game_over(surface, title_font, body_font, score, reason="Time's Up!"):
    # Overlay darkening
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    surface.blit(overlay, (0, 0))

    # Center card panel
    card = pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2 - 130, 400, 260)
    pygame.draw.rect(surface, (30, 36, 45), card, border_radius=12)
    pygame.draw.rect(surface, (80, 140, 200), card, width=2, border_radius=12)

    # Title
    title_text = "ROUND OVER" if "Time" in reason else "GAME OVER"
    title_surf = title_font.render(title_text, True, (255, 215, 0) if "Time" in reason else (255, 90, 90))
    surface.blit(title_surf, title_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 75)))

    # Reason
    sub_surf = body_font.render(reason, True, (200, 200, 200))
    surface.blit(sub_surf, sub_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 35)))

    # Final Score
    score_surf = title_font.render(f"Final Score: {score}", True, (255, 255, 255))
    surface.blit(score_surf, score_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10)))

    # Restart Prompt
    prompt_surf = body_font.render("Press [R] to Play Again", True, (80, 220, 120))
    surface.blit(prompt_surf, prompt_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 65)))

    quit_surf = body_font.render("Press [ESC] to Quit", True, (150, 150, 150))
    surface.blit(quit_surf, quit_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 95)))


def draw_text(surface, font, text, pos, color=COLOR_TEXT):
    surface.blit(font.render(text, True, color), pos)

