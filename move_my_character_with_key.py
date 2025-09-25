from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

w = 100
h = 100
idle = ((0, 300, w, h), (0, 200, w, h))   # 오른쪽, 왼쪽
idle_right = False
idle_left = False
x, y = 600, 500   # 처음 위치는 600, 500
dirIdx = -1   # 0: 오른쪽, 1: 왼쪽, 2: 위쪽, 3: 아래쪽

def handle_events():
    global running, idle_right, idle_left, dirIdx
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT:
                dirIdx = 0
            elif event.key == SDLK_LEFT:
                dirIdx = 1
            elif event.key == SDLK_UP:
                dirIdx = 2
            elif event.key == SDLK_DOWN:
                dirIdx = 3
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirIdx = -1
                idle_left = False
                idle_right = True
            elif event.key == SDLK_LEFT:
                dirIdx = -1
                idle_right = False
                idle_left = True
            elif event.key == SDLK_UP:
                pass
            elif event.key == SDLK_DOWN:
                pass
def pickDir():
    global dirIdx
    if (dirIdx == -1): return

    global dx, dy
    if dirIdx == 0:
        dx = 1
        dy = 0
    elif dirIdx == 1:
        dx = -1
        dy = 0
    elif dirIdx == 2:
        dx = 0
        dy = -1
    elif dirIdx == 3:
        dx = 0
        dy = 1

running = True
dx, dy = 0, 0   # 이동 x, y

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    pickDir()

    x += dx
    y += dy

    if idle_right:
        sx, sy, sw, sh = idle[0]
        character.clip_draw(sx, sy, sw, sh, x, y)
    elif idle_left:
        sx, sy, sw, sh = idle[1]
        character.clip_draw(sx, sy, sw, sh, x, y)
    else:
        character.clip_draw(0, 100, w, h, x, y)

    update_canvas()
    handle_events()
close_canvas()