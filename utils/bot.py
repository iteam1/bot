import pygame
import sys
import time

# Initialize pygame
pygame.init()

# Initial screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 400

# Colors
BLACK = (0, 0, 0)
EYE_COLOR = (0, 255, 0)  # Single color for the eyes (green)
WHITE = (255, 255, 255)  # White for inner anime-style highlights
TEXT_COLOR = (255, 255, 255)  # Text color (white)

# Screen setup with resizable option
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Cute Anime Robot Eyes")

# Font setup
FONT = pygame.font.Font(None, 50)  # Default font with size 50

# Function to calculate eye properties based on current screen dimensions
def calculate_eye_properties(width, height):
    eye_width = width // 8  # Eye width is 1/8th of the screen width
    eye_height = height // 3  # Eye height is 1/3rd of the screen height
    left_eye_center = (width // 3, height // 2)  # Position the left eye
    right_eye_center = (2 * width // 3, height // 2)  # Position the right eye
    return eye_width, eye_height, left_eye_center, right_eye_center

# Function to draw an anime-style eye
def draw_anime_eye(center, width, height, emotion):
    if emotion == "neutral":
        # Base eye shape
        pygame.draw.ellipse(screen, EYE_COLOR, (center[0] - width // 2,
                                                center[1] - height // 2,
                                                width, height))
        # Inner highlight for cuteness
        pygame.draw.ellipse(screen, WHITE, (center[0] - width // 4,
                                            center[1] - height // 4,
                                            width // 4, height // 4))
    elif emotion == "blink":
        # Blink (narrow horizontal line)
        pygame.draw.rect(screen, EYE_COLOR, (center[0] - width // 2,
                                             center[1] - 10,  # Narrow the height
                                             width, 20))


# Function to display neutral emotion
def draw_neutral(eye_width, eye_height, left_eye_center, right_eye_center):
    screen.fill(BLACK)
    draw_anime_eye(left_eye_center, eye_width, eye_height, "neutral")
    draw_anime_eye(right_eye_center, eye_width, eye_height, "neutral")
    pygame.display.flip()


# Function to display blink emotion
def draw_blink(eye_width, eye_height, left_eye_center, right_eye_center):
    screen.fill(BLACK)
    draw_anime_eye(left_eye_center, eye_width, eye_height, "blink")
    draw_anime_eye(right_eye_center, eye_width, eye_height, "blink")
    pygame.display.flip()
    time.sleep(0.2)  # Briefly hold the blink
    draw_neutral(eye_width, eye_height, left_eye_center, right_eye_center)


def display_streaming_text(text, delay=0.1):
    # Create a larger font size for the centered text
    large_font = pygame.font.Font(None, SCREEN_HEIGHT // 6)  # Font size proportional to screen height
    displayed_text = ""
    text_width, text_height = large_font.size(text)  # Calculate size of the full text

    # Calculate centered position
    x = (SCREEN_WIDTH - text_width) // 2
    y = (SCREEN_HEIGHT - text_height) // 2

    screen.fill(BLACK)  # Clear screen

    for char in text:
        displayed_text += char
        # Render the text up to the current character
        text_surface = large_font.render(displayed_text, True, EYE_COLOR)
        # Clear the text area and draw updated text
        screen.fill(BLACK)  # Clear the screen for consistency
        screen.blit(text_surface, (x, y))
        pygame.display.flip()
        time.sleep(delay)  # Pause between characters


# Main loop
def main():
    emotions = ["neutral", "blink"]
    emotion_index = 0
    text_index = 0

    clock = pygame.time.Clock()
    global SCREEN_WIDTH, SCREEN_HEIGHT

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                SCREEN_WIDTH, SCREEN_HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

        # Recalculate eye properties based on current screen size
        EYE_WIDTH, EYE_HEIGHT, LEFT_EYE_CENTER, RIGHT_EYE_CENTER = calculate_eye_properties(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Display the current emotion
        if emotions[emotion_index] == "neutral":
            draw_neutral(EYE_WIDTH, EYE_HEIGHT, LEFT_EYE_CENTER, RIGHT_EYE_CENTER)

        elif emotions[emotion_index] == "blink":
            draw_blink(EYE_WIDTH, EYE_HEIGHT, LEFT_EYE_CENTER, RIGHT_EYE_CENTER)

        if text_index == 5:
            display_streaming_text("Hello, World!", delay=0.1)
            text_index = 0

        time.sleep(1.5)

        emotion_index = (emotion_index + 1) % len(emotions)
        text_index +=1

        clock.tick(30)


if __name__ == "__main__":
    main()
