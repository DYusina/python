import pygame
import random
# import requests
# import os

pygame.init()

screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('comme des garcons')

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
orange = (255, 200, 100)

ball_radius = 15
ball_x = screen_width // 2
ball_y = screen_height // 2  # пусть стартует из центр
ball_speed_x = 5
ball_speed_y = 5
antibonus_speed_x = 10
antibonus_speed_y = 10

# замена шарика на сердечко
# image_url = 'https://commedesgarconshoodie.shop/wp-content/uploads/2024/01/download-5.webp'
# image_response = requests.get(image_url)
# image_path = 'ball_image.png'
#
# with open(image_path, 'wb') as f:
#     f.write(image_response.content)

# картинка на случай победы
# ball_image = pygame.image.load(image_path)
# ball_image = pygame.transform.scale(ball_image, (50, 50))
#
#
# victory_url = 'https://commedesgarconshoodie.shop/wp-content/uploads/2024/01/download-5.webp'
# image_response = requests.get(image_url)
# image_path = 'victore_image.png'
#
# with open(image_path, 'wb') as f:
#     f.write(image_response.content)

# замена шара
# ball_image = pygame.image.load(image_path)
# ball_image = pygame.transform.scale(ball_image, (50, 50))

platform_width = 100
platform_height = 15
platform_x = (screen_width - platform_width) // 2
platform_y = screen_height - 40
platform_speed = 10

brick_width = 50
brick_height = 25
layers = 4
columns = 6
right_margin = 10
down_margin = 5

clock = pygame.time.Clock()

lives = []
life_x = screen_width - 20
for i in range(3):
    life_x -= 20
    lives.append(pygame.Rect(life_x, 20, 10, 10))
    life_x -= 10

bricks = []
start_x = 15
start_y = 50
for l in range(layers):
    current_x = start_x
    # start_y += 10
    for c in range(columns):
        current_x += 10
        bricks.append(pygame.Rect(current_x, start_y, brick_width, brick_height))
        current_x += brick_width
    start_y += brick_height + 10

bonus_bricks = []
for i in range(5):
    bonus_bricks.append(random.choice(bricks))

bonus_ball_radius = 5
bonus_ball_speed_y = 5

def draw_text(screen, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

game_over = False
platform_rect = pygame.Rect(screen_width // 2 - platform_width // 2, screen_height - 40, platform_width, platform_height)

bonus_ballz = []

platform_extended = False
extended_time_remaining = 0
extend_duration = 3000

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)
    pygame.draw.rect(screen, black, (platform_x, platform_y, platform_width, platform_height))
    if not game_over:
        pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)
    # screen.blit(ball_image, (ball_x, ball_y))
    for brick in bricks:
        pygame.draw.rect(screen, black, brick)

    key = pygame.key.get_pressed()

    if key[pygame.K_a] and platform_x > 0:  # рулим налево
        platform_x -= platform_speed
    if key[pygame.K_d] and platform_x < screen_width - platform_width:  # право:)
        platform_x += platform_speed

    if not game_over:
        ball_x += ball_speed_x
        ball_y += ball_speed_y

    # Отскок шара от стен
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= screen_width:  # ограничиваем бока
        ball_speed_x *= -1
    if ball_y - ball_radius <= 0:
        ball_speed_y *= -1  # провал внз

    # отскок от платформы
    if platform_y <= ball_y + ball_radius <= platform_y + platform_height and platform_x <= ball_x <= platform_x + platform_width:
        ball_speed_y *= -1

    # в ямку бум + проигрыш
    if ball_y - ball_radius > screen_height:
        if len(lives) > 1:
            ball_x = screen_width // 2
            ball_y = screen_height // 2
            ball_speed_x = 5
            ball_speed_y = 5
            lives.pop()
        else:
            draw_text(screen, "Boo-hoo", pygame.font.SysFont(None, 75), red, screen_width // 4, screen_height // 2)
            game_over = True

    if not game_over:
        for life in lives:
            pygame.draw.rect(screen, red, life)

    if len(bricks) == 0 and len(lives) > 0:
        draw_text(screen, "Nice", pygame.font.SysFont(None, 75), red, screen_width // 3, screen_height // 2)
        game_over = True

    ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)


    # for brick in bricks:
    #     if ball_rect.colliderect(brick):
    #         if brick in bonus_bricks:
    #             bonus.append([*brick.center])
    #             print(brick.center)
    #         bricks.remove(brick)
    #         ball_speed_y *= -1
    #         bonus[0][1] += bonus_ball_speed_y
    #         pygame.draw.circle(screen, red, bonus[0], bonus_ball_radius)
    #         bonus.pop()

    for brick in bricks[:]:  # Обрабатываем копию списка кирпичей
        if ball_rect.colliderect(brick):
            if brick in bonus_bricks:  # Если кирпич содержит бонус
                bonus_ballz.append([*brick.center])  # Добавляем бонус (центр кирпича)
            bricks.remove(brick)  # Удаляем кирпич
            ball_speed_y *= -1  # Меняем направление мяча

    for bonus in bonus_ballz:
        # print(bonus)
        pygame.draw.circle(screen, red, (bonus[0], bonus[1]), bonus_ball_radius)
        bonus[1] += bonus_ball_speed_y  # Двигаем бонус вниз

        # Если бонус достигает платформы
        if platform_rect.colliderect(pygame.Rect(bonus[0], bonus[1], bonus_ball_radius * 2, bonus_ball_radius * 2)):
            bonus_ballz.remove(bonus)  # Удаляем бонус
            if not platform_extended:
                ball_speed_x = antibonus_speed_x
                ball_speed_y = antibonus_speed_y

                platform_extended = True  # Устанавливаем флаг расширения
                platform_width += 40  # Увеличиваем ширину платформы
                platform_extension_timer = 0




        # Если бонус выходит за экран
        elif bonus[1] > screen_height:
            bonus_ballz.remove(bonus)  # Удаляем бонус




    # for bonus in bonus_ballz[:]:
    # # Если бонус пойман платформой
    #     if platform_y - (platform_height//2) <= bonus[1] + bonus_ball_radius <= platform_y + platform_height or platform_x - (platform_width//2) <= bonus[0] <= platform_x + (platform_width//2):
    #         bonus_ballz.remove(bonus)
    #         platform_width += 40  # Увеличиваем платформу
    #
    #     # Удаляем бонус, если он выходит за пределы экрана
    #     if bonus[1] > screen_height:
    #         bonus_ballz.remove(bonus)

    for bonus in bonus_ballz[:]:
        # Проверяем, пересекается ли бонус с платформой
        if (platform_y <= bonus[1] + bonus_ball_radius <= platform_y + platform_height and
                platform_x <= bonus[0] <= platform_x + platform_width):
            bonus_ballz.remove(bonus)
            platform_width += 40  # Увеличиваем платформу

        # Удаляем бонус, если он вышел за пределы экрана
        elif bonus[1] > screen_height:
            bonus_ballz.remove(bonus)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
