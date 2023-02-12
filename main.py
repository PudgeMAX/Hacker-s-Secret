import pygame
import os
import sys
import moviepy.editor
import random as r

video = moviepy.editor.VideoFileClip("resources/hacker's secret.mp4")
clip_resized = video.resize(height=500, width=200)
    

FPS = 60
pygame.init()
pygame.mixer.init()
size = WIDTH, HEIGHT = 888, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Hacker's Secret")
clock = pygame.time.Clock()
english_mode = False
play_music = True
rus_alph = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')


def load_image(name, colorkey=None):
    fullname = os.path.join('resources', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def terminate():
    pygame.quit()
    sys.exit()


class GameMessage(pygame.sprite.Sprite):
    def __init__(self, text, color=(14, 107, 14)):
        super().__init__()
        font = pygame.font.Font(os.path.join('resources', 'Hacked Cyr.ttf'), 35)
        self.image = load_image('frame.png')
        self.rect = self.image.get_rect()
        self.text = font.render(text, True, color)
        self.x = 144
        self.y = 200

    def draw(self, x, y):
        self.x = x
        self.y = y
        screen.blit(self.image, (self.x, self.y))
        screen.blit(self.text, (self.x + 20, self.y + 20))

    def update_text(self, text, color=(14, 107, 14)):
        font = pygame.font.Font(os.path.join('resources', 'Hacked Cyr.ttf'), 35)
        self.text = font.render(text, True, color)


class Button(pygame.sprite.Sprite):
    def __init__(self, image):
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect()


def prompt_file():
    top = tkinter.Tk()
    top.withdraw()
    file_name = tkinter.filedialog.askopenfilename(parent=top)
    top.destroy()
    return file_name


def choose_word():
    global english_mode
    if english_mode:
        language = r.randint(0, 100)
        if language <= 50:  
            with open(os.path.join('resources', 'rus_words.txt')) as word:
                content = word.read()
                content = content.split(',')
        else:
            with open(os.path.join('resources', 'en_words.txt'), encoding='utf-8') as word:
                content = word.read()
                content = content.split(',')
    else:
        with open(os.path.join('resources', 'rus_words.txt')) as word:
            content = word.read()
            content = content.split(',')
    return content[r.randint(0, len(content) - 1)]


def main_game():
    global rus_alph
    main = True
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.Font(os.path.join('resources', 'Hacked Cyr.ttf'), 50)
    current_line = ['>> ']
    unknown_line = choose_word()
    messages = []
    messages.append(GameMessage(f'введи слово "{unknown_line}"'))
    x = 144
    y = 600
    remove = False
    count = 0
    check = False
    seconds = 10
    game_over = False
    win = False
    time = True
    while main:
        if play_music and not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(os.path.join('resources', 'bgm.mp3'))
            pygame.mixer.music.play()
        elif not play_music and pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        current_line_text = font.render(''.join(current_line), True, (14, 107, 14))
        time_text = font.render(str(seconds), True, (14, 107, 14))
        if game_over:
            game_over_window()
        if win:
            seconds = 10
            unknown_line = choose_word()
            win = False
            messages[0].update_text(f'введи слово "{unknown_line}"')
            current_line = ['>> ']
            time = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
            elif event.type == pygame.USEREVENT:
                if time:
                    seconds -= 1
            elif event.type == pygame.KEYDOWN:
                try:
                    if unknown_line.lower()[0] in rus_alph:
                        if event.key == pygame.K_q:
                            current_line.append('й')
                        elif event.key == pygame.K_w:
                            current_line.append('ц')
                        elif event.key == pygame.K_e:
                            current_line.append('у')
                        elif event.key == pygame.K_r:
                            current_line.append('к')
                        elif event.key == pygame.K_t:
                            current_line.append('е')
                        elif event.key == pygame.K_y:
                            current_line.append('н')
                        elif event.key == pygame.K_u:
                            current_line.append('г')
                        elif event.key == pygame.K_i:
                            current_line.append('ш')
                        elif event.key == pygame.K_o:
                            current_line.append('щ')
                        elif event.key == pygame.K_p:
                            current_line.append('з')
                        elif event.key == pygame.K_a:
                            current_line.append('ф')
                        elif event.key == pygame.K_s:
                            current_line.append('ы')
                        elif event.key == pygame.K_d:
                            current_line.append('в')
                        elif event.key == pygame.K_f:
                            current_line.append('а')
                        elif event.key == pygame.K_g:
                            current_line.append('п')
                        elif event.key == pygame.K_h:
                            current_line.append('р')
                        elif event.key == pygame.K_j:
                            current_line.append('о')
                        elif event.key == pygame.K_k:
                            current_line.append('л')
                        elif event.key == pygame.K_l:
                            current_line.append('д')
                        elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_SEMICOLON:
                            current_line.append(':')
                        elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_6:
                            current_line.append(':')
                        elif event.key == 1098:
                            current_line.append('ъ')
                        elif event.key == 1093:
                            current_line.append('х')
                        elif event.key == 1078:
                            current_line.append('ж')
                        elif event.key == 1101:
                            current_line.append('э')
                        elif event.key == pygame.K_z:
                            current_line.append('я')
                        elif event.key == pygame.K_x:
                            current_line.append('ч')
                        elif event.key == pygame.K_c:
                            current_line.append('с')
                        elif event.key == pygame.K_v:
                            current_line.append('м')
                        elif event.key == pygame.K_b:
                            current_line.append('и')
                        elif event.key == pygame.K_n:
                            current_line.append('т')
                        elif event.key == pygame.K_m:
                            current_line.append('ь')
                        elif event.key == 1102:
                            current_line.append('ю')
                        elif event.key == 1073:
                            current_line.append('б')
                        elif event.key == 46:
                            current_line.append('ю')
                        elif event.key == 44:
                            current_line.append('б')
                        elif event.key == 59:
                            current_line.append('ж')
                        elif event.key == 39:
                            current_line.append('э')
                        elif event.key == 91:
                            current_line.append('х')
                        elif event.key == 93:
                            current_line.append('ъ')
                        elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_SLASH:
                            current_line.append(',')
                        elif event.key == pygame.K_SLASH:
                            current_line.append('.')
                        elif event.key == pygame.K_BACKQUOTE:
                            current_line.append('ё')
                        elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_1:
                            current_line.append('!')
                        elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_2:
                            current_line.append('@')
                        elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_3:
                            current_line.append('#')
                        elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_4:
                            current_line.append('$')
                        elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_5:
                            current_line.append('%')
                        elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_7:
                            current_line.append('&')
                        elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_8:
                            current_line.append('*')
                        elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_9:
                            current_line.append('(')
                        elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_0:
                            current_line.append(')')
                        elif event.key == pygame.K_0:
                            current_line.append('0')
                        elif event.key == pygame.K_1:
                            current_line.append('1')
                        elif event.key == pygame.K_2:
                            current_line.append('2')
                        elif event.key == pygame.K_3:
                            current_line.append('3')
                        elif event.key == pygame.K_4:
                            current_line.append('4')
                        elif event.key == pygame.K_5:
                            current_line.append('5')
                        elif event.key == pygame.K_6:
                            current_line.append('6')
                        elif event.key == pygame.K_7:
                            current_line.append('7')
                        elif event.key == pygame.K_8:
                            current_line.append('8')
                        elif event.key == pygame.K_9:
                            current_line.append('9')
                        elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_MINUS:
                            current_line.append('_')
                        elif event.key == pygame.K_MINUS:
                            current_line.append('-')
                        elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_EQUALS:
                            current_line.append('+')
                        elif event.key == pygame.K_EQUALS:
                            current_line.append('=')
                        elif event.key == pygame.K_BACKSPACE:
                            remove = True
                        elif event.key == pygame.K_SPACE:
                            current_line.append(' ')
                        elif event.key == pygame.K_RETURN:
                            check = True
                    else:
                        if event.key == pygame.K_q:
                            current_line.append('q')
                        elif event.key == pygame.K_w:
                            current_line.append('w')
                        elif event.key == pygame.K_e:
                            current_line.append('e')
                        elif event.key == pygame.K_r:
                            current_line.append('r')
                        elif event.key == pygame.K_t:
                            current_line.append('t')
                        elif event.key == pygame.K_y:
                            current_line.append('y')
                        elif event.key == pygame.K_u:
                            current_line.append('u')
                        elif event.key == pygame.K_i:
                            current_line.append('i')
                        elif event.key == pygame.K_o:
                            current_line.append('o')
                        elif event.key == pygame.K_p:
                            current_line.append('p')
                        elif event.key == pygame.K_a:
                            current_line.append('a')
                        elif event.key == pygame.K_s:
                            current_line.append('s')
                        elif event.key == pygame.K_d:
                            current_line.append('d')
                        elif event.key == pygame.K_f:
                            current_line.append('f')
                        elif event.key == pygame.K_g:
                            current_line.append('g')
                        elif event.key == pygame.K_h:
                            current_line.append('h')
                        elif event.key == pygame.K_j:
                            current_line.append('j')
                        elif event.key == pygame.K_k:
                            current_line.append('k')
                        elif event.key == pygame.K_l:
                            current_line.append('l')
                        elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_SEMICOLON:
                            current_line.append(':')
                        elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_COMMA:
                            current_line.append('<')
                        elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_PERIOD:
                            current_line.append('>')
                        elif event.key == pygame.K_SEMICOLON:
                            current_line.append(';')
                        elif event.key == pygame.K_QUOTE:
                            current_line.append('"')
                        elif event.key == pygame.K_z:
                            current_line.append('z')
                        elif event.key == pygame.K_x:
                            current_line.append('x')
                        elif event.key == pygame.K_c:
                            current_line.append('c')
                        elif event.key == pygame.K_v:
                            current_line.append('v')
                        elif event.key == pygame.K_b:
                            current_line.append('b')
                        elif event.key == pygame.K_n:
                            current_line.append('n')
                        elif event.key == pygame.K_m:
                            current_line.append('m')
                        elif event.key == pygame.K_COMMA:
                            current_line.append(',')
                        elif event.key == pygame.K_PERIOD:
                            current_line.append('.')
                        elif event.key == pygame.K_SLASH:
                            current_line.append('/')
                        elif event.key == pygame.K_BACKQUOTE:
                            current_line.append('`')
                        elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_1:
                            current_line.append('!')
                        elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_2:
                            current_line.append('@')
                        elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_3:
                            current_line.append('#')
                        elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_4:
                            current_line.append('$')
                        elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_5:
                            current_line.append('%')
                        elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_7:
                            current_line.append('&')
                        elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_8:
                            current_line.append('*')
                        elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_9:
                            current_line.append('(')
                        elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_0:
                            current_line.append(')')
                        elif event.key == pygame.K_0:
                            current_line.append('0')
                        elif event.key == pygame.K_1:
                            current_line.append('1')
                        elif event.key == pygame.K_2:
                            current_line.append('2')
                        elif event.key == pygame.K_3:
                            current_line.append('3')
                        elif event.key == pygame.K_4:
                            current_line.append('4')
                        elif event.key == pygame.K_5:
                            current_line.append('5')
                        elif event.key == pygame.K_6:
                            current_line.append('6')
                        elif event.key == pygame.K_7:
                            current_line.append('7')
                        elif event.key == pygame.K_8:
                            current_line.append('8')
                        elif event.key == pygame.K_9:
                            current_line.append('9')
                        elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_MINUS:
                            current_line.append('_')
                        elif event.key == pygame.K_MINUS:
                            current_line.append('-')
                        elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_EQUALS:
                            current_line.append('+')
                        elif event.key == pygame.K_EQUALS:
                            current_line.append('=')
                        elif event.key == pygame.K_BACKSPACE:
                            remove = True
                        elif event.key == pygame.K_SPACE:
                            current_line.append(' ')
                        elif event.key == pygame.K_RETURN:
                            check = True
                        elif event.key == 1078:
                            current_line.append(';')
                        elif event.key == 1101:
                            current_line.append('"')
                        elif event.key == 1102:
                            current_line.append('.')
                        elif event.key == 1073:
                            current_line.append(',')
                except IndexError:
                    pass

            elif event.type == pygame.KEYUP:
                remove = False
        if seconds < 0:
            seconds = 0
            messages[0].update_text('время вышло!')
            game_over = True

        if remove:
            count += 1
            if count % 5 == 0:
                if len(current_line) > 1:
                    current_line.pop(-1)
        if check:
            if ''.join(current_line[1:]) == unknown_line.lower():
                messages[0].update_text('отлично!')
                check = False
                win = True
                time = False
            else:
                messages[0].update_text(f'неверно! введи слово "{unknown_line}"', (255, 36, 0))
                check = False
        y -= 5
        if y < 300:
            y = 300

        screen.fill((0, 0, 0))
        messages[0].draw(x, y)
        screen.blit(current_line_text, (0, 0))
        screen.blit(time_text, (800, 0))
        clock.tick(FPS)
        pygame.display.flip()

def helping():
    main = True
    font = pygame.font.Font(os.path.join('resources', 'Hacked Cyr.ttf'), 23)
    words = [
        'help - выводит текущую подсказку',
        'start train.exe - запускает тренировку',
        'start settings.exe - запускает окно с настройками',
        'start cmd.exe - запускает консоль',
        'cls - очищает консоль',
        'clear - очищает консоль',
        'select music on - включает музыку',
        'select music off - выключает музыку',
        'select english_mode on - включает английский режим',
        'select english_mode off - выключает английский режим'
    ]
    main_window = load_image('dialog_window.png')
    button_cross = load_image('cross_dialog_btn.png')
    button_cross_rect = button_cross.get_rect().move(640, 35)
    desktop_background = pygame.transform.scale(load_image("desktop_bg.jpg"), (888, 500))
    switch_btn = load_image('switch_btn_off.png')
    switch_btn_rect = switch_btn.get_rect().move(575, 65)
    y = 60
    while main:
        if play_music and not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(os.path.join('resources', 'bgm.mp3'))
            pygame.mixer.music.play()
        elif not play_music and pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if button_cross_rect.collidepoint(pygame.mouse.get_pos()):
                        main = False
                        cmd()

        screen.fill((0, 0, 0))
        screen.blit(desktop_background, (0, 0))
        screen.blit(main_window, (35, 35))
        screen.blit(button_cross, (button_cross_rect.x, button_cross_rect.y))
        for text in words:
            y += 30
            screen.blit(font.render(text, True, (14, 107, 14)), (75, y))
        y = 60
        clock.tick(FPS)
        pygame.display.flip()


def settings():
    global english_mode, play_music
    main = True
    font = pygame.font.Font(os.path.join('resources', 'Hacked Cyr.ttf'), 35)
    func1_text = 'использовать английские слова'
    func2_text = 'включить/выключить музыку'
    version_text = 'v1.0'
    main_window = load_image('dialog_window.png')
    button_cross = load_image('cross_dialog_btn.png')
    button_cross_rect = button_cross.get_rect().move(640, 35)
    desktop_background = pygame.transform.scale(load_image("desktop_bg.jpg"), (888, 500))
    switch_btn = load_image('switch_btn_off.png')
    switch_btn_rect = switch_btn.get_rect().move(575, 65)
    switch_btn1 = load_image('switch_btn_on.png')
    switch_btn_rect1 = switch_btn1.get_rect().move(575, 100)
    while main:
        if play_music and not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(os.path.join('resources', 'bgm.mp3'))
            pygame.mixer.music.play()
        elif not play_music and pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        if english_mode:
            switch_btn = load_image('switch_btn_on.png')
            switch_btn_rect = switch_btn.get_rect().move(575, 65)
        if not play_music:
            switch_btn1 = load_image('switch_btn_off.png')
            switch_btn_rect1 = switch_btn1.get_rect().move(575, 100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if button_cross_rect.collidepoint(pygame.mouse.get_pos()):
                        main = False
                        main_menu()
                    elif switch_btn_rect.collidepoint(pygame.mouse.get_pos()):
                        if english_mode:
                            english_mode = False
                            switch_btn = load_image('switch_btn_off.png')
                            switch_btn_rect = switch_btn.get_rect().move(575, 65)
                        else:
                            english_mode = True
                            switch_btn = load_image('switch_btn_on.png')
                            switch_btn_rect = switch_btn.get_rect().move(575, 65)
                    elif switch_btn_rect1.collidepoint(pygame.mouse.get_pos()):
                        if play_music:
                            play_music = False
                            switch_btn1 = load_image('switch_btn_off.png')
                            switch_btn_rect1 = switch_btn1.get_rect().move(575, 100)
                        else:
                            play_music = True
                            switch_btn1 = load_image('switch_btn_on.png')
                            switch_btn_rect1 = switch_btn1.get_rect().move(575, 100)

        screen.fill((0, 0, 0))
        screen.blit(desktop_background, (0, 0))
        screen.blit(main_window, (35, 35))
        screen.blit(button_cross, (button_cross_rect.x, button_cross_rect.y))
        screen.blit(font.render(func1_text, True, (14, 107, 14)), (60, 60))
        screen.blit(font.render(func2_text, True, (14, 107, 14)), (60, 95))
        screen.blit(font.render(version_text, True, (14, 107, 14)), (560, 410))
        screen.blit(switch_btn, (switch_btn_rect.x, switch_btn_rect.y))
        screen.blit(switch_btn1, (switch_btn_rect1.x, switch_btn_rect1.y))
        clock.tick(FPS)
        pygame.display.flip()


def cmd():
    global english_mode, play_music
    commands = [
        'start train.exe',
        'start settings.exe',
        'start cmd.exe',
        'cls',
        'clear',
        'select music on',
        'select music off',
        'select english_mode on',
        'select english_mode off',
        'help'
    ]
    main = True
    font = pygame.font.Font(os.path.join('resources', 'Hacked Cyr.ttf'), 35)
    current_line = ['>> ']
    main_window = load_image('dialog_window.png')
    button_cross = load_image('cross_dialog_btn.png')
    button_cross_rect = button_cross.get_rect().move(640, 35)
    desktop_background = pygame.transform.scale(load_image("desktop_bg.jpg"), (888, 500))
    switch_btn = load_image('switch_btn_off.png')
    switch_btn_rect = switch_btn.get_rect().move(575, 65)
    remove = False
    check = False
    count = 0
    while main:
        if play_music and not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(os.path.join('resources', 'bgm.mp3'))
            pygame.mixer.music.play()
        elif not play_music and pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        current_line_text = font.render(''.join(current_line), True, (14, 107, 14))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
            elif event.type == pygame.KEYDOWN:
                try:
                    if event.key == pygame.K_q:
                        current_line.append('q')
                    elif event.key == pygame.K_w:
                        current_line.append('w')
                    elif event.key == pygame.K_e:
                        current_line.append('e')
                    elif event.key == pygame.K_r:
                        current_line.append('r')
                    elif event.key == pygame.K_t:
                        current_line.append('t')
                    elif event.key == pygame.K_y:
                        current_line.append('y')
                    elif event.key == pygame.K_u:
                        current_line.append('u')
                    elif event.key == pygame.K_i:
                        current_line.append('i')
                    elif event.key == pygame.K_o:
                        current_line.append('o')
                    elif event.key == pygame.K_p:
                        current_line.append('p')
                    elif event.key == pygame.K_a:
                        current_line.append('a')
                    elif event.key == pygame.K_s:
                        current_line.append('s')
                    elif event.key == pygame.K_d:
                        current_line.append('d')
                    elif event.key == pygame.K_f:
                        current_line.append('f')
                    elif event.key == pygame.K_g:
                        current_line.append('g')
                    elif event.key == pygame.K_h:
                        current_line.append('h')
                    elif event.key == pygame.K_j:
                        current_line.append('j')
                    elif event.key == pygame.K_k:
                        current_line.append('k')
                    elif event.key == pygame.K_l:
                        current_line.append('l')
                    elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_SEMICOLON:
                        current_line.append(':')
                    elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_COMMA:
                        current_line.append('<')
                    elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_PERIOD:
                        current_line.append('>')
                    elif event.key == pygame.K_SEMICOLON:
                        current_line.append(';')
                    elif event.key == pygame.K_QUOTE:
                        current_line.append('"')
                    elif event.key == pygame.K_z:
                        current_line.append('z')
                    elif event.key == pygame.K_x:
                        current_line.append('x')
                    elif event.key == pygame.K_c:
                        current_line.append('c')
                    elif event.key == pygame.K_v:
                        current_line.append('v')
                    elif event.key == pygame.K_b:
                        current_line.append('b')
                    elif event.key == pygame.K_n:
                        current_line.append('n')
                    elif event.key == pygame.K_m:
                        current_line.append('m')
                    elif event.key == pygame.K_COMMA:
                        current_line.append(',')
                    elif event.key == pygame.K_PERIOD:
                        current_line.append('.')
                    elif event.key == pygame.K_SLASH:
                        current_line.append('/')
                    elif event.key == pygame.K_BACKQUOTE:
                        current_line.append('`')
                    elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_1:
                        current_line.append('!')
                    elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_2:
                        current_line.append('@')
                    elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_3:
                        current_line.append('#')
                    elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_4:
                        current_line.append('$')
                    elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_5:
                        current_line.append('%')
                    elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_7:
                        current_line.append('&')
                    elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_8:
                        current_line.append('*')
                    elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_9:
                        current_line.append('(')
                    elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_0:
                        current_line.append(')')
                    elif event.key == pygame.K_0:
                        current_line.append('0')
                    elif event.key == pygame.K_1:
                        current_line.append('1')
                    elif event.key == pygame.K_2:
                        current_line.append('2')
                    elif event.key == pygame.K_3:
                        current_line.append('3')
                    elif event.key == pygame.K_4:
                        current_line.append('4')
                    elif event.key == pygame.K_5:
                        current_line.append('5')
                    elif event.key == pygame.K_6:
                        current_line.append('6')
                    elif event.key == pygame.K_7:
                        current_line.append('7')
                    elif event.key == pygame.K_8:
                        current_line.append('8')
                    elif event.key == pygame.K_9:
                        current_line.append('9')
                    elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_MINUS:
                        current_line.append('_')
                    elif event.key == pygame.K_MINUS:
                        current_line.append('-')
                    elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_EQUALS:
                        current_line.append('+')
                    elif event.key == pygame.K_EQUALS:
                        current_line.append('=')
                    elif event.key == pygame.K_BACKSPACE:
                        remove = True
                    elif event.key == pygame.K_SPACE:
                        current_line.append(' ')
                    elif event.key == pygame.K_RETURN:
                        check = True
                    elif event.key == 1078:
                        current_line.append(';')
                    elif event.key == 1101:
                        current_line.append('"')
                    elif event.key == 1102:
                        current_line.append('.')
                    elif event.key == 1073:
                        current_line.append(',')
                except IndexError:
                    pass

            elif event.type == pygame.KEYUP:
                remove = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if button_cross_rect.collidepoint(pygame.mouse.get_pos()):
                        main = False
                        main_menu()

        if remove:
            count += 1
            if count % 5 == 0:
                if len(current_line) > 1:
                    current_line.pop(-1)
        if check:
            if ''.join(current_line[1:]) in commands:
                if ''.join(current_line[1:]) == 'help':
                    current_line = ['>> ']
                    main = False
                    helping()
                elif ''.join(current_line[1:]) == 'start train.exe':
                    current_line = ['>> ']
                    main = False
                    main_game()
                elif ''.join(current_line[1:]) == 'start settings.exe':
                    current_line = ['>> ']
                    main = False
                    settings()
                elif ''.join(current_line[1:]) == 'start cmd.exe':
                    current_line = ['>> ']
                    main = False
                    cmd()
                elif ''.join(current_line[1:]) == 'cls' or ''.join(current_line[1:]) == 'clear':
                    current_line = ['>> ']
                elif ''.join(current_line[1:]) == 'select music on':
                    current_line = ['>> ']
                    play_music = True
                elif ''.join(current_line[1:]) == 'select music off':
                    current_line = ['>> ']
                    play_music = False
                elif ''.join(current_line[1:]) == 'select english_mode on':
                    current_line = ['>> ']
                    english_mode = True
                elif ''.join(current_line[1:]) == 'select english_mode off':
                    current_line = ['>> ']
                    english_mode = False
            check = False


        screen.fill((0, 0, 0))
        screen.blit(desktop_background, (0, 0))
        screen.blit(main_window, (35, 35))
        screen.blit(button_cross, (button_cross_rect.x, button_cross_rect.y))
        screen.blit(current_line_text, (70, 70))
        clock.tick(FPS)
        pygame.display.flip()



def main_menu():
    main = True
    font = pygame.font.Font(os.path.join('resources', 'Hacked Cyr.ttf'), 50)
    settings_btn = Button(load_image('settings_btn.png'))
    settings_btn.rect.x, settings_btn.rect.y = 25, 50
    cmd_btn = Button(load_image('cmd_btn.png'))
    cmd_btn.rect.x, cmd_btn.rect.y = 25, 120
    desktop_background = pygame.transform.scale(load_image("desktop_bg.jpg"), (888, 500))
    while main:
        if play_music and not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(os.path.join('resources', 'bgm.mp3'))
            pygame.mixer.music.play()
        elif not play_music and pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and settings_btn.rect.collidepoint(pygame.mouse.get_pos()):
                    main = False
                    settings()
                elif event.button == 1 and cmd_btn.rect.collidepoint(pygame.mouse.get_pos()):
                    main = False
                    cmd()

        screen.fill((0, 0, 0))
        screen.blit(desktop_background, (0, 0))
        screen.blit(settings_btn.image, (settings_btn.rect.x, settings_btn.rect.y))
        screen.blit(cmd_btn.image, (cmd_btn.rect.x, cmd_btn.rect.y))
        clock.tick(FPS)
        pygame.display.flip()


def tutorial():
    main = True
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.Font(os.path.join('resources', 'Hacked Cyr.ttf'), 50)
    current_line = ['>> ']
    unknown_line = 'start'
    messages = []
    messages.append(GameMessage('введи слово "start"'))
    x = 144
    y = 600
    remove = False
    count = 0
    check = False
    seconds = 60
    game_over = False
    to_main_game = False
    while main:
        if play_music and not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(os.path.join('resources', 'bgm.mp3'))
            pygame.mixer.music.play()
        elif not play_music and pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        current_line_text = font.render(''.join(current_line), True, (14, 107, 14))
        time_text = font.render(str(seconds), True, (14, 107, 14))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
            elif event.type == pygame.USEREVENT:
                if not to_main_game:
                    seconds -= 1
            elif event.type == pygame.KEYDOWN:
                if game_over:
                    tutorial()
                if to_main_game:
                    main = False
                    main_menu()
                try:
                    if event.key == pygame.K_q:
                        current_line.append('q')
                    elif event.key == pygame.K_w:
                        current_line.append('w')
                    elif event.key == pygame.K_e:
                        current_line.append('e')
                    elif event.key == pygame.K_r:
                        current_line.append('r')
                    elif event.key == pygame.K_t:
                        current_line.append('t')
                    elif event.key == pygame.K_y:
                        current_line.append('y')
                    elif event.key == pygame.K_u:
                        current_line.append('u')
                    elif event.key == pygame.K_i:
                        current_line.append('i')
                    elif event.key == pygame.K_o:
                        current_line.append('o')
                    elif event.key == pygame.K_p:
                        current_line.append('p')
                    elif event.key == pygame.K_a:
                        current_line.append('a')
                    elif event.key == pygame.K_s:
                        current_line.append('s')
                    elif event.key == pygame.K_d:
                        current_line.append('d')
                    elif event.key == pygame.K_f:
                        current_line.append('f')
                    elif event.key == pygame.K_g:
                        current_line.append('g')
                    elif event.key == pygame.K_h:
                        current_line.append('h')
                    elif event.key == pygame.K_j:
                        current_line.append('j')
                    elif event.key == pygame.K_k:
                        current_line.append('k')
                    elif event.key == pygame.K_l:
                        current_line.append('l')
                    elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_SEMICOLON:
                        current_line.append(':')
                    elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_COMMA:
                        current_line.append('<')
                    elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_PERIOD:
                        current_line.append('>')
                    elif event.key == pygame.K_SEMICOLON:
                        current_line.append(';')
                    elif event.key == pygame.K_QUOTE:
                        current_line.append('"')
                    elif event.key == pygame.K_z:
                        current_line.append('z')
                    elif event.key == pygame.K_x:
                        current_line.append('x')
                    elif event.key == pygame.K_c:
                        current_line.append('c')
                    elif event.key == pygame.K_v:
                        current_line.append('v')
                    elif event.key == pygame.K_b:
                        current_line.append('b')
                    elif event.key == pygame.K_n:
                        current_line.append('n')
                    elif event.key == pygame.K_m:
                        current_line.append('m')
                    elif event.key == pygame.K_COMMA:
                        current_line.append(',')
                    elif event.key == pygame.K_PERIOD:
                        current_line.append('.')
                    elif event.key == pygame.K_SLASH:
                        current_line.append('/')
                    elif event.key == pygame.K_BACKQUOTE:
                        current_line.append('`')
                    elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_1:
                        current_line.append('!')
                    elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_2:
                        current_line.append('@')
                    elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_3:
                        current_line.append('#')
                    elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_4:
                        current_line.append('$')
                    elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_5:
                        current_line.append('%')
                    elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_7:
                        current_line.append('&')
                    elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_8:
                        current_line.append('*')
                    elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_9:
                        current_line.append('(')
                    elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_0:
                        current_line.append(')')
                    elif event.key == pygame.K_0:
                        current_line.append('0')
                    elif event.key == pygame.K_1:
                        current_line.append('1')
                    elif event.key == pygame.K_2:
                        current_line.append('2')
                    elif event.key == pygame.K_3:
                        current_line.append('3')
                    elif event.key == pygame.K_4:
                        current_line.append('4')
                    elif event.key == pygame.K_5:
                        current_line.append('5')
                    elif event.key == pygame.K_6:
                        current_line.append('6')
                    elif event.key == pygame.K_7:
                        current_line.append('7')
                    elif event.key == pygame.K_8:
                        current_line.append('8')
                    elif event.key == pygame.K_9:
                        current_line.append('9')
                    elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_MINUS:
                        current_line.append('_')
                    elif event.key == pygame.K_MINUS:
                        current_line.append('-')
                    elif pygame.key.get_mods() & pygame.KMOD_SHIFT and event.key == pygame.K_EQUALS:
                        current_line.append('+')
                    elif event.key == pygame.K_EQUALS:
                        current_line.append('=')
                    elif event.key == pygame.K_BACKSPACE:
                        remove = True
                    elif event.key == pygame.K_SPACE:
                        current_line.append(' ')
                    elif event.key == pygame.K_RETURN:
                        check = True
                except IndexError:
                    pass

            elif event.type == pygame.KEYUP:
                remove = False
        if seconds < 0:
            seconds = 0
            messages[0].update_text('время вышло!')
            game_over = True

        if remove:
            count += 1
            if count % 5 == 0:
                if len(current_line) > 1:
                    current_line.pop(-1)
        if check:
            if ''.join(current_line[1:]) == unknown_line:
                messages[0].update_text('отлично!')
                check = False
                to_main_game = True
            else:
                messages[0].update_text('неверно!')
                check = False
        y -= 5
        if y < 300:
            y = 300

        screen.fill((0, 0, 0))
        messages[0].draw(x, y)
        screen.blit(current_line_text, (0, 0))
        screen.blit(time_text, (800, 0))
        clock.tick(FPS)
        pygame.display.flip()


def welcome():
    tut = True
    font = pygame.font.Font(os.path.join('resources', 'Hacked Cyr.ttf'), 50)
    text_coord = 0
    hello_words = []
    hello_words2 = []
    hello_words3 = []
    hello_words4 = []
    count = 0
    flag = True
    while tut:
        if play_music and not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(os.path.join('resources', 'bgm.mp3'))
            pygame.mixer.music.play()
        elif not play_music and pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        screen.fill((0, 0, 0))
        try:
            if count % 4 == 0:
                if count == 0:
                    hello_words.append('>')
                elif count == 4:
                    hello_words.append('>')
                elif count == 8:
                    hello_words.append(' ')
                elif count == 12:
                    hello_words.append('п')
                elif count == 16:
                    hello_words.append('р')
                elif count == 20:
                    hello_words.append('и')
                elif count == 24:
                    hello_words.append('в')
                elif count == 28:
                    hello_words.append('е')
                elif count == 32:
                    hello_words.append('т')
                elif count == 5004:
                    hello_words.remove('т')
                elif count == 5008:
                    hello_words.remove('е')
                elif count == 5012:
                    hello_words.remove('в')
                elif count == 5016:
                    hello_words.remove('и')
                elif count == 5020:
                    hello_words.remove('р')
                elif count == 5024:
                    hello_words.remove('п')
                elif count == 10004:
                    hello_words.append('э')
                elif count == 10008:
                    hello_words.append('т')
                elif count == 10012:
                    hello_words.append('о')
                elif count == 10016:
                    hello_words.append(' ')
                elif count == 10020:
                    hello_words.append('х')
                elif count == 10024:
                    hello_words.append('а')
                elif count == 10028:
                    hello_words.append('к')
                elif count == 10032:
                    hello_words.append('е')
                elif count == 10036:
                    hello_words.append('р')
                elif count == 10040:
                    hello_words.append('с')
                elif count == 10044:
                    hello_words.append('к')
                elif count == 10048:
                    hello_words.append('и')
                elif count == 10052:
                    hello_words.append('й')
                elif count == 10056:
                    hello_words.append(' ')
                elif count == 10060:
                    hello_words2.append('т')
                elif count == 10064:
                    hello_words2.append('р')
                elif count == 10068:
                    hello_words2.append('е')
                elif count == 10072:
                    hello_words2.append('н')
                elif count == 10076:
                    hello_words2.append('а')
                elif count == 10080:
                    hello_words2.append('ж')
                elif count == 10084:
                    hello_words2.append('ё')
                elif count == 10088:
                    hello_words2.append('р')
                elif count == 10092:
                    hello_words2.append(' ')
                elif count == 10096:
                    hello_words2.append('д')
                elif count == 10100:
                    hello_words2.append('л')
                elif count == 10104:
                    hello_words2.append('я')
                elif count == 10108:
                    hello_words2.append(' ')
                elif count == 10112:
                    hello_words3.append('с')
                elif count == 10116:
                    hello_words3.append('к')
                elif count == 10120:
                    hello_words3.append('о')
                elif count == 10124:
                    hello_words3.append('р')
                elif count == 10128:
                    hello_words3.append('о')
                elif count == 10132:
                    hello_words3.append('с')
                elif count == 10136:
                    hello_words3.append('т')
                elif count == 10140:
                    hello_words3.append('н')
                elif count == 10144:
                    hello_words3.append('о')
                elif count == 10148:
                    hello_words3.append('й')
                elif count == 10152:
                    hello_words3.append(' ')
                elif count == 10156:
                    hello_words3.append('п')
                elif count == 10160:
                    hello_words3.append('е')
                elif count == 10164:
                    hello_words3.append('ч')
                elif count == 10168:
                    hello_words3.append('а')
                elif count == 10172:
                    hello_words3.append('т')
                elif count == 10176:
                    hello_words3.append('и')
                elif count == 10180:
                    hello_words3.append(' ')
                elif count == 10184:
                    hello_words4.append('н')
                elif count == 10188:
                    hello_words4.append('а')
                elif count == 10192:
                    hello_words4.append(' ')
                elif count == 10196:
                    hello_words4.append('к')
                elif count == 10200:
                    hello_words4.append('л')
                elif count == 10204:
                    hello_words4.append('а')
                elif count == 10208:
                    hello_words4.append('в')
                elif count == 10212:
                    hello_words4.append('и')
                elif count == 10216:
                    hello_words4.append('а')
                elif count == 10220:
                    hello_words4.append('т')
                elif count == 10224:
                    hello_words4.append('у')
                elif count == 10228:
                    hello_words4.append('р')
                elif count == 10232:
                    hello_words4.append('е')
                elif count == 15000:
                    hello_words4.remove('е')
                elif count == 15004:
                    hello_words4.remove('р')
                elif count == 15008:
                    hello_words4.remove('у')
                elif count == 15012:
                    hello_words4.remove('т')
                elif count == 15016:
                    hello_words4.remove('а')
                elif count == 15020:
                    hello_words4.remove('и')
                elif count == 15024:
                    hello_words4.remove('в')
                elif count == 15028:
                    hello_words4.remove('а')
                elif count == 15032:
                    hello_words4.remove('л')
                elif count == 15036:
                    hello_words4.remove('к')
                elif count == 15040:
                    hello_words4.remove(' ')
                elif count == 15044:
                    hello_words4.remove('а')
                elif count == 15048:
                    hello_words4.remove('н')
                elif count == 15052:
                    hello_words3.remove(' ')
                elif count == 15056:
                    hello_words3.remove('и')
                elif count == 15060:
                    hello_words3.remove('т')
                elif count == 15064:
                    hello_words3.remove('а')
                elif count == 15068:
                    hello_words3.remove('ч')
                elif count == 15072:
                    hello_words3.remove('е')
                elif count == 15076:
                    hello_words3.remove('п')
                elif count == 15080:
                    hello_words3.remove(' ')
                elif count == 15084:
                    hello_words3.remove('й')
                elif count == 15088:
                    hello_words3.remove('о')
                elif count == 15092:
                    hello_words3.remove('н')
                elif count == 15096:
                    hello_words3.remove('т')
                elif count == 15100:
                    hello_words3.remove('с')
                elif count == 15104:
                    hello_words3.remove('о')
                elif count == 15108:
                    hello_words3.remove('р')
                elif count == 15112:
                    hello_words3.remove('о')
                elif count == 15116:
                    hello_words3.remove('к')
                elif count == 15120:
                    hello_words3.remove('с')
                elif count == 15124:
                    hello_words2.remove(' ')
                elif count == 15128:
                    hello_words2.remove('я')
                elif count == 15132:
                    hello_words2.remove('л')
                elif count == 15136:
                    hello_words2.remove('д')
                elif count == 15140:
                    hello_words2.remove(' ')
                elif count == 15144:
                    hello_words2.remove('р')
                elif count == 15148:
                    hello_words2.remove('ё')
                elif count == 15152:
                    hello_words2.remove('ж')
                elif count == 15156:
                    hello_words2.remove('а')
                elif count == 15160:
                    hello_words2.remove('н')
                elif count == 15164:
                    hello_words2.remove('е')
                elif count == 15168:
                    hello_words2.remove('р')
                elif count == 15172:
                    hello_words2.remove('т')
                elif count == 15176:
                    hello_words.remove(' ')
                elif count == 15180:
                    hello_words.remove('й')
                elif count == 15184:
                    hello_words.remove('и')
                elif count == 15188:
                    hello_words.remove('к')
                elif count == 15192:
                    hello_words.remove('с')
                elif count == 15196:
                    hello_words.remove('р')
                elif count == 15200:
                    hello_words.remove('е')
                elif count == 15204:
                    hello_words.remove('к')
                elif count == 15208:
                    hello_words.remove('а')
                elif count == 15212:
                    hello_words.remove('х')
                elif count == 15216:
                    hello_words.remove(' ')
                elif count == 15220:
                    hello_words.remove('о')
                elif count == 15224:
                    hello_words.remove('т')
                elif count == 15228:
                    hello_words.remove('э')
        except ValueError:
            pass
        string_rendered = font.render(''.join(hello_words), True, (14, 107, 14))
        string_rendered2 = font.render(''.join(hello_words2), True, (14, 107, 14))
        string_rendered3 = font.render(''.join(hello_words3), True, (14, 107, 14))
        string_rendered4 = font.render(''.join(hello_words4), True, (14, 107, 14))
        screen.blit(string_rendered, (0, 0))
        screen.blit(string_rendered2, (0, 50))
        screen.blit(string_rendered3, (0, 100))
        screen.blit(string_rendered4, (0, 150))
        count += 1
        if count % 40 == 0 and count < 10004:
            if flag:
                hello_words.append(' |')
                flag = False
            else:
                hello_words.remove(' |')
                flag = True
        if ' |' in hello_words and count > 10004:
            hello_words.remove(' |')
            flag = True
        if ' |' in hello_words4 and count > 15228:
            hello_words4.remove(' |')
            flag = True
        elif count % 40 == 0 and count > 10232 and hello_words4:
            if (hello_words4[-1] == 'е' or hello_words4[-1] == ' |'):
                if flag:
                    hello_words4.append(' |')
                    flag = False
                else:
                    hello_words4.remove(' |')
                    flag = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tut = False
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN: 
                if count < 5004:
                    count = 5004
                elif count > 5024 and count < 10004:
                    count = 10000
                elif count > 10232 and count < 15004:
                    count = 15000

        if count > 15228:
            tut = False
            tutorial()
        clock.tick(60)
        pygame.display.flip()


running = True
clip_resized.preview(fps=60)
welcome()
