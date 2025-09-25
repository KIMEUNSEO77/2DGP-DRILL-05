from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

w = 100
h = 100
idle = (0, 300, w, h)

def handle_events():
    global running
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
                pass
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
    update_canvas()

close_canvas()