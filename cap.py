import pygame
import images
from enum import Enum

pygame.init()  # Initializing pygame
pygame.font.init()  # Initializing font

class GameState(Enum):
    MAIN_SCREEN = 1
    SEED1_SCREEN = 2
    SEED2_SCREEN = 3
    PLANT1_SCREEN = 4
    PLANT2_SCREEN = 5
    PLANT3_SCREEN = 6
    PLANT4_SCREEN = 7
    PLANT5_SCREEN = 8
    PLANT6_SCREEN = 9
    PLANT7_SCREEN = 10
    PLANT8_SCREEN = 11

current_state = GameState.MAIN_SCREEN

# Set up the screen
screen = pygame.display.set_mode((800, 600))
colour1 = (53,94,59)
colour2 = (135, 206, 235)
colour3 = (50, 64, 123)

icon = pygame.image.load("plant_icon.png")
font1 = pygame.font.Font('SuperPixel.ttf', 70)
font2 = pygame.font.Font('SuperPixel.ttf', 40)
text_1 = font1.render('Grow a Plant!', True, (117, 173, 80))
text_2 = font2.render('Click plant to start!', True, (117, 173, 80))

pygame.display.set_caption("Planting Sim")
pygame.display.set_icon(icon)

# Load and play background music
audio = "Wax.mp3"
pygame.mixer.music.load(audio)
pygame.mixer.music.play(-1)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_state == GameState.MAIN_SCREEN and images.click_rect1.collidepoint(event.pos):
                current_state = GameState.SEED1_SCREEN
            elif current_state == GameState.SEED1_SCREEN and images.click_rect2_1.collidepoint(event.pos):
                current_state = GameState.PLANT1_SCREEN
            elif current_state == GameState.SEED1_SCREEN and images.click_rect2_2.collidepoint(event.pos):
                current_state = GameState.PLANT2_SCREEN

    if current_state == GameState.MAIN_SCREEN:
        screen.fill(colour1)
        screen.blit(text_1, (50, 50))
        screen.blit(text_2, (90, 500))
        screen.blit(images.title_plant, images.click_rect1)
    elif current_state == GameState.SEED1_SCREEN:
        screen.fill(colour1)
        screen.blit(images.seed1, images.click_rect2_1)
        screen.blit(images.seed2, images.click_rect2_2)
    elif current_state == GameState.PLANT1_SCREEN:
        for img in images.plant1:
            screen.fill(colour2)
            screen.blit(images.sun, (-140, -140))
            screen.blit(img, (300, 200))
            screen.blit(images.watering_can, (400, 10))
            pygame.display.flip()
            pygame.time.delay(2000)
            screen.fill(colour3)
            screen.blit(img, (300, 200))
            screen.blit(images.moon, (650, -50))
            pygame.display.flip()
            pygame.time.delay(3000)
        current_state = GameState.MAIN_SCREEN  # Transition back to SEED1_SCREEN after displaying the images
    elif current_state == GameState.PLANT2_SCREEN:
        screen.fill(colour2)
        screen.blit(images.plant1_1, (450, 150))
    
    pygame.display.flip()

pygame.quit()

