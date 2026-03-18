import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rook Dodging Pawns")

# Load images
rook_img = pygame.image.load("rook.png")
pawn_img = pygame.image.load("pawn.png")

# Scale images
size_xy=(random.randint(5,100))
rook_img = pygame.transform.scale(rook_img, (50, 50))
pawn_img = pygame.transform.scale(pawn_img, (size_xy, size_xy))

# Rook setup
rook_x = WIDTH // 2
rook_y = HEIGHT - 100
rook_speed = 7  # smaller speed for smoother movement
rook_velocity = 0

# Pawn setup
pawn_speed = size_xy
pawns = []
pawn_spawn_time = 30  # frames
frame_count = 0

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Game loop
colr=random.randint(0,255)
colg=
colb
running = True

while running:
    screen.fill((0, 255, 255))  # cyan background

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Smooth movement: adjust velocity on key down/up
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                rook_velocity = -rook_speed
            elif event.key == pygame.K_d:
                rook_velocity = rook_speed
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_a, pygame.K_d):
                rook_velocity = 0

    # Update rook position
    rook_x += rook_velocity
    if rook_x < 0:
        rook_x = 0
    elif rook_x > WIDTH - 50:
        rook_x = WIDTH - 50

    # Increase difficulty as score increases
    pawn_speed = 5 + score // 5  # pawns fall faster every 5 points
    pawn_spawn_time = max(10, 30 - score // 3)  # spawn more often, min 10 frames

    # Spawn pawns
    frame_count += 1
    if frame_count >= pawn_spawn_time:
        pawn_x = random.randint(0, WIDTH - 50)
        pawns.append(pygame.Rect(pawn_x, -50, 50, 50))
        frame_count = 0

    # Move pawns
    for pawn in pawns[:]:
        pawn.y += pawn_speed
        if pawn.y > HEIGHT:
            pawns.remove(pawn)
            score += 1  # Increment score for dodged pawn

    # Draw pawns
    for pawn in pawns:
        screen.blit(pawn_img, (pawn.x, pawn.y))

    # Draw rook
    rook_rect = pygame.Rect(rook_x, rook_y, 50, 50)
    screen.blit(rook_img, (rook_x, rook_y))

    # Collision detection
    for pawn in pawns:
        if rook_rect.colliderect(pawn):
            print(f"Your score: {score}")
            running = False  # End game immediately

    # Draw score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
