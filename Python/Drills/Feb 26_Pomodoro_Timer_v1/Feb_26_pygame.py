import pygame
import sys

# ---------- SETTINGS ----------
WORK_TIME = 25  # 25 Minutes
BREAK_TIME = 5  # 5  Minutes
WIDTH, HEIGHT = 800, 400 # X, Y
# ------------------------------
WORK_TIME = WORK_TIME*60
BREAK_TIME = BREAK_TIME*60
# ------------------------------

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pomodoro Timer")

font = pygame.font.SysFont("Arial", 120)
small_font = pygame.font.SysFont("Arial", 40)

clock = pygame.time.Clock()

is_work = True
running_timer = False
start_ticks = 0
paused_time = 0

current_duration = WORK_TIME

def format_time(seconds):
    mins = seconds // 60
    secs = seconds % 60
    return f"{mins:02}:{secs:02}"

while True:
    screen.fill((20, 20, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not running_timer:
                    running_timer = True
                    start_ticks = pygame.time.get_ticks() - paused_time
                else:
                    running_timer = False
                    paused_time = pygame.time.get_ticks() - start_ticks

    if running_timer:
        elapsed_ms = pygame.time.get_ticks() - start_ticks
        elapsed_seconds = elapsed_ms // 1000
        remaining = max(0, current_duration - elapsed_seconds)

        if remaining == 0:
            is_work = not is_work
            current_duration = WORK_TIME if is_work else BREAK_TIME
            start_ticks = pygame.time.get_ticks()
            paused_time = 0
    else:
        elapsed_seconds = paused_time // 1000
        remaining = max(0, current_duration - elapsed_seconds)

    timer_text = font.render(format_time(remaining), True, (255, 255, 255))
    mode_text = small_font.render("WORK" if is_work else "BREAK", True, (100, 200, 255))

    screen.blit(timer_text, (WIDTH//2 - timer_text.get_width()//2, HEIGHT//2 - 80))
    screen.blit(mode_text, (WIDTH//2 - mode_text.get_width()//2, HEIGHT//2 + 60))

    pygame.display.flip()
    clock.tick(60)