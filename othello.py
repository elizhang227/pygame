import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 100, 0)
RED = (255, 0, 0)

grid_width = 62   # for making individual grids on the screen
grid_height = 62
margin = 1

class Piece:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 20 # will be a circle    

class White(Piece):
    def render(self, screen):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius)

class Black(Piece):
    def render(self, screen):
        pygame.draw.circle(screen, BLACK, (self.x, self.y), self.radius)

grid = []
for row in range(10):
    grid.append([])
    for column in range(10):
        grid[row].append(0)

def main():
    pygame.init()
    bg = [0, 0, 0] # Green color for canvas
    width = 505
    height = 505 # Size of canvas
    screen = pygame.display.set_mode((width, height)) # sets the screen to the desired size desired on line 6
    pygame.display.set_caption('My Game')

    #Game initilization
    white_pieces_count = [   #list for white pieces
        # Initial 2 white pieces (need to find out how to center)
        White(220, 220),
        White(284, 282) 
    ]
    black_pieces_count = [   #list for black pieces
        # Initial 2 black pieces (need to center)
        Black(284, 220),
        Black(222, 284)
    ]

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_game = True

            if event.type == pygame.MOUSEBUTTONDOWN: #places a white piece at the location of mouse click
                x, y = event.pos
                print(x, y) # finding position 
                white_pieces_count.append(White(x, y))            

        screen.fill(bg) # calls fill method on the screen that fills in with the bg color we set on line 5

        for row in range(8):
            for column in range(8):
                color = GREEN
                if grid[row][column] == 1:
                    color = WHITE
                pygame.draw.rect(screen,
                                color,
                                [(margin + grid_width) * column + margin,
                                (margin + grid_height) * row + margin,
                                grid_width,
                                grid_height])

        for piece in white_pieces_count: # has to be called after screen.fill(bg) line 51 because it runs top to bottom and if you render ball first then fill the screen the screen will be on top
            piece.render(screen)
        for piece in black_pieces_count:
            piece.render(screen)
        # instructions to play the game line 56-58
        font = pygame.font.Font(None, 25)
        text = font.render('Click an empty square to place your piece down', True, (0, 0, 0))
        screen.blit(text, (80, 230))        

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()