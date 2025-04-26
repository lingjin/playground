import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snow Plow Simulation")

# Colors
BLACK = (0, 0, 0)
ORANGE = (255, 140, 0)
DARK_ORANGE = (200, 100, 0)
GRAY = (150, 150, 150)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (80, 80, 80)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (30, 30, 150)
SILVER = (192, 192, 192)

# Truck position
truck_x = 100
truck_y = 300
truck_speed = 3

# Snow particles
snowflakes = []
for _ in range(100):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    snowflakes.append([x, y])

# Snow on ground
snow_ground = []
for x in range(0, WIDTH, 10):
    height = random.randint(5, 15)
    snow_ground.append([x, HEIGHT - 100, 10, height])

# Main loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        truck_x -= truck_speed
    if keys[pygame.K_RIGHT]:
        truck_x += truck_speed
    if keys[pygame.K_UP]:
        truck_y -= truck_speed
    if keys[pygame.K_DOWN]:
        truck_y += truck_speed
    
    # Keep truck on screen
    truck_x = max(0, min(truck_x, WIDTH - 350))
    truck_y = max(200, min(truck_y, HEIGHT - 150))
    
    # Update snow
    for snow in snowflakes:
        snow[1] += random.randint(1, 3)
        if snow[1] > HEIGHT:
            snow[1] = 0
            snow[0] = random.randint(0, WIDTH)
    
    # Clear snow where plow goes
    for snow_pile in snow_ground:
        if truck_x - 80 <= snow_pile[0] <= truck_x and truck_y + 100 <= HEIGHT - 80:
            snow_pile[3] = 0
    
    # Fill background
    screen.fill((50, 50, 100))  # Dark blue sky
    pygame.draw.rect(screen, (100, 100, 100), (0, HEIGHT - 100, WIDTH, 100))  # Road
    
    # Draw snow on ground
    for snow_pile in snow_ground:
        pygame.draw.rect(screen, WHITE, snow_pile)
    
    # Draw snow plow truck
    # Main body (truck bed)
    pygame.draw.rect(screen, ORANGE, (truck_x, truck_y, 200, 80))
    pygame.draw.rect(screen, DARK_ORANGE, (truck_x, truck_y, 200, 20))  # Top edge
    
    # Cab
    pygame.draw.rect(screen, ORANGE, (truck_x + 200, truck_y, 100, 80))
    
    # Windows
    pygame.draw.rect(screen, LIGHT_GRAY, (truck_x + 210, truck_y + 15, 80, 40))
    
    # Snow plow blade
    pygame.draw.polygon(screen, SILVER, [
        (truck_x - 70, truck_y + 100),
        (truck_x, truck_y + 40),
        (truck_x, truck_y + 100)
    ])
    pygame.draw.line(screen, DARK_GRAY, (truck_x - 70, truck_y + 100), (truck_x, truck_y + 40), 5)
    pygame.draw.line(screen, DARK_GRAY, (truck_x, truck_y + 40), (truck_x, truck_y + 100), 5)
    
    # Salt spreader
    pygame.draw.rect(screen, DARK_GRAY, (truck_x + 50, truck_y + 80, 100, 20))
    pygame.draw.polygon(screen, DARK_GRAY, [
        (truck_x + 50, truck_y + 80),
        (truck_x + 150, truck_y + 80),
        (truck_x + 130, truck_y + 60),
        (truck_x + 70, truck_y + 60)
    ])
    
    # Wheels
    pygame.draw.circle(screen, BLACK, (truck_x + 50, truck_y + 120), 20)
    pygame.draw.circle(screen, BLACK, (truck_x + 150, truck_y + 120), 20)
    pygame.draw.circle(screen, BLACK, (truck_x + 250, truck_y + 120), 20)
    
    # Wheel rims
    pygame.draw.circle(screen, GRAY, (truck_x + 50, truck_y + 120), 10)
    pygame.draw.circle(screen, GRAY, (truck_x + 150, truck_y + 120), 10)
    pygame.draw.circle(screen, GRAY, (truck_x + 250, truck_y + 120), 10)
    
    # Warning lights
    pygame.draw.circle(screen, YELLOW, (truck_x + 20, truck_y - 10), 7)
    pygame.draw.circle(screen, YELLOW, (truck_x + 80, truck_y - 10), 7)
    pygame.draw.circle(screen, YELLOW, (truck_x + 140, truck_y - 10), 7)
    pygame.draw.circle(screen, YELLOW, (truck_x + 200, truck_y - 10), 7)
    pygame.draw.circle(screen, YELLOW, (truck_x + 260, truck_y - 10), 7)
    
    # Draw snowflakes
    for snow in snowflakes:
        pygame.draw.circle(screen, WHITE, snow, 2)
    
    # Update display
    pygame.display.flip()
    clock.tick(60)

# Quit
pygame.quit()
sys.exit()