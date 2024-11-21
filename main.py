import pygame
import cv2
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration

# Initialize Pygame and OpenCV
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Object Guessing Game")
font = pygame.font.Font(None, 36)

# Initialize camera
cap = cv2.VideoCapture(0)

# Load lightweight multimodal model (BLIP)
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Game variables
description = "Capture an object to start!"
score = 0
running = True
clock = pygame.time.Clock()

def get_image_description(frame):
    """Generate a text description from an image."""
    # Convert BGR to RGB and resize
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(rgb_frame)

    # Process image and generate description
    inputs = processor(pil_image, return_tensors="pt").to("cpu")
    out = model.generate(**inputs)
    return processor.decode(out[0], skip_special_tokens=True)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Capture frame from camera
    ret, frame = cap.read()
    if not ret:
        break

    # Display camera feed in Pygame
    frame = cv2.flip(frame, 1)  # Flip frame horizontally for mirror effect
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_surface = pygame.surfarray.make_surface(frame_rgb.swapaxes(0, 1))
    screen.blit(frame_surface, (0, 0))

    # Display description and score
    description_surface = font.render(f"Description: {description}", True, (255, 255, 255))
    score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(description_surface, (10, HEIGHT - 60))
    screen.blit(score_surface, (10, HEIGHT - 30))

    # Check for spacebar press to capture and describe image
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        description = get_image_description(frame)

    pygame.display.flip()
    clock.tick(30)

# Release resources
cap.release()
pygame.quit()
