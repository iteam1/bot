import pygame
import random
import time

# Pygame initialization
pygame.init()

# Constants
SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Display setup
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Eye Animation')

# Eye constants
ref_eye_height = 40
ref_eye_width = 40
ref_space_between_eye = 10
ref_corner_radius = 10

# Initial eye positions
left_eye_x = 32
left_eye_y = 32
right_eye_x = 32 + ref_eye_width + ref_space_between_eye
right_eye_y = 32
left_eye_height = ref_eye_height
right_eye_height = ref_eye_height
left_eye_width = ref_eye_width
right_eye_width = ref_eye_width

# Animation state
demo_mode = 1
max_animation_index = 8
current_animation_index = 0

# Function to draw the eyes
def draw_eyes():
    screen.fill(BLACK)
    # Draw left eye
    pygame.draw.rect(screen, WHITE, (left_eye_x - left_eye_width // 2, left_eye_y - left_eye_height // 2, left_eye_width, left_eye_height), border_radius=ref_corner_radius)
    # Draw right eye
    pygame.draw.rect(screen, WHITE, (right_eye_x - right_eye_width // 2, right_eye_y - right_eye_height // 2, right_eye_width, right_eye_height), border_radius=ref_corner_radius)
    pygame.display.update()

# Function to center the eyes
def center_eyes():
    global left_eye_x, left_eye_y, right_eye_x, right_eye_y, left_eye_height, right_eye_height
    left_eye_x = SCREEN_WIDTH // 2 - ref_eye_width // 2 - ref_space_between_eye // 2
    left_eye_y = SCREEN_HEIGHT // 2
    right_eye_x = SCREEN_WIDTH // 2 + ref_eye_width // 2 + ref_space_between_eye // 2
    right_eye_y = SCREEN_HEIGHT // 2
    left_eye_height = ref_eye_height
    right_eye_height = ref_eye_height
    draw_eyes()

# Function for blinking animation
def blink(speed=12):
    global left_eye_height, right_eye_height
    draw_eyes()
    for _ in range(3):
        left_eye_height -= speed
        right_eye_height -= speed
        draw_eyes()
        time.sleep(0.01)
    for _ in range(3):
        left_eye_height += speed
        right_eye_height += speed
        draw_eyes()
        time.sleep(0.01)

# Function for "sleep" animation
def sleep():
    global left_eye_height, right_eye_height
    left_eye_height = 2
    right_eye_height = 2
    draw_eyes()

# Function for "wake up" animation
def wakeup():
    sleep()
    for h in range(0, ref_eye_height + 1, 2):
        global left_eye_height, right_eye_height
        left_eye_height = h
        right_eye_height = h
        draw_eyes()
        time.sleep(0.05)

# Function to simulate "happy eyes"
def happy_eye():
    center_eyes()
    offset = ref_eye_height // 2
    for _ in range(10):
        pygame.draw.polygon(screen, BLACK, [
            (left_eye_x - left_eye_width // 2 - 1, left_eye_y + offset),
            (left_eye_x + left_eye_width // 2 + 1, left_eye_y + 5 + offset),
            (left_eye_x - left_eye_width // 2 - 1, left_eye_y + left_eye_height + offset)
        ])
        pygame.draw.polygon(screen, BLACK, [
            (right_eye_x + right_eye_width // 2 + 1, right_eye_y + offset),
            (right_eye_x - left_eye_width // 2 - 1, right_eye_y + 5 + offset),
            (right_eye_x + right_eye_width // 2 + 1, right_eye_y + right_eye_height + offset)
        ])
        offset -= 2
        pygame.display.update()
        time.sleep(0.01)
    time.sleep(1)

# Function for saccade (quick movement of the eyes)
def saccade(direction_x, direction_y):
    global left_eye_x, right_eye_x, left_eye_y, right_eye_y, left_eye_height, right_eye_height
    direction_x_movement_amplitude = 8
    direction_y_movement_amplitude = 6
    blink_amplitude = 8

    left_eye_x += direction_x * direction_x_movement_amplitude
    right_eye_x += direction_x * direction_x_movement_amplitude
    left_eye_y += direction_y * direction_y_movement_amplitude
    right_eye_y += direction_y * direction_y_movement_amplitude
    left_eye_height -= blink_amplitude
    right_eye_height -= blink_amplitude
    draw_eyes()

    left_eye_x += direction_x * direction_x_movement_amplitude
    right_eye_x += direction_x * direction_x_movement_amplitude
    left_eye_y += direction_y * direction_y_movement_amplitude
    right_eye_y += direction_y * direction_y_movement_amplitude
    left_eye_height += blink_amplitude
    right_eye_height += blink_amplitude
    draw_eyes()

# Function to trigger animation based on index
def launch_animation_with_index(animation_index):
    global current_animation_index
    if animation_index > max_animation_index:
        animation_index = 8
    if animation_index == 0:
        wakeup()
    elif animation_index == 1:
        center_eyes()
    elif animation_index == 2:
        blink(10)
    elif animation_index == 3:
        blink(20)
    elif animation_index == 4:
        happy_eye()
    elif animation_index == 5:
        sleep()
    elif animation_index == 6:
        saccade(1, 0)
    elif animation_index == 7:
        saccade(-1, 0)
    elif animation_index == 8:
        center_eyes()
        for _ in range(20):
            dir_x = random.choice([-1, 0, 1])
            dir_y = random.choice([-1, 0, 1])
            saccade(dir_x, dir_y)
            time.sleep(0.01)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if demo_mode == 1:
        launch_animation_with_index(current_animation_index)
        current_animation_index += 1
        if current_animation_index > max_animation_index:
            current_animation_index = 0

    pygame.display.update()
    time.sleep(0.5)

pygame.quit()
