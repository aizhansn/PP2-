import psycopg2
from connect import connect, load_config

def create_tables():
    config = load_config()
    conn = connect(config)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS user_score (
        id SERIAL PRIMARY KEY,
        user_id INT NOT NULL,
        score INT NOT NULL,
        level INT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
    """)

    conn.commit()
    cur.close()
    conn.close()

def get_or_create_user(username):
    config = load_config()
    conn = connect(config)
    cur = conn.cursor()

    cur.execute("""
    SELECT id FROM users WHERE username = %s
    """, (username,))
    user = cur.fetchone()

    if user:
        print(f"Welcome, {username}!")
        user_id = user[0]
        cur.execute("""
        SELECT score, level FROM user_score WHERE user_id = %s ORDER BY score DESC, level DESC LIMIT 1
        """, (user_id,))
        score_data = cur.fetchone()
        if score_data:
            print(f"Your current score is: {score_data[0]} at level {score_data[1]}")
    else:
        print(f"New user, {username}. Creating account.")
        cur.execute("""
        INSERT INTO users (username) VALUES (%s) RETURNING id
        """, (username,))
        user_id = cur.fetchone()[0]
        print(f"Account created")

    conn.commit()
    cur.close()
    conn.close()
    return user_id

def save_score(user_id, score, level):
    config = load_config()
    conn = connect(config)
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO user_score (user_id, score, level)
    VALUES (%s, %s, %s)
    """, (user_id, score, level))

    conn.commit()
    cur.close()
    conn.close()

def game_loop(user_id):
    import pygame
    import time
    import random

    pygame.init()

    window_x = 720
    window_y = 480
    snake_speed = 10

    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)

    game_window = pygame.display.set_mode((window_x, window_y))
    pygame.display.set_caption('Snake Game with Levels')

    fps = pygame.time.Clock()

    snake_position = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

    def generate_food():
        size_options = {
            "small": (10, 10, 3),
            "medium": (15, 15, 2),
            "large": (20, 20, 1)
        }

        size_key = random.choice(list(size_options.keys()))
        new_size = size_options[size_key][:2]
        new_score = size_options[size_key][2]

        while True:
            food_x = random.randint(1, (window_x - new_size[0]) // 10) * 10
            food_y = random.randint(1, (window_y - new_size[1]) // 10) * 10
            if [food_x, food_y] not in snake_body:
                return [food_x, food_y, new_size, new_score, time.time()]

    fruit_position = generate_food()
    fruit_spawn = True

    direction = 'RIGHT'

    score = 0
    level = 1

    def show_info():
        font = pygame.font.SysFont('times new roman', 20)
        score_surface = font.render(f'Score: {score}  Level: {level}', True, white)
        game_window.blit(score_surface, [10, 10])

    def game_over():
        save_score(user_id, score, level)
        font = pygame.font.SysFont('times new roman', 50)
        message = font.render(f'Game Over! Score: {score}', True, red)
        game_window.blit(message, [window_x // 4, window_y // 3])
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        quit()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'

        if direction == 'UP':
            snake_position[1] -= 10
        elif direction == 'DOWN':
            snake_position[1] += 10
        elif direction == 'LEFT':
            snake_position[0] -= 10
        elif direction == 'RIGHT':
            snake_position[0] += 10

        if (snake_position[0] < 0 or snake_position[0] >= window_x or
                snake_position[1] < 0 or snake_position[1] >= window_y):
            game_over()

        snake_body.insert(0, list(snake_position))
        if snake_position[:2] == fruit_position[:2]:
            score += fruit_position[3]
            fruit_spawn = False
            if score % 30 == 0:
                level += 1
                snake_speed += 2
        else:
            snake_body.pop()

        if time.time() - fruit_position[4] > 10:
            fruit_spawn = False

        if not fruit_spawn:
            fruit_position = generate_food()
            fruit_spawn = True

        for block in snake_body[1:]:
            if snake_position == block:
                game_over()

        game_window.fill(black)
        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(game_window, red, pygame.Rect(fruit_position[0], fruit_position[1], fruit_position[2][0], fruit_position[2][1]))

        show_info()

        pygame.display.update()
        fps.tick(snake_speed)
running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
                if paused:
                    if get_player_data(player):
                        update_person(player, level, score, speed)
                        print("Игра поставлена на паузу и сохранена. Нажмите P, чтобы продолжить.")

    if paused:
        pause_text = game_over_font.render("PAUSE", True, BLACK)
        screen.blit(pause_text, (WIDTH // 2 - 100, HEIGHT // 2 - 30))
        pygame.display.flip()
        clock.tick(5)
        continue
if __name__ == "__main__":
    create_tables()
    username = input("Enter your username: ")
    user_id = get_or_create_user(username)
    game_loop(user_id)
