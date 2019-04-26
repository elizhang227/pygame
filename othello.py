import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 100, 0)
RED = (255, 0, 0)

grid_width = 62   # for making individual grids on the screen
grid_height = 62
margin = 1
radius = 5

class Piece:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 20 # will be a circle    

class White(Piece):
    pass
    # def render(self, screen):
    #     pygame.draw.circle(screen, BLACK, (self.x, self.y), self.radius)

class Black(Piece):
    pass
    # def render(self, screen):
    #     pygame.draw.circle(screen, BLACK, (self.x, self.y), self.radius)


grid = []
# creates 8 empty rows and appends them to the grid
for row in range(8):
    grid.append([])
    #creates 8 items in the rows and intializes the value at 0
    for column in range(8):
        grid[row].append(0)

# grid[3][4] = RED
# grid[4][3] = RED
# grid[3][3] = WHITE
# grid[4][4] = WHITE

def main():
    pygame.init()
    bg = [0, 0, 0] # Green color for canvas
    width = 505
    height = 505 # Size of canvas
    screen = pygame.display.set_mode((width, height)) # sets the screen to the desired size desired on line 6
    pygame.display.set_caption('Will this game work OR NAH')
    
    """
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
    """

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_game = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                #### User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # print(pos[0]) # prints out index 0 of the tuple of the coordinates which is the x value
                # print(pos[1]) # prints out index 1 of the tuple of the coordinates which is the y value
                #### Change the x/y screen coordinates to grid coordinates:
                #### takes the x value of the mouse click and divides by (grid_width + margin is the total space of a singular box that we created)
                #### // operator rounds the result to the nearest integer *DOWN*
                column = pos[0] // (grid_width + margin) # for 0,0 rectangle if pos[0] (x value) doesn't exceed the total of grid_width + margin then it will always return 0 which is used to indicate what column its in
                row = pos[1] // (grid_height + margin) # for 0,0 rectangle if pos[1] (y value) doesnt exceed total of grid_height + margin then it will return 0 used to indicate what row it is in
                #### Set that location to one
                grid[row][column] = 1 #### uses the location we now know to set the value of that spot in the matrix to 1 indicating a change
                print("Click ", pos, "Grid coordinates: ", row, column)
                #pygame.draw.circle(screen, WHITE, pos, 10)
                for row in range(8):
                    for column in range(8):
                        color = GREEN
                        #pygame.draw.rect(screen, color, [(margin + grid_width) * column + margin, (margin + grid_height) * row + margin, grid_width, grid_height])
                        if grid[row][column] == 1: ## once the user clicks the box the value of that in the matrix turns into 1 which makes it true and changes
                            pygame.draw.circle(screen, color, pos, 20)       

        #screen.fill(bg) # calls fill method on the screen that fills in with the bg color we set on line 5
        #### THIS DRAWS UR GREEN RECTANGLES AND CREATES THE GRID ###
        # for row in range(8):
        #     for column in range(8):
        #         color = GREEN
        #         #pygame.draw.rect(screen, color, [(margin + grid_width) * column + margin, (margin + grid_height) * row + margin, grid_width, grid_height])
        #         if grid[row][column] == 1: ## once the user clicks the box the value of that in the matrix turns into 1 which makes it true and changes
        #             pygame.draw.circle(screen, color, (50,50), 20)
                    #color = BLACK          ## color to black
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     pos = pygame.mouse.get_pos()
        #     pygame.draw.circle(screen, RED, pos, 20)                
                #pygame.draw.rect(screen, color, [(margin + grid_width) * column + margin, (margin + grid_height) * row + margin, grid_width, grid_height])

        # for row in range(8):
        #     for column in range(8):
        #         color = GREEN
        #         #if grid[row][column] == 1: ## once the user clicks the box the value of that in the matrix turns into 1 which makes it true and changes
        #         #    color = BLACK          ## color to black                
        #         pygame.draw.rect(screen, color, [(margin + grid_width) * column + margin, (margin + grid_height) * row + margin, grid_width, grid_height])              

        # for piece in white_pieces_count: # has to be called after screen.fill(bg) line 51 because it runs top to bottom and if you render ball first then fill the screen the screen will be on top
        #     piece.render(screen)
        # for piece in black_pieces_count:
        #     piece.render(screen)
        #### instructions to play the game line 56-58
        # font = pygame.font.Font(None, 25)
        # text = font.render('Click an empty square to place your piece down', True, (0, 0, 0))
        # screen.blit(text, (80, 230))   

        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    main()