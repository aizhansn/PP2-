import pygame
import os

# Предварительная инициализация микшера для стабильной работы музыки
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

# Фиксированный размер окна
W, H = 400, 300

# Устанавливаем режим окна
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Music Player")

# Проверка и загрузка фонового изображения
bg_path = "bg.jpg"
if not os.path.exists(bg_path):
    bg_path = "bg.png"  # Попробовать альтернативный формат
    if not os.path.exists(bg_path):
        print("Ошибка: Файл bg.jpg или bg.png отсутствует!")
        pygame.quit()
        exit()

# Загружаем фон и масштабируем под размер окна
bg = pygame.image.load(bg_path).convert()
bg = pygame.transform.scale(bg, (W, H))
screen.blit(bg, (0, 0))
pygame.display.update()

# Список песен
songs = ["songs/Despasito.mp3", "songs/Diki.mp3"]
if not all(os.path.exists(song) for song in songs):
    print("Ошибка: Один или несколько аудиофайлов отсутствуют.")
    pygame.quit()
    exit()

# Загрузка кнопок из папки buttons
buttons = {}
button_paths = {
    "play": "buttons/play.png",
    "pause": "buttons/pause.png",
    "prev": "buttons/prev.png",
    "next": "buttons/next.png"
}
button_sizes = {"play": 7, "pause": 7, "prev": 8, "next": 8}

for name, path in button_paths.items():
    if os.path.exists(path):
        image = pygame.image.load(path).convert_alpha()
        image = pygame.transform.scale(
            image,
            (image.get_width() // button_sizes[name], image.get_height() // button_sizes[name])
        )
        buttons[name] = image
    else:
        print(f"Ошибка: {path} отсутствует!")
        pygame.quit()
        exit()

# Расстояние между иконками
spacing = 80
# Координаты кнопок – располагаем их в нижней части окна относительно центра
prev_rect = buttons["prev"].get_rect(center=(W // 2 - spacing, H - 50))
play_rect = buttons["play"].get_rect(center=(W // 2, H - 50))
pause_rect = buttons["pause"].get_rect(center=(W // 2 + spacing, H - 50))
next_rect = buttons["next"].get_rect(center=(W // 2 + 2 * spacing, H - 50))

# Первоначальная отрисовка кнопок
screen.blit(buttons["prev"], prev_rect)
screen.blit(buttons["play"], play_rect)
screen.blit(buttons["pause"], pause_rect)
screen.blit(buttons["next"], next_rect)
pygame.display.update()

pygame.mixer.music.load(songs[0])
count = 0
is_play = False
clock = pygame.time.Clock()

while True:
    pygame.event.pump()  # Обработка системных событий
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if play_rect.collidepoint(event.pos):
                is_play = not is_play
                if count != 1:
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.unpause()
                count = 1
            elif pause_rect.collidepoint(event.pos):
                is_play = not is_play
                pygame.mixer.music.pause()
            elif next_rect.collidepoint(event.pos):
                songs = songs[1:] + [songs[0]]
                pygame.mixer.music.load(songs[0])
                pygame.mixer.music.play()
            elif prev_rect.collidepoint(event.pos):
                songs = [songs[-1]] + songs[:-1]
                pygame.mixer.music.load(songs[0])
                pygame.mixer.music.play()
    
    # Отрисовка фона и кнопок на каждом кадре
    screen.blit(bg, (0, 0))
    screen.blit(buttons["prev"], prev_rect)
    screen.blit(buttons["play"], play_rect)
    screen.blit(buttons["pause"], pause_rect)
    screen.blit(buttons["next"], next_rect)
    
    pygame.display.update()
    clock.tick(60)
