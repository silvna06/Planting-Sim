import pygame
import images
from enum import Enum

pygame.init()  #initializing pygame
pygame.font.init()  #initializing font

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
    SHOP1_SCREEN = 12
    SHOP2_SCREEN = 13
    END_SCREEN = 14

current_state = GameState.MAIN_SCREEN

class Owner:   
    def __init__(self, money):
        self.__money = money

    @property
    def money(self):
        return self.__money
    
    @money.setter
    def money(self, value):
        self.__money = value
    
    def __call__(self):
        return self.money
    
    def total_money(self, correct_plant):
        if correct_plant:
            self.money += 10
        else:
            self.money -= 5

    def __str__(self):
        return f"{self.money}"
owner = Owner(20)

sell_plants = [images.plant_rect6, images.plant_rect3, images.plant_rect7, images.plant_rect5, images.plant_rect4, images.plant_rect1, images.plant_rect2, images.plant_rect8]
new_plants = images.image_loader()
plant_list = list(new_plants.keys())
plant_index = 0

#screen and colours
screen = pygame.display.set_mode((800, 600))
colour1 = (53,94,59)
colour2 = (135, 206, 235)
colour3 = (50, 64, 123)

font1 = pygame.font.Font('MinecraftBold.otf', 70)
font2 = pygame.font.Font('MinecraftBold.otf', 50)
font3 = pygame.font.SysFont('Arial', 200)
font4 = pygame.font.Font('MinecraftBold.otf', 90)
text_1 = font1.render('Planting Simulation!', True, (117, 173, 80))
text_2 = font2.render('Click plant to start!', True, (117, 173, 80))
text_3 = font2.render('Select a Plant Seed', True, (117, 173, 80))
text_4 = font1.render('PLANTING!', True, (117, 173, 80))
text_5 = font1.render('Time to sell!!!', True, (117, 173, 80))
text_6 = font2.render('Are you ready?', True, (117, 173, 80))
text_7 = font4.render('YES!', True, (117, 173, 80))
text_8 = font1.render('MENU', True, (117, 173, 80))
text_9 = font1.render('QUIT', True, (117, 173, 80))
f_rank = font3.render(f"F", True, "red")
c_rank = font3.render(f"C", True, "grey48")
b_rank = font3.render(f"B", True, "grey48")
a_rank = font3.render(f"A", True, "grey48")

pygame.display.set_caption("Planting Sim")
pygame.display.set_icon(images.icon)

