import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Train Simulation")

# Colors
BLACK = (0, 0, 0)
RED = (180, 0, 0)
BLUE = (0, 0, 180)
GREEN = (0, 120, 0)
YELLOW = (255, 215, 0)
BROWN = (139, 69, 19)
GRAY = (150, 150, 150)
DARK_GRAY = (80, 80, 80)
WHITE = (255, 255, 255)
SKY_BLUE = (135, 206, 235)

# Train properties
train_x = -400
train_speed = 2
direction = 1  # 1 for right, -1 for left
num_passenger_cars = 4
car_colors = [BLUE, GREEN, YELLOW, RED]

# Smoke particles
smoke_particles = []

# Function to draw the locomotive
def draw_locomotive(x, y):
    # Main body
    pygame.draw.rect(screen, BLACK, (x, y, 150, 60))
    
    # Cabin
    pygame.draw.rect(screen, RED, (x + 100, y - 30, 50, 30))
    pygame.draw.rect(screen, WHITE, (x + 110, y - 20, 30, 15))  # Window
    
    # Chimney
    pygame.draw.rect(screen, BLACK, (x + 120, y - 60, 20, 30))
    
    # Front
    pygame.draw.rect(screen, RED, (x, y + 10, 30, 50))
    
    # Wheels
    pygame.draw.circle(screen, BLACK, (x + 30, y + 70), 15)
    pygame.draw.circle(screen, BLACK, (x + 70, y + 70), 15)
    pygame.draw.circle(screen, BLACK, (x + 110, y + 70), 15)
    pygame.draw.circle(screen, BLACK, (x + 140, y + 70), 15)
    
    # Wheel details
    pygame.draw.circle(screen, GRAY, (x + 30, y + 70), 8)
    pygame.draw.circle(screen, GRAY, (x + 70, y + 70), 8)
    pygame.draw.circle(screen, GRAY, (x + 110, y + 70), 8)
    pygame.draw.circle(screen, GRAY, (x + 140, y + 70), 8)
    
    # Coupling
    pygame.draw.rect(screen, BLACK, (x + 150, y + 40, 10, 5))
    
    # Add smoke
    if len(smoke_particles) < 20 and pygame.time.get_ticks() % 10 == 0:
        smoke_particles.append([x + 130, y - 60, 5])

# Function to draw a passenger car
def draw_passenger_car(x, y, color):
    # Main body
    pygame.draw.rect(screen, color, (x, y + 10, 120, 50))
    
    # Windows
    for i in range(4):
        pygame.draw.rect(screen, WHITE, (x + 15 + i * 25, y + 20, 15, 15))
    
    # Wheels
    pygame.draw.circle(screen, BLACK, (x + 30, y + 70), 15)
    pygame.draw.circle(screen, BLACK, (x + 90, y + 70), 15)
    
    # Wheel details
    pygame.draw.circle(screen, GRAY, (x + 30, y + 70), 8)
    pygame.draw.circle(screen, GRAY, (x + 90, y + 70), 8)
    
    # Couplings
    pygame.draw.rect(screen, BLACK, (x - 10, y + 40, 10, 5))
    pygame.draw.rect(screen, BLACK, (x + 120, y + 40, 10, 5))

# Function to update and draw smoke
def update_smoke():
    for i, smoke in enumerate(smoke_particles):
        # Move smoke up and slightly in wind direction
        smoke[0] += 0.5
        smoke[1] -= 1
        smoke[2] += 0.2  # Grow in size
        
        # Draw smoke
        pygame.draw.circle(screen, (200, 200, 200), (int(smoke[0]), int(smoke[1])), int(smoke[2]))
        
        # Remove old smoke
        if smoke[2] > 15:
            smoke_particles.pop(i)
            if i >= len(smoke_particles):
                break

# Main loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Change direction
                direction *= -1
                train_speed *= -1
    
    # Move train
    train_x += train_speed
    
    # Reset train position when it goes off screen
    if direction == 1 and train_x > WIDTH + 200:
        train_x = -800
    elif direction == -1 and train_x < -800:
        train_x = WIDTH + 200
    
    # Fill background
    screen.fill(SKY_BLUE)
    
    # Draw sun
    pygame.draw.circle(screen, YELLOW, (100, 100), 40)
    
    # Draw hills
    pygame.draw.ellipse(screen, GREEN, (50, HEIGHT - 300, 400, 250))
    pygame.draw.ellipse(screen, GREEN, (400, HEIGHT - 250, 500, 200))
    pygame.draw.ellipse(screen, GREEN, (700, HEIGHT - 280, 400, 230))
    
    # Draw ground
    pygame.draw.rect(screen, BROWN, (0, HEIGHT - 100, WIDTH, 30))
    pygame.draw.rect(screen, GRAY, (0, HEIGHT - 70, WIDTH, 70))
    
    # Draw tracks
    pygame.draw.rect(screen, DARK_GRAY, (0, HEIGHT - 85, WIDTH, 5))
    pygame.draw.rect(screen, DARK_GRAY, (0, HEIGHT - 70, WIDTH, 5))
    for i in range(0, WIDTH, 20):
        pygame.draw.rect(screen, DARK_GRAY, (i, HEIGHT - 85, 3, 20))
    
    # Draw locomotive
    if direction == 1:
        draw_locomotive(train_x, HEIGHT - 150)
    else:
        # For the opposite direction, we need to flip the locomotive drawing
        draw_locomotive(train_x + 150, HEIGHT - 150)
    
    # Draw passenger cars
    for i in range(num_passenger_cars):
        car_x = train_x + 180 + (i * 140) if direction == 1 else train_x - 140 - (i * 140)
        draw_passenger_car(car_x, HEIGHT - 150, car_colors[i % len(car_colors)])
    
    # Update and draw smoke
    update_smoke()
    
    # Update display
    pygame.display.flip()
    clock.tick(60)

# Quit
pygame.quit()
sys.exit()
