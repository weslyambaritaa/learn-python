import pygame
import math

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Bouncing Ihnside Spinning Hexagon")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Physics constants
g = 0.5  # Gravity
friction = 0.98  # Friction
bounce = 0.8  # Coefficient of restitution

# Ball properties
ball_radius = 10
ball_x, ball_y = WIDTH // 2, HEIGHT // 4
ball_vx, ball_vy = 2, 0

# Hexagon properties
hexagon_radius = 300
hexagon_angle = 0
hexagon_rotation_speed = 1  # Degrees per frame

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Function to calculate hexagon vertices
def get_hexagon_vertices(center_x, center_y, radius, angle):
    vertices = []
    for i in range(6):
        theta = math.radians(angle + i * 60)
        x = center_x + radius * math.cos(theta)
        y = center_y + radius * math.sin(theta)
        vertices.append((x, y))
    return vertices

# Function to reflect the ball off a wall
def reflect_ball(normal_x, normal_y):
    global ball_vx, ball_vy
    normal_length = math.sqrt(normal_x**2 + normal_y**2)
    nx, ny = normal_x / normal_length, normal_y / normal_length
    dot_product = ball_vx * nx + ball_vy * ny
    ball_vx -= 2 * dot_product * nx
    ball_vy -= 2 * dot_product * ny
    ball_vx *= friction
    ball_vy *= friction

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update ball position
    ball_vy += g
    ball_x += ball_vx
    ball_y += ball_vy

    # Get hexagon vertices and rotate it
    hexagon_angle += hexagon_rotation_speed
    vertices = get_hexagon_vertices(WIDTH // 2, HEIGHT // 2, hexagon_radius, hexagon_angle)

    # Check for collisions with hexagon walls
    for i in range(6):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % 6]

        # Line equation parameters
        dx, dy = x2 - x1, y2 - y1
        wall_length = math.sqrt(dx**2 + dy**2)
        nx, ny = -dy / wall_length, dx / wall_length  # Wall normal

        # Ball-to-line distance
        dist = abs((ball_x - x1) * ny - (ball_y - y1) * nx)

        # Collision check
        if dist <= ball_radius:
            reflect_ball(nx, ny)

            # Prevent ball from sticking to wall
            overlap = ball_radius - dist
            ball_x += nx * overlap
            ball_y += ny * overlap

    # Draw hexagon
    pygame.draw.polygon(screen, WHITE, vertices, 2)

    # Draw ball
    pygame.draw.circle(screen, RED, (int(ball_x), int(ball_y)), ball_radius)

    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

pygame.quit()