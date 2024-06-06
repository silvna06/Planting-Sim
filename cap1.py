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

current_state = GameState.MAIN_SCREEN
correct_plant = True

class Owner:   
    def __init__(self, money):
        self.__money = money

    @property
    def money(self):
        return self.__money
    
    @money.setter
    def money(self, value):
        self.__money = value
    
    def total_money(self):
        if correct_plant:
            self.money += 10
        else:
            self.money -= 10
owner = Owner(20)

sell_plants = {"order1":1, "order2":2, "order3":3, "order4":4, "order5":5, "order6":6, "order7":7, "order8":8}

#screen and colours
screen = pygame.display.set_mode((800, 600))
colour1 = (53,94,59)
colour2 = (135, 206, 235)
colour3 = (50, 64, 123)

font1 = pygame.font.Font('SuperPixel.ttf', 70)
font2 = pygame.font.Font('SuperPixel.ttf', 40)
text_1 = font1.render('Grow a Plant!', True, (117, 173, 80))
text_2 = font2.render('Click plant to start!', True, (117, 173, 80))
text_3 = font2.render('Select a Plant Seed', True, (117, 173, 80))
text_4 = font1.render('PLANTING!', True, (117, 173, 80))
text_5 = font1.render('Time to sell!!!', True, (117, 173, 80))
text_6 = font2.render('Are you ready?', True, (117, 173, 80))
text_7 = font1.render('YES!', True, (117, 173, 80))

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
                current_state = GameState.SHOP2_SCREEN
            elif current_state == GameState.SEED1_SCREEN and images.click_rect2_5.collidepoint(event.pos):
                current_state = GameState.SEED2_SCREEN
            elif current_state == GameState.SEED2_SCREEN and images.click_rect2_5.collidepoint(event.pos):
                current_state = GameState.SEED1_SCREEN
            elif current_state == GameState.SEED1_SCREEN and images.click_rect2_1.collidepoint(event.pos):
                current_state = GameState.PLANT1_SCREEN
            elif current_state == GameState.SEED1_SCREEN and images.click_rect2_2.collidepoint(event.pos):
                current_state = GameState.PLANT2_SCREEN
            elif current_state == GameState.SEED1_SCREEN and images.click_rect2_3.collidepoint(event.pos):
                current_state = GameState.PLANT3_SCREEN
            elif current_state == GameState.SEED1_SCREEN and images.click_rect2_4.collidepoint(event.pos):
                current_state = GameState.PLANT4_SCREEN
            elif current_state == GameState.SEED2_SCREEN and images.click_rect2_1.collidepoint(event.pos):
                current_state = GameState.PLANT5_SCREEN
            elif current_state == GameState.SEED2_SCREEN and images.click_rect2_2.collidepoint(event.pos):
                current_state = GameState.PLANT6_SCREEN
            elif current_state == GameState.SEED2_SCREEN and images.click_rect2_3.collidepoint(event.pos):
                current_state = GameState.PLANT7_SCREEN
            elif current_state == GameState.SEED2_SCREEN and images.click_rect2_4.collidepoint(event.pos):
                current_state = GameState.PLANT8_SCREEN
            elif current_state == GameState.SHOP1_SCREEN and images.click_rect3.collidepoint(event.pos):
                current_state = GameState.SHOP2_SCREEN
            elif current_state == GameState.SHOP2_SCREEN and images.plant_rect1.collidepoint(event.pos):
                correct_plant = True

    if current_state == GameState.MAIN_SCREEN:
        screen.fill(colour1)
        screen.blit(text_1, (50, 50))
        screen.blit(text_2, (90, 500))
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

    elif current_state == GameState.PLANT1_SCREEN:
        for img in images.plant1:
            screen.fill(colour2)
            screen.blit(text_4, (175, 450))
            screen.blit(images.sun, (-140, -140))
            screen.blit(img, (300, 200))
            screen.blit(images.watering_can, (400, 10))
            pygame.display.flip()
            pygame.time.delay(2000)
            screen.fill(colour3)
            screen.blit(text_4, (175, 450))
            screen.blit(img, (300, 200))
            screen.blit(images.moon, (650, -50))
            pygame.display.flip()
            pygame.time.delay(3000)
        current_state = GameState.SHOP1_SCREEN  #changes into a different display after loop
    
    elif current_state == GameState.PLANT2_SCREEN:
        for img in images.plant2:
            screen.fill(colour2)
            screen.blit(text_4, (175, 450))
            screen.blit(images.sun, (-140, -140))
            screen.blit(img, (300, 200))
            screen.blit(images.watering_can, (400, 10))
            pygame.display.flip()
            pygame.time.delay(2000)
            screen.fill(colour3)
            screen.blit(text_4, (175, 450))
            screen.blit(img, (300, 200))
            screen.blit(images.moon, (650, -50))
            pygame.display.flip()
            pygame.time.delay(3000)
        current_state = GameState.SHOP1_SCREEN

    elif current_state == GameState.PLANT3_SCREEN:
        for img in images.plant3:
            screen.fill(colour2)
            screen.blit(text_4, (175, 450))
            screen.blit(images.sun, (-140, -140))
            screen.blit(img, (300, 200))
            screen.blit(images.watering_can, (400, 10))
            pygame.display.flip()
            pygame.time.delay(2000)
            screen.fill(colour3)
            screen.blit(text_4, (175, 450))
            screen.blit(img, (300, 200))
            screen.blit(images.moon, (650, -50))
            pygame.display.flip()
            pygame.time.delay(3000)
        current_state = GameState.SHOP1_SCREEN

    elif current_state == GameState.PLANT4_SCREEN:
        for img in images.plant4:
            screen.fill(colour2)
            screen.blit(text_4, (175, 450))
            screen.blit(images.sun, (-140, -140))
            screen.blit(img, (300, 200))
            screen.blit(images.watering_can, (400, 10))
            pygame.display.flip()
            pygame.time.delay(2000)
            screen.fill(colour3)
            screen.blit(text_4, (175, 450))
            screen.blit(img, (300, 200))
            screen.blit(images.moon, (650, -50))
            pygame.display.flip()
            pygame.time.delay(3000)
        current_state = GameState.SHOP1_SCREEN

    elif current_state == GameState.PLANT5_SCREEN:
        for img in images.plant5:
            screen.fill(colour2)
            screen.blit(text_4, (175, 450))
            screen.blit(images.sun, (-140, -140))
            screen.blit(img, (300, 200))
            screen.blit(images.watering_can, (400, 10))
            pygame.display.flip()
            pygame.time.delay(2000)
            screen.fill(colour3)
            screen.blit(text_4, (175, 450))
            screen.blit(img, (300, 200))
            screen.blit(images.moon, (650, -50))
            pygame.display.flip()
            pygame.time.delay(3000)
        current_state = GameState.SHOP1_SCREEN

    elif current_state == GameState.PLANT6_SCREEN:
        for img in images.plant6:
            screen.fill(colour2)
            screen.blit(text_4, (175, 450))
            screen.blit(images.sun, (-140, -140))
            screen.blit(img, (300, 200))
            screen.blit(images.watering_can, (400, 10))
            pygame.display.flip()
            pygame.time.delay(2000)
            screen.fill(colour3)
            screen.blit(text_4, (175, 450))
            screen.blit(img, (300, 200))
            screen.blit(images.moon, (650, -50))
            pygame.display.flip()
            pygame.time.delay(3000)
        current_state = GameState.SHOP1_SCREEN
    
    elif current_state == GameState.PLANT7_SCREEN:
        for img in images.plant7:
            screen.fill(colour2)
            screen.blit(text_4, (175, 450))
            screen.blit(images.sun, (-140, -140))
            screen.blit(img, (300, 200))
            screen.blit(images.watering_can, (400, 10))
            pygame.display.flip()
            pygame.time.delay(2000)
            screen.fill(colour3)
            screen.blit(text_4, (175, 450))
            screen.blit(img, (300, 200))
            screen.blit(images.moon, (650, -50))
            pygame.display.flip()
            pygame.time.delay(3000)
        current_state = GameState.SHOP1_SCREEN

    elif current_state == GameState.PLANT8_SCREEN:
        for img in images.plant8:
            screen.fill(colour2)
            screen.blit(text_4, (175, 450))
            screen.blit(images.sun, (-140, -140))
            screen.blit(img, (300, 200))
            screen.blit(images.watering_can, (400, 10))
            pygame.display.flip()
            pygame.time.delay(2000)
            screen.fill(colour3)
            screen.blit(text_4, (175, 450))
            screen.blit(img, (300, 200))
            screen.blit(images.moon, (650, -50))
            pygame.display.flip()
            pygame.time.delay(3000)
        current_state = GameState.SHOP1_SCREEN

    elif current_state == GameState.SHOP1_SCREEN:
        screen.fill(colour1)
        screen.blit(text_5, (50, 50))
        screen.blit(text_6, (200, 400))
        screen.blit (images.coin_pile, (300,160))
        screen.blit(images.button,images.click_rect3)
        screen.blit(text_7, (315, 487))

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
        screen.blit(images.plant7, (400, 75))

    pygame.display.flip()

pygame.quit()
