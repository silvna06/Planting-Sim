import pygame
import os

pygame.init() # initializing pygame

def load_image(image_path):
    # get the directory where the script is located
    current_path = os.path.dirname(__file__) 
    image_path = os.path.join(current_path, 'image', image_path)
    return pygame.image.load(image_path) # loads image onto pygame

# load and scale images for MAIN, SEED1, SEED2
icon = load_image("plant_icon.png")
title_plant = load_image("opening_plant.png")
title_plant = pygame.transform.scale(title_plant, (500, 500))
seed1 = load_image("seed1.png")
seed1 = pygame.transform.scale(seed1, (150, 150))
seed2 = load_image("seed2.png")
seed2 = pygame.transform.scale(seed2, (150, 150)) 
seed3 = load_image("seed3.png")
seed3 = pygame.transform.scale(seed3, (150, 150))
seed4 = load_image("seed4.png")
seed4 = pygame.transform.scale(seed4, (150, 150)) 
seed5 = load_image("seed5.png")
seed5 = pygame.transform.scale(seed5, (150, 150))
seed6 = load_image("seed6.png")
seed6 = pygame.transform.scale(seed6, (150, 150))
seed7 = load_image("seed7.png")
seed7 = pygame.transform.scale(seed7, (150, 150))
seed8 = load_image("seed8.png")
seed8 = pygame.transform.scale(seed8, (150, 150)) 

# load and scale for PLANT1
plant1_1 = load_image("plant1_1.png")
plant1_1 = pygame.transform.scale(plant1_1, (200, 200))
plant1_2 = load_image("plant1_2.png")
plant1_2 = pygame.transform.scale(plant1_2, (200, 200))
plant1_3 = load_image("plant1_3.png")
plant1_3 = pygame.transform.scale(plant1_3, (200, 200))
plant1_4 = load_image("plant1_4.png")
plant1_4 = pygame.transform.scale(plant1_4, (200, 200))
plants_1 = [plant1_1, plant1_2, plant1_3, plant1_4]

# load and scale for PLANT2
plant2_1 = load_image("plant2_1.png")
plant2_1 = pygame.transform.scale(plant2_1, (200, 200))
plant2_2 = load_image("plant2_2.png")
plant2_2 = pygame.transform.scale(plant2_2, (200, 200))
plant2_3 = load_image("plant2_3.png")
plant2_3 = pygame.transform.scale(plant2_3, (200, 200))
plant2_4 = load_image("plant2_4.png")
plant2_4 = pygame.transform.scale(plant2_4, (200, 200))
plants_2 = [plant2_1, plant2_2, plant2_3, plant2_4]

# load and scale for PLANT3
plant3_1 = load_image("plant3_1.png")
plant3_1 = pygame.transform.scale(plant3_1, (200, 200))
plant3_2 = load_image("plant3_2.png")
plant3_2 = pygame.transform.scale(plant3_2, (200, 200))
plant3_3 = load_image("plant3_3.png")
plant3_3 = pygame.transform.scale(plant3_3, (200, 200))
plant3_4 = load_image("plant3_4.png")
plant3_4 = pygame.transform.scale(plant3_4, (200, 200))
plants_3 = [plant3_1, plant3_2, plant3_3, plant3_4]

# load and scale for PLANT4
plant4_1 = load_image("plant4_1.png")
plant4_1 = pygame.transform.scale(plant4_1, (200, 200))
plant4_2 = load_image("plant4_2.png")
plant4_2 = pygame.transform.scale(plant4_2, (200, 200))
plant4_3 = load_image("plant4_3.png")
plant4_3 = pygame.transform.scale(plant4_3, (200, 200))
plant4_4 = load_image("plant4_4.png")
plant4_4 = pygame.transform.scale(plant4_4, (200, 200)) 
plants_4 = [plant4_1, plant4_2, plant4_3, plant4_4]

# load and scale for PLANT5
plant5_1 = load_image("plant5_1.png")
plant5_1 = pygame.transform.scale(plant5_1, (200, 200))
plant5_2 = load_image("plant5_2.png")
plant5_2 = pygame.transform.scale(plant5_2, (200, 200))
plant5_3 = load_image("plant5_3.png")
plant5_3 = pygame.transform.scale(plant5_3, (200, 200))
plant5_4 = load_image("plant5_4.png")
plant5_4 = pygame.transform.scale(plant5_4, (200, 200)) 
plants_5 = [plant5_1, plant5_2, plant5_3, plant5_4]

# load and scale for PLANT6
plant6_1 = load_image("plant6_1.png")
plant6_1 = pygame.transform.scale(plant6_1, (200, 200))
plant6_2 = load_image("plant6_2.png")
plant6_2 = pygame.transform.scale(plant6_2, (200, 200))
plant6_3 = load_image("plant6_3.png")
plant6_3 = pygame.transform.scale(plant6_3, (200, 200))
plant6_4 = load_image("plant6_4.png")
plant6_4 = pygame.transform.scale(plant6_4, (200, 200)) 
plants_6 = [plant6_1, plant6_2, plant6_3, plant6_4]

