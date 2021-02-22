import pygame
import random
import engine as e

from perlin_noise import PerlinNoise

pygame.init()

RES = [1280, 720]
engine = e.Engine(RES)
clock = pygame.time.Clock()
display = pygame.display.set_mode(RES)

time = 0
scroll = [0, 0]
colors = [[54, 52, 51], [219, 49, 22]]
noise = PerlinNoise(3)

# box generation
for y in range(5):
    for x in range(7):
        color = random.choice(colors)
        side_color = [x-12 for x in color]
        engine.add_box(e.Box(
                pygame.Rect(x*150, y*100, 125, 75), 
                random.choice(range(10, 50, 4)), 
                color,
                side_color
        ))

def render(surface):
    surface.fill((10, 8, 9))
    engine.run_cycle(surface, scroll)
    pygame.display.update()

''' --- MAINLOOP --- '''
run = True
while run:
    clock.tick(9000)

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

    for i, box in enumerate(engine.box_list):
        value = noise([(time + 2*i)/221, i/221]) * 5
        if 0 >= box.width + value or 70 <= box.width + value:
            value = 0
        box.width += value
    time += 1

    render(display)

pygame.quit()
