import pygame

WIDTH = 500
HEIGHT = 500
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
hero = pygame.image.load('razorinv.png')

hero_hp = 100
x_hero = WIDTH // 2 - 10
y_hero = HEIGHT // 2 - 10

moving = '' # НЕ ЗАБЫТЬ!!!!
is_shot = False
bullets = []
bullets_coord = []

running = True
while running:
    screen.fill(BLACK)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                moving = 'UP'
            elif event.key == pygame.K_DOWN:
                moving = 'DOWN'
            elif event.key == pygame.K_LEFT:
                moving = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                moving = 'RIGHT'
            elif event.key == pygame.K_SPACE:
                is_shot = True
        elif event.type == pygame.KEYUP:
            if (event.key == pygame.K_UP or
            event.key == pygame.K_DOWN or
            event.key == pygame.K_LEFT or
            event.key == pygame.K_RIGHT):
                moving = 'STOP'
    
    # движение пули
    if is_shot:
        bullets.append(pygame.image.load('bullet.png'))
        bullets_coord.append((x_bul, y_bul))
        is_shot = False
    
    # отрисовка каждой пули на экране
    sch = 0
    for bullet in bullets:
        coords = bullets_coord[sch]
        x_b = coords[0]
        y_b = coords[1]
        screen.blit(bullet, (x_b, y_b))
        cords = (x_b, y_b - 5)
        bullets_coord[sch] = cords
        sch += 1
            
    # сделать удаление пули при достижение конца экрана!!!
    
            
    screen.blit(hero, (x_hero, y_hero))
    if moving == 'UP':
        y_hero -= 5
    elif moving == 'DOWN':
        y_hero += 5
    elif moving == 'LEFT':
        x_hero -= 5
    elif moving == 'RIGHT':
        x_hero += 5
    
    surf = hero.get_rect()
    x_bul = x_hero + (surf.width // 2)
    y_bul = y_hero
        
    pygame.display.update()
    clock.tick(FPS)
    
    
    
    
    
    
