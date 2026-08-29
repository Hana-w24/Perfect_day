import pygame
import random

# -----------------------------
# Setup
# -----------------------------

pygame.init()

WIDTH = 945
HEIGHT = 540

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Apple Game")

clock = pygame.time.Clock()

# Colours
POWDER_BLUE = (176, 224, 230)
LAWN_GREEN = (124, 252, 0)
BROWN = (139, 69, 19)
BLACK = (0, 0, 0)

# -----------------------------
# Load images
# -----------------------------

apple_image = pygame.image.load("Images/apple.png").convert_alpha()
apple_image = pygame.transform.scale(apple_image, (21, 25))

splat_image = pygame.image.load("Images/apple2.png").convert_alpha()
splat_image = pygame.transform.scale(splat_image, (21, 16))

tree_image = pygame.image.load("Images/apple_tree.png").convert_alpha()
tree_image = pygame.transform.scale(tree_image, (285, 345))

# -----------------------------
# Bucket1
# -----------------------------

bucket = pygame.Rect(480, 395, 75, 60)

# -----------------------------
# Apples
# -----------------------------

apples = []
splats = []

APPLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(APPLE_EVENT, 1000)

# -----------------------------
# Score
# -----------------------------

score = 0
font = pygame.font.SysFont("Arial", 24)

# -----------------------------
# Main game loop
# -----------------------------

running = True

while running:

    # -------------------------
    # Events
    # -------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Create a new apple every second
        if event.type == APPLE_EVENT:

            tree = random.randint(1, 2)

            if tree == 1:
                x = random.randint(113, 300)
                y = random.randint(75, 173)
            else:
                x = random.randint(638, 825)
                y = random.randint(75, 173)

            apple_rect = apple_image.get_rect(topleft=(x, y))

            apples.append({
                "rect": apple_rect,
                "speed": 5
            })

    # -------------------------
    # Keyboard controls
    # -------------------------

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if bucket.x > 7:
            bucket.x -= 20

    if keys[pygame.K_RIGHT]:
        if bucket.x < 877:
            bucket.x += 20

    # -------------------------
    # Move apples
    # -------------------------

    for apple in apples[:]:

        apple["rect"].y += apple["speed"]

        # Apple reaches bucket/ground
        if apple["rect"].y > 395:

            # Check whether bucket catches the apple
            if bucket.colliderect(apple["rect"]):
                score += 1

            else:
                score -= 1

                # Store splat position
                splat_rect = splat_image.get_rect(center=apple["rect"].center)
                splats.append(splat_rect)

            # Remove apple (once, after the if/else)
            apples.remove(apple)

    # -------------------------
    # Draw background
    # -------------------------

    screen.fill(POWDER_BLUE)

    # Draw splats
    for splat_rect in splats:
        screen.blit(splat_image, splat_rect)

    # Ground
    pygame.draw.rect(
        screen,
        LAWN_GREEN,
        (0, 300, WIDTH, 240)
    )

    # Trees
    screen.blit(tree_image, (210, 210))
    screen.blit(tree_image, (735, 210))

    # -------------------------
    # Draw apples
    # -------------------------

    for apple in apples:
        screen.blit(
            apple_image,
            apple["rect"]
        )

    # -------------------------
    # Draw bucket
    # -------------------------

    pygame.draw.rect(
        screen,
        BROWN,
        bucket
    )

    # -------------------------
    # Draw score
    # -------------------------

    score_text = font.render(
        "Score: " + str(score),
        True,
        BLACK
    )

    screen.blit(
        score_text,
        (484, 90)
    )

    # -------------------------
    # Update screen
    # -------------------------

    pygame.display.flip()

    clock.tick(60)


pygame.quit()