import pygame



# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Delta Legends")
clock = pygame.time.Clock()
running = True

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0 
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
    
    def move(self, dx, dy):
        self.rect.x += dx 
        self.rect.y += dy 

    def move_left(self, vel):
        self.x_vel = vel 
        if self.direction != 'left':
            self.direction = 'left'
            self.animation_count = 0 

    
    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != 'right':
            self.direction = 'right'
            self.animation_count = 0

    def loop(self, fps):
        self.move(self.x_vel, self.y_vel)
    

def main(window):

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill((135, 206, 235))

        # RENDER YOUR GAME HERE
        draw_text("Press SPACE to pause", font, TEXT_COL, 640, 360)    

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
    quit()
