import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Define constants for screen width and height
SCREEN_WIDTH = 360 #128
SCREEN_HEIGHT = 240 #64

# Create the Pygame display surface
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define eye parameters
ref_eye_height = 40
ref_eye_width = 40
ref_space_between_eye = 10
ref_corner_radius = 10

# Current state of the eyes
left_eye_height = ref_eye_height
left_eye_width = ref_eye_width
left_eye_x = 32
left_eye_y = 32
right_eye_x = 32 + ref_eye_width + ref_space_between_eye
right_eye_y = 32
right_eye_height = ref_eye_height
right_eye_width = ref_eye_width

# Demo mode
demo_mode = True
current_animation_index = 0
max_animation_index = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0,255,0)

# Function to draw eyes
def draw_eyes(update=True):
    screen.fill(BLACK)  # Clear the screen
    
    # Draw left eye
    left_eye_rect = pygame.Rect(left_eye_x - left_eye_width / 2, left_eye_y - left_eye_height / 2, left_eye_width, left_eye_height)
    pygame.draw.rect(screen, WHITE, left_eye_rect, border_radius=ref_corner_radius)
    
    # Draw right eye
    right_eye_rect = pygame.Rect(right_eye_x - right_eye_width / 2, right_eye_y - right_eye_height / 2, right_eye_width, right_eye_height)
    pygame.draw.rect(screen, WHITE, right_eye_rect, border_radius=ref_corner_radius)
    
    if update:
        pygame.display.update()

# Function to center eyes
def center_eyes(update=True):
    global left_eye_x, left_eye_y, right_eye_x, right_eye_y, left_eye_height, left_eye_width, right_eye_height, right_eye_width
    left_eye_x = SCREEN_WIDTH / 2 - ref_eye_width / 2 - ref_space_between_eye / 2
    left_eye_y = SCREEN_HEIGHT / 2
    right_eye_x = SCREEN_WIDTH / 2 + ref_eye_width / 2 + ref_space_between_eye / 2
    right_eye_y = SCREEN_HEIGHT / 2

    left_eye_height = ref_eye_height
    left_eye_width = ref_eye_width
    right_eye_height = ref_eye_height
    right_eye_width = ref_eye_width

    draw_eyes(update)

# Function to simulate blinking
def blink(speed=12):
    global left_eye_height, right_eye_height
    draw_eyes()

    for _ in range(3):
        left_eye_height -= speed
        right_eye_height -= speed
        draw_eyes()
        time.sleep(0.1)

    for _ in range(3):
        left_eye_height += speed
        right_eye_height += speed
        draw_eyes()
        time.sleep(0.1)

# Function to simulate sleep
def sleep():
    global left_eye_height, right_eye_height
    left_eye_height = 2
    right_eye_height = 2
    draw_eyes(True)

# Function to simulate wakeup
def wakeup():
    global left_eye_height, right_eye_height
    sleep()
    for h in range(0, ref_eye_height + 1, 2):
        left_eye_height = h
        right_eye_height = h
        draw_eyes(True)
        time.sleep(0.05)

# Function to simulate happy eyes
def happy_eye():
    center_eyes(False)
    offset = ref_eye_height // 2
    for _ in range(10):
        pygame.draw.polygon(screen, BLACK, [
            (left_eye_x - left_eye_width / 2 - 1, left_eye_y + offset),
            (left_eye_x + left_eye_width / 2 + 1, left_eye_y + 5 + offset),
            (left_eye_x - left_eye_width / 2 - 1, left_eye_y + left_eye_height + offset)
        ])
        pygame.draw.polygon(screen, BLACK, [
            (right_eye_x + right_eye_width / 2 + 1, right_eye_y + offset),
            (right_eye_x - right_eye_width / 2 - 1, right_eye_y + 5 + offset),
            (right_eye_x + right_eye_width / 2 + 1, right_eye_y + right_eye_height + offset)
        ])
        offset -= 2
        pygame.display.update()
        time.sleep(0.1)