# load and scale for PLANT7
plant7_1 = load_image("plant7_1.png")
plant7_1 = pygame.transform.scale(plant7_1, (200, 200))
plant7_2 = load_image("plant7_2.png")
plant7_2 = pygame.transform.scale(plant7_2, (200, 200))
plant7_3 = load_image("plant7_3.png")
plant7_3 = pygame.transform.scale(plant7_3, (200, 200))
plant7_4 = load_image("plant7_4.png")
plant7_4 = pygame.transform.scale(plant7_4, (200, 200)) 
plants_7 = [plant7_1, plant7_2, plant7_3, plant7_4]

# load and scale for PLANT8
plant8_1 = load_image("plant8_1.png")
plant8_1 = pygame.transform.scale(plant8_1, (200, 200))
plant8_2 = load_image("plant8_2.png")
plant8_2 = pygame.transform.scale(plant8_2, (200, 200))
plant8_3 = load_image("plant8_3.png")
plant8_3 = pygame.transform.scale(plant8_3, (200, 200))
plant8_4 = load_image("plant8_4.png")
plant8_4 = pygame.transform.scale(plant8_4, (200, 200)) 
plants_8 = [plant8_1, plant8_2, plant8_3, plant8_4]

def image_loader():
    plants = {'plant6': plant6_4,
    'plant3': plant3_4,
    'plant7': plant7_4,
    'plant5': plant5_4,
    'plant4': plant4_4,
    'plant1': plant1_4,
    'plant2': plant2_4,
    'plant8': plant8_4}
    shop_plants = {}
    for key,value in plants.items():
        shop_plants[key] = pygame.transform.scale(value, (150, 150))
    return shop_plants # returns the scaled image along ith a dictionary for the shop

plant1 = pygame.transform.scale(plant1_4, (150, 150))
plant2 = pygame.transform.scale(plant2_4, (150, 150))
plant3 = pygame.transform.scale(plant3_4, (150, 150))
plant4 = pygame.transform.scale(plant4_4, (150, 150)) 
plant5 = pygame.transform.scale(plant5_4, (150, 150))
plant6 = pygame.transform.scale(plant6_4, (150, 150))
plant7 = pygame.transform.scale(plant7_4, (150, 150))
plant8 = pygame.transform.scale(plant8_4, (150, 150))

# additional images that were loaded into the game
sun = load_image("sun.png")
moon = load_image("moon.png")
watering_can = load_image("watering_can.png")
left_arrow = load_image("left_arrow.png")
right_arrow = load_image("right_arrow.png")
button = load_image("button.png")
plant_stand = load_image("plant_stand.png")
coin_pile = load_image("coin_pile.png")
coin_pile = pygame.transform.scale(coin_pile, (200, 200)) 
coin = load_image("coin.png")
coin = pygame.transform.scale(coin, (50, 50)) 
npc = load_image("npc.png")
s_rank = load_image("s_rank.png")
s_rank = pygame.transform.scale(s_rank, (150, 200)) 

# get the rect object of the images
click_rect1 = title_plant.get_rect(center=(400, 300))
click_rect2_1 = seed1.get_rect()
click_rect2_1.topleft = (200, 150)
click_rect2_2 = seed2.get_rect()
click_rect2_2.topright = (600, 150)
click_rect2_3 = seed1.get_rect()
click_rect2_3.topleft = (200, 325)
click_rect2_4 = seed2.get_rect()
click_rect2_4.topright = (600, 325)
click_rect2_5 = left_arrow.get_rect()
click_rect2_5.topright = (450, 475)
click_rect3 = button.get_rect()
click_rect3.topleft = (280,475)
click_rect4 = button.get_rect()
click_rect4.topleft = (100,475)
click_rect5 = button.get_rect()
click_rect5.topleft = (450,475)

# gets the rect object for the shop
plant_rect1 = plant1.get_rect()
plant_rect1.topleft = (45,275)
plant_rect2 = plant2.get_rect()
plant_rect2.topleft = (235, 275)
plant_rect3 = plant3.get_rect()
plant_rect3.topleft = (425, 275)
plant_rect4 = plant4.get_rect()
plant_rect4.topleft = (605, 275)
plant_rect5 = plant5.get_rect()
plant_rect5.topleft = (45,440)
plant_rect6 = plant6.get_rect()
plant_rect6.topleft = (235, 440)
plant_rect7 = plant7.get_rect()
plant_rect7.topleft = (425, 440)
plant_rect8 = plant8.get_rect()
plant_rect8.topleft = (605, 440)