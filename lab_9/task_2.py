import pygame, sys, random, time

pygame.init()

# Размеры окна и блоков
BLOCK_SIZE = 20
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Шрифт для отображения текста
font = pygame.font.SysFont("Montserrat", 20)
game_over_font = pygame.font.SysFont("Montserrat", 50)

# Змейка: начальное положение
snake = [(100, 100), (80, 100), (60, 100)]  # Список блоков
direction = 'RIGHT'

score = 0
level = 1
speed = 10

# Функция генерации еды с случайным весом
def generate_food():
    while True:
        x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        if (x, y) not in snake:
            weight = random.randint(1, 5)  # Еда с случайным весом от 1 до 5
            return (x, y, weight)  # Возвращаем координаты и вес еды

# Функция для проверки, истекло ли время для еды
def food_timer(food_spawn_time, expiration_time=5):
    """Возвращает True, если еда должна исчезнуть по таймеру."""
    if time.time() - food_spawn_time > expiration_time:
        return True
    return False

# Генерация начальной еды
food = generate_food()
food_spawn_time = time.time()  # Время, когда еда была сгенерирована

# Основной игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and direction != 'DOWN':
        direction = 'UP'
    elif keys[pygame.K_s] and direction != 'UP':
        direction = 'DOWN'
    elif keys[pygame.K_a] and direction != 'RIGHT':
        direction = 'LEFT'
    elif keys[pygame.K_d] and direction != 'LEFT':
        direction = 'RIGHT'

    head_x, head_y = snake[0]
    if direction == 'UP':
        head_y -= BLOCK_SIZE
    elif direction == 'DOWN':
        head_y += BLOCK_SIZE
    elif direction == 'LEFT':
        head_x -= BLOCK_SIZE
    elif direction == 'RIGHT':
        head_x += BLOCK_SIZE
    new_head = (head_x, head_y)

    # Проверка выхода за границы — game over
    if (head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT or new_head in snake):
        # Game Over logic
        game_over_text = game_over_font.render("Game Over", True, RED)
        final_score_text = game_over_font.render(f"Score: {score}", True, BLACK)
        
        # Display the Game Over message and final score
        screen.blit(game_over_text, (WIDTH // 4, HEIGHT // 3))
        screen.blit(final_score_text, (WIDTH // 4, HEIGHT // 2))
        pygame.display.flip()
        
        pygame.time.wait(2000)  # Wait for 2 seconds before closing
        pygame.quit()
        sys.exit()

    snake.insert(0, new_head)

    # Проверка, съела ли змея еду
    if new_head == food[:2]:  # Сравниваем только координаты
        score += food[2]  # Добавляем вес еды в очки
        food = generate_food()  # Генерация новой еды
        food_spawn_time = time.time()  # Обновление времени генерации еды

        # Повышение уровня каждые 4 очка
        if score % 4 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()  # Удалить последний элемент, если еда не съедена

    # Проверка, истекло ли время для еды
    if food_timer(food_spawn_time):
        food = generate_food()  # Если время истекло, генерируем новую еду
        food_spawn_time = time.time()  # Обновляем время генерации

    # Отрисовка еды и змеи
    pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))
    for block in snake:
        pygame.draw.rect(screen, GREEN, (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

    # Отображение очков и уровня
    score_text = font.render(f"Score: {score}   Level: {level}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)
