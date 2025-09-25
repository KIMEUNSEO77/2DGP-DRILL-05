from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

w = 100
h = 100
idle = ((0, 300, w, h), (0, 200, w, h))   # 오른쪽, 왼쪽
idle_right = False
x, y = 600, 500   # 처음 위치는 600, 500

def handle_events():
    global running, idle_right
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT:
                pass
            elif event.key == SDLK_LEFT:
                pass
            elif event.key == SDLK_UP:
                pass
            elif event.key == SDLK_DOWN:
                pass
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                idle_right = True
            elif event.key == SDLK_LEFT:
                pass
            elif event.key == SDLK_UP:
                pass
            elif event.key == SDLK_DOWN:
                pass

running = True

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    if idle_right:
        sx, sy, sw, sh = idle[0]
        character.clip_draw(sx, sy, sw, sh, x, y)

    update_canvas()
    handle_events()
close_canvas()