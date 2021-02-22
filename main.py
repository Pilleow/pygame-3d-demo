import pygame
import engine as e

pygame.init()

RES = [1920, 1080]
engine = e.Engine(RES)
clock = pygame.time.Clock()
display = pygame.display.set_mode(RES)

scroll = [0, 0]

# hardcoded boxes because yes
engine.add_box(e.Box([50, 70, 90, 120], 40, [50, 70, 90], [80, 100, 120]))
engine.add_box(e.Box([600, 240, 70, 50], 100, [69, 245, 66], [99, 255, 96]))
engine.add_box(e.Box([140, 90, 150, 70], 75, [245, 239, 66], [255, 255, 96]))
engine.add_box(e.Box([806, 600, 100, 60], 90, [245, 69, 66], [255, 99, 96]))
engine.add_box(e.Box([1010, 50, 150, 70], 60, [150, 66, 245], [180, 96, 255]))
engine.add_box(e.Box([RES[0]//2-25, RES[1]//2-25, 50, 50], 20, [66, 245, 173], [96, 255, 203]))

def render(surface):
    surface.fill((10, 10, 10))
    engine.run_cycle(surface, scroll)
    pygame.display.update()

''' --- MAINLOOP --- '''
run = True
while run:
    clock.tick(9000)
    print(clock.get_fps())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
    
    # camera movement (arrows, hold LShift to move half as slow)
    keys = pygame.key.get_pressed()
    velocity = 6
    if keys[pygame.K_LSHIFT]:
        velocity /= 2
    if keys[pygame.K_UP]:
        scroll[1] -= velocity
    if keys[pygame.K_DOWN]:
        scroll[1] += velocity
    if keys[pygame.K_RIGHT]:
        scroll[0] += velocity
    if keys[pygame.K_LEFT]:
        scroll[0] -= velocity

    render(display)

pygame.quit()
