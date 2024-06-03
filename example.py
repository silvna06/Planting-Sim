import pygame
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
colour = (117, 173, 80)

icon = pygame.image.load("plant_icon.png")
font1 = pygame.font.Font('SuperPixel.ttf', 70)
font2 = pygame.font.Font('SuperPixel.ttf', 40)
text_1 = font1.render('Grow a Plant!', True, (27, 121, 49))
text_2 = font2.render('Click plant to start!', True, (27, 121, 49))

pygame.display.set_caption("Planting Sim")
pygame.display.set_icon(icon)

# Load and play background music
audio = "Wax.mp3"
pygame.mixer.music.load(audio)
pygame.mixer.music.play(-1)

# Load the images for the clickable areas
title_plant = pygame.image.load("opening_plant.png")
title_plant = pygame.transform.scale(title_plant, (500, 500))
seed1 = pygame.image.load("seed1.png")
seed1 = pygame.transform.scale(seed1, (100, 100))
seed2 = pygame.image.load("seed2.png")
seed2 = pygame.transform.scale(seed2, (100, 100)) 
plant1_1 = pygame.image.load("plant1_1.png")
plant1_1 = pygame.transform.scale(plant1_1, (100, 100))
plant1_2 = pygame.image.load("plant1_2.png")
plant1_2 = pygame.transform.scale(plant1_2, (100, 100))
plant1_3 = pygame.image.load("plant1_3.png")
plant1_3 = pygame.transform.scale(plant1_3, (100, 100))
plant1_4 = pygame.image.load("plant1_4.png")
plant1_4 = pygame.transform.scale(plant1_4, (100, 100))
plant1 = [plant1_1, plant1_2, plant1_3, plant1_4]

# Get the rect object of the images
click_rect1 = title_plant.get_rect(center=(400, 300))
click_rect2_1 = seed1.get_rect()
click_rect2_1.topleft = (50, 100)
click_rect2_2 = seed2.get_rect()
click_rect2_2.topright = (750, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_state == GameState.MAIN_SCREEN and click_rect1.collidepoint(event.pos):
                current_state = GameState.SEED1_SCREEN
            elif current_state == GameState.SEED1_SCREEN and click_rect2_1.collidepoint(event.pos):
                current_state = GameState.PLANT1_SCREEN
            elif current_state == GameState.SEED1_SCREEN and click_rect2_2.collidepoint(event.pos):
                current_state = GameState.PLANT2_SCREEN

    if current_state == GameState.MAIN_SCREEN:
        screen.fill(colour)
        screen.blit(text_1, (50, 50))
        screen.blit(text_2, (90, 500))
        screen.blit(title_plant, click_rect1)
    elif current_state == GameState.SEED1_SCREEN:
        screen.fill(colour)
        screen.blit(seed1, click_rect2_1)
        screen.blit(seed2, click_rect2_2)
    elif current_state == GameState.PLANT1_SCREEN:
        for img in plant1:
            screen.fill(colour)
            screen.blit(img, (350, 300))
            pygame.display.flip()
            pygame.time.wait(3000)
            #current_state = GameState.SEED1_SCREEN  # Transition back to SEED1_SCREEN after displaying the images
    elif current_state == GameState.PLANT2_SCREEN:
        screen.fill(colour)
        screen.blit(plant1_1, (450, 150))
    
    pygame.display.flip()

pygame.quit()

