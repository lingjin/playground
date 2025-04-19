import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
GRAVITY = 0.15
BIRD_JUMP = -5
PIPE_SPEED = 1
PIPE_FREQUENCY = 2500  # milliseconds
GAP_SIZE = 150

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
SKY_BLUE = (135, 206, 235)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

# Bird class
class Bird:
    def __init__(self):
        self.x = 100
        self.y = HEIGHT // 2
        self.velocity = 0
        self.rect = pygame.Rect(self.x, self.y, 30, 30)
    
    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        self.rect.y = self.y
    
    def jump(self):
        self.velocity = BIRD_JUMP
    
    def draw(self):
        pygame.draw.rect(screen, (255, 255, 0), self.rect)  # Yellow bird

# Pipe class
class Pipe:
    def __init__(self):
        self.gap_y = random.randint(100, HEIGHT - 100 - GAP_SIZE)
        self.x = WIDTH
        self.width = 50
        self.top_rect = pygame.Rect(self.x, 0, self.width, self.gap_y)
        self.bottom_rect = pygame.Rect(self.x, self.gap_y + GAP_SIZE, self.width, HEIGHT)
        self.passed = False
    
    def update(self):
        self.x -= PIPE_SPEED
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x
    
    def draw(self):
        pygame.draw.rect(screen, GREEN, self.top_rect)
        pygame.draw.rect(screen, GREEN, self.bottom_rect)

# Game variables
bird = Bird()
pipes = []
score = 0
game_active = True
last_pipe = pygame.time.get_ticks()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird.jump()
            if event.key == pygame.K_SPACE and not game_active:
                # Reset game
                bird = Bird()
                pipes = []
                score = 0
                game_active = True
                last_pipe = pygame.time.get_ticks()
    
    screen.fill(SKY_BLUE)
    
    # Game logic
    if game_active:
        # Bird
        bird.update()
        bird.draw()
        
        # Pipes
        current_time = pygame.time.get_ticks()
        if current_time - last_pipe > PIPE_FREQUENCY:
            pipes.append(Pipe())
            last_pipe = current_time
        
        for pipe in pipes:
            pipe.update()
            pipe.draw()
            
            # Check for collision
            if pipe.top_rect.colliderect(bird.rect) or pipe.bottom_rect.colliderect(bird.rect):
                game_active = False
            
            # Score increment
            if pipe.x + pipe.width < bird.x and not pipe.passed:
                score += 1
                pipe.passed = True
        
        # Remove off-screen pipes
        pipes = [pipe for pipe in pipes if pipe.x > -pipe.width]
        
        # Floor/ceiling collision
        if bird.y <= 0 or bird.y >= HEIGHT - 30:
            game_active = False
    else:
        # Game over screen
        game_over_text = font.render("Game Over! Press SPACE to restart", True, BLACK)
        screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2))
    
    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()
    clock.tick(60)