#loads and play background music
audio = "music.mp3"
pygame.mixer.music.load(audio)
#pygame.mixer.music.play(-1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_state == GameState.MAIN_SCREEN and images.click_rect1.collidepoint(event.pos):
                current_state = GameState.SEED1_SCREEN
            elif current_state == GameState.SEED1_SCREEN and images.click_rect2_5.collidepoint(event.pos):
                current_state = GameState.SEED2_SCREEN
            elif current_state == GameState.SEED2_SCREEN and images.click_rect2_5.collidepoint(event.pos):
                current_state = GameState.SEED1_SCREEN
            elif current_state == GameState.SEED1_SCREEN and images.click_rect2_1.collidepoint(event.pos):
                current_state = GameState.PLANT1_SCREEN
                plant_clicked = True
            elif current_state == GameState.SEED1_SCREEN and images.click_rect2_2.collidepoint(event.pos):
                current_state = GameState.PLANT2_SCREEN
                plant_clicked = True
            elif current_state == GameState.SEED1_SCREEN and images.click_rect2_3.collidepoint(event.pos):
                current_state = GameState.PLANT3_SCREEN
                plant_clicked = True
            elif current_state == GameState.SEED1_SCREEN and images.click_rect2_4.collidepoint(event.pos):
                current_state = GameState.PLANT4_SCREEN
                plant_clicked = True
            elif current_state == GameState.SEED2_SCREEN and images.click_rect2_1.collidepoint(event.pos):
                current_state = GameState.PLANT5_SCREEN
                plant_clicked = True
            elif current_state == GameState.SEED2_SCREEN and images.click_rect2_2.collidepoint(event.pos):
                current_state = GameState.PLANT6_SCREEN
                plant_clicked = True
            elif current_state == GameState.SEED2_SCREEN and images.click_rect2_3.collidepoint(event.pos):
                current_state = GameState.PLANT7_SCREEN
                plant_clicked = True
            elif current_state == GameState.SEED2_SCREEN and images.click_rect2_4.collidepoint(event.pos):
                current_state = GameState.PLANT8_SCREEN
                plant_clicked = True
            elif current_state == GameState.SHOP1_SCREEN and images.click_rect3.collidepoint(event.pos):
                current_state = GameState.SHOP2_SCREEN
                plant_index = 0  # reset for SHOP2_SCREEN (playability)
            elif current_state == GameState.SHOP2_SCREEN:
                correct_plant = False
                for rect in sell_plants:
                    if rect.collidepoint(event.pos):
                        correct_plant = (rect == sell_plants[plant_index])
                owner.total_money(correct_plant)
                plant_index += 1
                if plant_index >= len(plant_list):
                    current_state = GameState.END_SCREEN
            elif current_state == GameState.END_SCREEN and images.click_rect4.collidepoint(event.pos):
                current_state = GameState.MAIN_SCREEN
            elif current_state == GameState.END_SCREEN and images.click_rect5.collidepoint(event.pos):
                running = False


    if current_state == GameState.MAIN_SCREEN:
        screen.fill(colour1)
        screen.blit(text_1, (15, 50))
        screen.blit(text_2, (125, 500))
        screen.blit(images.title_plant, images.click_rect1)

    elif current_state == GameState.SEED1_SCREEN:
        screen.fill(colour1)
        screen.blit(text_3, (125, 50))
        screen.blit(images.seed1, images.click_rect2_1)
        screen.blit(images.seed2, images.click_rect2_2)
        screen.blit(images.seed3, images.click_rect2_3)
        screen.blit(images.seed4, images.click_rect2_4)
        screen.blit(images.right_arrow, images.click_rect2_5)

    elif current_state == GameState.SEED2_SCREEN:
        screen.fill(colour1)
        screen.blit(text_3, (125, 50))
        screen.blit(images.seed5, images.click_rect2_1)
        screen.blit(images.seed6, images.click_rect2_2)
        screen.blit(images.seed7, images.click_rect2_3)
        screen.blit(images.seed8, images.click_rect2_4)
        screen.blit(images.left_arrow, images.click_rect2_5)

    elif current_state in [GameState.PLANT1_SCREEN, GameState.PLANT2_SCREEN, GameState.PLANT3_SCREEN, GameState.PLANT4_SCREEN, GameState.PLANT5_SCREEN, GameState.PLANT6_SCREEN, GameState.PLANT7_SCREEN, GameState.PLANT8_SCREEN]:

        if current_state == GameState.PLANT1_SCREEN:
            plant_images = images.plants_1
        elif current_state == GameState.PLANT2_SCREEN:
            plant_images = images.plants_2
        elif current_state == GameState.PLANT3_SCREEN:
            plant_images = images.plants_3
        elif current_state == GameState.PLANT4_SCREEN:
            plant_images = images.plants_4
        elif current_state == GameState.PLANT5_SCREEN:
            plant_images = images.plants_5
        elif current_state == GameState.PLANT6_SCREEN:
            plant_images = images.plants_6
        elif current_state == GameState.PLANT7_SCREEN:
            plant_images = images.plants_7
        elif current_state == GameState.PLANT8_SCREEN:
            plant_images = images.plants_8

        for img in plant_images:
            screen.fill(colour2)
            screen.blit(text_4, (220, 450))
            screen.blit(images.sun, (-140, -140))
            screen.blit(img, (300, 200))
            screen.blit(images.watering_can, (400, 10))
            pygame.display.flip()
            pygame.time.delay(2000)
            screen.fill(colour3)
            screen.blit(text_4, (220, 450))
            screen.blit(img, (300, 200))
            screen.blit(images.moon, (650, -50))
            pygame.display.flip()
            pygame.time.delay(3000)
        current_state = GameState.SHOP1_SCREEN  #changes into a different display after loop

    elif current_state == GameState.SHOP1_SCREEN:
        screen.fill(colour1)
        screen.blit(text_5, (155, 50))
        screen.blit(text_6, (200, 400))
        screen.blit(images.coin_pile, (300,160))
        screen.blit(images.button,images.click_rect3)
        screen.blit(text_7, (300, 487))

    elif current_state == GameState.SHOP2_SCREEN:
        screen.fill(colour2)
        screen.blit(images.npc, (155,20))
        screen.blit(images.plant_stand, (0, 0))
        screen.blit(images.plant1, images.plant_rect1)
        screen.blit(images.plant2, images.plant_rect2)
        screen.blit(images.plant3, images.plant_rect3)
        screen.blit(images.plant4, images.plant_rect4)
        screen.blit(images.plant5, images.plant_rect5)
        screen.blit(images.plant6, images.plant_rect6)
        screen.blit(images.plant7, images.plant_rect7)
        screen.blit(images.plant8, images.plant_rect8)
        balance = font2.render(f"{owner}", True, "black")
        screen.blit(images.coin, (710,0))
        if owner.money >= 0:
            screen.blit(balance, (630,5))
        else:
            screen.blit(balance, (590,5))
        plant_key = plant_list[plant_index]
        plant_image = new_plants[plant_key]
        screen.blit(plant_image, (400, 75))
    
    else:
        screen.fill(colour1)
        final_currency = font2.render(f"Your total is {owner} coins.", True, (117, 173, 80))
        if owner.money >= 100:
            screen.blit(images.s_rank, (330,20))
            screen.blit(final_currency, (65,250))
            screen.blit(images.button, images.click_rect4)
            screen.blit(images.button, images.click_rect5)
            screen.blit(text_8, (130,490))
            screen.blit(text_9,(490,490))
        elif owner.money > 80:
            screen.blit(a_rank, (330,0))
            screen.blit(final_currency, (75,250))
            screen.blit(images.button, images.click_rect4)
            screen.blit(images.button, images.click_rect5)
            screen.blit(text_8, (130,490))
            screen.blit(text_9,(490,490))
        elif owner.money > 50:
            screen.blit(b_rank, (350,0))
            screen.blit(final_currency, (75,250))
            screen.blit(images.button, images.click_rect4)
            screen.blit(images.button, images.click_rect5)
            screen.blit(text_8, (130,490))
            screen.blit(text_9,(490,490))
        elif owner.money > 20:
            screen.blit(c_rank, (330,0))
            screen.blit(final_currency, (75,250))
            screen.blit(images.button, images.click_rect4)
            screen.blit(images.button, images.click_rect5)
            screen.blit(text_8, (130,490))
            screen.blit(text_9,(490,490))
        else:
            screen.blit(f_rank, (350,0))
            screen.blit(final_currency, (75,250))
            screen.blit(images.button, images.click_rect4)
            screen.blit(images.button, images.click_rect5)
            screen.blit(text_8, (130,490))
            screen.blit(text_9,(490,490)) 

    pygame.display.flip()

pygame.quit()