# Function to simulate sad
def sad_eye():
    center_eyes(False)
    offset = ref_eye_height // 2
    for _ in range(10):
        # For the left eye, flip the triangle vertically by adjusting the Y-axis
        pygame.draw.polygon(screen, BLACK, [
            (left_eye_x - left_eye_width / 2 - 1, left_eye_y - offset),  # Y is now negative to flip
            (left_eye_x + left_eye_width / 2 + 1, left_eye_y - 5 - offset),  # Y is now negative to flip
            (left_eye_x - left_eye_width / 2 - 1, left_eye_y - left_eye_height - offset)  # Y is now negative to flip
        ])
        
        # For the right eye, flip the triangle vertically by adjusting the Y-axis
        pygame.draw.polygon(screen, BLACK, [
            (right_eye_x + right_eye_width / 2 + 1, right_eye_y - offset),  # Y is now negative to flip
            (right_eye_x - right_eye_width / 2 - 1, right_eye_y - 5 - offset),  # Y is now negative to flip
            (right_eye_x + right_eye_width / 2 + 1, right_eye_y - right_eye_height - offset)  # Y is now negative to flip
        ])
        offset -= 2
        pygame.display.update()
        time.sleep(0.1)


def angry_eye():
    center_eyes(False)
    offset = ref_eye_height // 2
    for _ in range(10):
        pygame.draw.polygon(screen, BLACK, [
            (left_eye_x - left_eye_width / 2 - 1, left_eye_y - 2 - offset),  
            (left_eye_x + left_eye_width / 2 + 1, left_eye_y + 6 - offset),  
            (left_eye_x - left_eye_width / 2 - 1, left_eye_y - left_eye_height - offset)
        ])
        
        pygame.draw.polygon(screen, BLACK, [
            (right_eye_x + right_eye_width / 2 + 1, right_eye_y - 2 - offset),  
            (right_eye_x - right_eye_width / 2 - 1, right_eye_y + 6 - offset),  
            (right_eye_x + right_eye_width / 2 + 1, right_eye_y - right_eye_height - offset)
        ])
        offset -= 2
        pygame.display.update()
        time.sleep(0.1)

# Function for saccade (quick eye movement)
def saccade(direction_x, direction_y):
    global left_eye_x, left_eye_y, right_eye_x, right_eye_y, left_eye_height, right_eye_height
    direction_x_movement_amplitude = 8
    direction_y_movement_amplitude = 6
    blink_amplitude = 8

    # Move eyes in one direction
    for _ in range(1):
        left_eye_x += direction_x_movement_amplitude * direction_x
        right_eye_x += direction_x_movement_amplitude * direction_x
        left_eye_y += direction_y_movement_amplitude * direction_y
        right_eye_y += direction_y_movement_amplitude * direction_y
        left_eye_height -= blink_amplitude
        right_eye_height -= blink_amplitude
        draw_eyes()
        time.sleep(0.1)

    # Move eyes back to original position
    for _ in range(1):
        left_eye_x += direction_x_movement_amplitude * direction_x
        right_eye_x += direction_x_movement_amplitude * direction_x
        left_eye_y += direction_y_movement_amplitude * direction_y
        right_eye_y += direction_y_movement_amplitude * direction_y
        left_eye_height += blink_amplitude
        right_eye_height += blink_amplitude
        draw_eyes()
        time.sleep(0.1)

# Function to execute animation based on index
def launch_animation_with_index(animation_index):
    if animation_index > max_animation_index:
        animation_index = 10

    if animation_index == 0:
        wakeup()
    elif animation_index == 1:
        center_eyes(True)
    elif animation_index == 2:
        # move_right_big_eye()  # Implement this animation
        pass
    elif animation_index == 3:
        # move_left_big_eye()  # Implement this animation
        pass
    elif animation_index == 4:
        blink(10)
    elif animation_index == 5:
        blink(20)
    elif animation_index == 6:
        happy_eye()
    elif animation_index == 7:
        sleep()
    elif animation_index == 8:
        center_eyes(True)
        for _ in range(20):
            dir_x = random.choice([-1, 0, 1])
            dir_y = random.choice([-1, 0, 1])
            saccade(dir_x, dir_y)
            time.sleep(0.1)
            saccade(-dir_x, -dir_y)
            time.sleep(0.1)
    elif animation_index == 9:
        sad_eye()

    elif animation_index == 10:
        angry_eye()


# Main loop
running = True
while running:
    screen.fill(BLACK)  # Clear the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if demo_mode:
        launch_animation_with_index(current_animation_index)
        current_animation_index += 1
        if current_animation_index > max_animation_index:
            current_animation_index = 0
        time.sleep(2)
    
    pygame.display.update()

pygame.quit()
