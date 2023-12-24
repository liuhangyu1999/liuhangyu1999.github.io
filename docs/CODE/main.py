import pygame
import random

# 初始化pygame
pygame.init()

# 定义颜色
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# 创建游戏窗口的宽度和高度
width, height = 600, 400

# 创建游戏窗口
game_window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Greedy Snake Game')

clock = pygame.time.Clock()

snake_block = 10

background_image = pygame.image.load("background.jpg")


font_style = pygame.font.SysFont('hgy1cnki', 15)

# 定义贪吃蛇的分数
def your_score(score):
    value = font_style.render("Score分数: " + str(score), True, white)
    game_window.blit(value, [50, 80])


# 定义贪吃蛇的身体
def our_snake(snake_block, snake_list):
    for x in snake_list[:-1]:
        pygame.draw.rect(game_window, white, [x[0], x[1], snake_block, snake_block])
    pygame.draw.circle(game_window, green, (snake_list[-1][0], snake_list[-1][1]), 4)

# 定义游戏结束的消息
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_window.blit(mesg, [width / 2, height / 2])

# 定义游戏的主循环
def gameLoop():
    game_over = False
    game_close = False

    # 贪吃蛇的起始位置
    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_speed = 6

    snake_List = []
    length_of_snake = 1

    # 食物的随机位置
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            # game_window.fill(black)
            game_window.blit(background_image, (0, 0))
            message("c-继续 或q-退出", white)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_a:
                    snake_speed += 10
                elif event.key == pygame.K_q:
                    game_close = True

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        game_window.blit(background_image, (0, 0))
        pygame.draw.rect(game_window, green, [foodx, foody, snake_block, snake_block])



        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        your_score(length_of_snake - 1)
        # 显示食物坐标
        font = pygame.font.Font(None, 20)
        text = font.render(str(foodx) + "," + str(foody), True, white)
        game_window.blit(text, (foodx + 10, foody + 10))

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0


            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# 运行游戏
gameLoop()
