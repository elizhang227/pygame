import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 100, 0)
RED = (255, 0, 0)

grid_width = 61   # for making individual grids on the screen
grid_height = 61
margin = 1
radius = 5

class Piece:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 20 # will be a circle    

class White(Piece):
    pass

class Black(Piece):
    pass

screen = pygame.display.set_mode((497,497))

grid = []
# creates 8 empty rows and appends them to the grid
for row in range(8):
    grid.append([])
    #creates 8 items in the rows and intializes the value at 0
    for column in range(8):
        grid[row].append(0)

def create_grid():
    for row in range(8): 
        for column in range(8):
            color = GREEN
            pygame.draw.rect(screen, color, [(margin + grid_width) * column + margin, (margin + grid_height) * row + margin, grid_width, grid_height])

def initial_board():
    pygame.draw.circle(screen, BLACK, (217,217), 19)        #[3,3]            
    pygame.draw.circle(screen, WHITE, (217,279), 19)        #[4,3]
    pygame.draw.circle(screen, WHITE, (279,217), 19)        #[3,4]                
    pygame.draw.circle(screen, BLACK, (279,279), 19)        #[4,4] 

def valid_moves():
    pass

def place_piece():
    color = BLACK
    # grid[row][column] = 1
    stop_game = False   

    while not stop_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_game = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                #### User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                #### Change the x/y screen coordinates to grid coordinates:
                #### takes the x value of the mouse click and divides by (grid_width + margin is the total space of a singular box that we created)
                #### // operator rounds the result to the nearest integer *DOWN*
                column = pos[0] // (grid_width + margin) # for 0,0 rectangle if pos[0] (x value) doesn't exceed the total of grid_width + margin then it will always return 0 which is used to indicate what column its in
                row = pos[1] // (grid_height + margin) # for 0,0 rectangle if pos[1] (y value) doesnt exceed total of grid_height + margin then it will return 0 used to indicate what row it is in
                grid[row][column] += 1
                #### Set that location to one
                print("Click ", pos, "Grid coordinates: ", row, column)

                ### COLUMN 1 CHECKS ####
                #if grid[row][column] == 1:
                    
                if pos[0] <= 63 and pos[1] <= 63:                           #[0,0]
                    #round it to middle value of that square to use for coordinates                
                    pygame.draw.circle(screen, color, (31,31), 19) # POSITION OF DIAGONAL CIRCE ADD 62,62 // HORIZONTAL&VERTICAL ADD 61,61                 
                if pos[0] < 63 and pos[1] > 63 and pos[1] <= 126:           #[1,0]
                    pygame.draw.circle(screen, color, (31,93), 19)
                if pos[0] < 63 and pos[1] > 126 and pos[1] <= 189:          #[2,0]          
                    pygame.draw.circle(screen, color, (31,155), 19)
                if pos[0] < 63 and pos[1] > 189 and pos[1] <= 252:          #[3,0]
                    pygame.draw.circle(screen, color, (31,217), 19)
                if pos[0] < 63 and pos[1] > 252 and pos[1] <= 315:          #[4,0]
                    pygame.draw.circle(screen, color, (31,279), 19)
                if pos[0] < 63 and pos[1] > 315 and pos[1] <= 378:          #[5,0]
                    pygame.draw.circle(screen, color, (31,341), 19)
                if pos[0] < 63 and pos[1] > 378 and pos[1] <= 441:          #[6,0]
                    pygame.draw.circle(screen, color, (31,403), 19)
                if pos[0] < 63 and pos[1] > 441 and pos[1] <= 504:          #[7,0]
                    pygame.draw.circle(screen, color, (31,465), 19)


                ### COLUMN 2 minus 1 CHECKS ####
                if pos[0] <= 126 and pos[0] > 63 and pos[1] <= 63:                          #[0,1]
                    pygame.draw.circle(screen, color, (92,31), 19)                    
                if pos[0] > 63 and pos[0] <= 126 and pos[1] > 63 and pos[1] <= 126:         #[1,1]
                    pygame.draw.circle(screen, color, (93,93), 19)                    
                if pos[0] > 63 and pos[0] <= 126 and pos[1] > 126 and pos[1] <= 189:        #[2,1]
                    pygame.draw.circle(screen, color, (93,155), 19)
                if pos[0] > 63 and pos[0] <= 126 and pos[1] > 189 and pos[1] <= 252:        #[3,1]
                    pygame.draw.circle(screen, color, (93,217), 19)
                if pos[0] > 63 and pos[0] <= 126 and pos[1] > 252 and pos[1] <= 315:        #[4,1]
                    pygame.draw.circle(screen, color, (93,279), 19)
                if pos[0] > 63 and pos[0] <= 126 and pos[1] > 315 and pos[1] <= 378:        #[5,1]
                    pygame.draw.circle(screen, color, (93,341), 19)
                if pos[0] > 63 and pos[0] <= 126 and pos[1] > 378 and pos[1] <= 441:        #[6,1]
                    pygame.draw.circle(screen, color, (93,403), 19)
                if pos[0] > 63 and pos[0] <= 126 and pos[1] > 441 and pos[1] <= 504:        #[7,1]
                    pygame.draw.circle(screen, color, (93,465), 19)


                ### column 3 CHECKS ####
                if pos[0] <= 189 and pos[0] > 126 and pos[1] <= 63:                             #[0,2]
                    pygame.draw.circle(screen, color, (155,31), 19)
                if pos[0] > 126 and pos[0] <= 189 and pos[1] > 63 and pos[1] <= 126:            #[1,2]
                    pygame.draw.circle(screen, color, (155,93), 19)
                if pos[0] > 126 and pos[0] <= 189 and pos[1] > 126 and pos[1] <= 189:           #[2,2]
                    pygame.draw.circle(screen, color, (155,155), 19)                
                if pos[0] > 126 and pos[0] <= 189 and pos[1] > 189 and pos[1] <= 252:           #[3,2]       
                    pygame.draw.circle(screen, color, (155,217), 19)
                    pygame.draw.circle(screen, color, (217,217), 19)
                if pos[0] > 126 and pos[0] <= 189 and pos[1] > 252 and pos[1] <= 315:           #[4,2]
                    pygame.draw.circle(screen, color, (155,279), 19)
                    pygame.draw.circle(screen, color, (217,279), 19)
                if pos[0] > 126 and pos[0] <= 189 and pos[1] > 315 and pos[1] <= 378:           #[5,2]
                    pygame.draw.circle(screen, color, (155,341), 19)
                if pos[0] > 126 and pos[0] <= 189 and pos[1] > 378 and pos[1] <= 441:           #[6,2]
                    pygame.draw.circle(screen, color, (155,403), 19)
                if pos[0] > 126 and pos[0] <= 189 and pos[1] > 441 and pos[1] <= 504:           #[7,2]
                    pygame.draw.circle(screen, color, (155,465), 19)


                ### column 4 CHECKS ####
                if pos[0] <= 252 and pos[0] > 189 and pos[1] <= 63:                             #[0,3]
                    pygame.draw.circle(screen, color, (217,31), 19)
                if pos[0] > 189 and pos[0] <= 252 and pos[1] > 63 and pos[1] <= 126:            #[1,3]
                    pygame.draw.circle(screen, color, (217,93), 19)
                if pos[0] > 189 and pos[0] <= 252 and pos[1] > 126 and pos[1] <= 189:           #[2,3]
                    pygame.draw.circle(screen, color, (217,155), 19)
                    pygame.draw.circle(screen, color, (217,217), 19)                                    
                #if pos[0] > 189 and pos[0] <= 252 and pos[1] > 189 and pos[1] <= 252:           #[3,3] initial
                    #pygame.draw.circle(screen, color, (217,217), 19)                
                #if pos[0] > 189 and pos[0] <= 252 and pos[1] > 252 and pos[1] <= 315:           #[4,3] initial
                    #pygame.draw.circle(screen, color, (217,279), 19)
                if pos[0] > 189 and pos[0] <= 252 and pos[1] > 315 and pos[1] <= 378:           #[5,3]
                    pygame.draw.circle(screen, color, (217,341), 19)
                    pygame.draw.circle(screen, color, (217,279), 19)
                if pos[0] > 189 and pos[0] <= 252 and pos[1] > 378 and pos[1] <= 441:           #[6,3]
                    pygame.draw.circle(screen, color, (217,403), 19)
                if pos[0] > 189 and pos[0] <= 252 and pos[1] > 441 and pos[1] <= 504:           #[7,3]
                    pygame.draw.circle(screen, color, (217,465), 19)


                #### column 5 CHECKS ####
                if pos[0] <= 315 and pos[0] > 252 and pos[1] <= 63:                           #[0,4]
                    pygame.draw.circle(screen, color, (279,31), 19)                
                if pos[0] > 252 and pos[0] <= 315 and pos[1] > 63 and pos[1] <= 126:          #[1,4]
                    pygame.draw.circle(screen, color, (279,93), 19)
                    pygame.draw.circle(screen, color, (279,155), 19)
                    pygame.draw.circle(screen, color, (279,217), 19)
                    pygame.draw.circle(screen, color, (279,279), 19)
                if pos[0] > 252 and pos[0] <= 315 and pos[1] > 126 and pos[1] <= 189:         #[2,4]
                    pygame.draw.circle(screen, color, (279,155), 19)
                    pygame.draw.circle(screen, color, (279,217), 19)  
                #if pos[0] > 252 and pos[0] <= 315 and pos[1] > 189 and pos[1] <= 252:         #[3,4] initial
                    #pygame.draw.circle(screen, color, (279,217), 19)                
                #if pos[0] > 252 and pos[0] <= 315 and pos[1] > 252 and pos[1] <= 315:         #[4,4] initial
                    #pygame.draw.circle(screen, color, (279,279), 19)                
                if pos[0] > 252 and pos[0] <= 315 and pos[1] > 315 and pos[1] <= 378:         #[5,4]
                    pygame.draw.circle(screen, color, (279,341), 19)
                    pygame.draw.circle(screen, color, (279,279), 19)
                if pos[0] > 252 and pos[0] <= 315 and pos[1] > 378 and pos[1] <= 441:         #[6,4]
                    pygame.draw.circle(screen, color, (279,403), 19)
                if pos[0] > 252 and pos[0] <= 315 and pos[1] > 441 and pos[1] <= 504:         #[7,4]
                    pygame.draw.circle(screen, color, (279,465), 19)


                #### column 6 CHECKS ####
                if pos[0] <= 378 and pos[0] > 315 and pos[1] <= 63:                           #[0,5]
                    pygame.draw.circle(screen, color, (341,31), 19)                
                if pos[0] > 315 and pos[0] <= 378 and pos[1] > 63 and pos[1] <= 126:          #[1,5]
                    pygame.draw.circle(screen, color, (341,93), 19)
                if pos[0] > 315 and pos[0] <= 378 and pos[1] > 126 and pos[1] <= 189:         #[2,5]
                    pygame.draw.circle(screen, color, (341,155), 19)
                if pos[0] > 315 and pos[0] <= 378 and pos[1] > 189 and pos[1] <= 252:         #[3,5]
                    pygame.draw.circle(screen, color, (341,217), 19)
                    pygame.draw.circle(screen, color, (279,217), 19)                
                if pos[0] > 315 and pos[0] <= 378 and pos[1] > 252 and pos[1] <= 315:         #[4,5]
                    pygame.draw.circle(screen, color, (341,279), 19)
                    pygame.draw.circle(screen, color, (279,279), 19)                
                if pos[0] > 315 and pos[0] <= 378 and pos[1] > 315 and pos[1] <= 378:         #[5,5]
                    pygame.draw.circle(screen, color, (341,341), 20)                
                if pos[0] > 315 and pos[0] <= 378 and pos[1] > 378 and pos[1] <= 441:         #[6,5]
                    pygame.draw.circle(screen, color, (341,403), 19)
                if pos[0] > 315 and pos[0] <= 378 and pos[1] > 441 and pos[1] <= 504:         #[7,5]
                    pygame.draw.circle(screen, color, (341,465), 19)


                #### column 7 CHECKS ####
                if pos[0] <= 441 and pos[0] > 378 and pos[1] <= 63:                           #[0,6]
                    pygame.draw.circle(screen, color, (403,31), 19)                
                if pos[0] > 378 and pos[0] <= 441 and pos[1] > 63 and pos[1] <= 126:          #[1,6]
                    pygame.draw.circle(screen, color, (403,93), 19)
                if pos[0] > 378 and pos[0] <= 441 and pos[1] > 126 and pos[1] <= 189:         #[2,6]
                    pygame.draw.circle(screen, color, (403,155), 19)
                if pos[0] > 378 and pos[0] <= 441 and pos[1] > 189 and pos[1] <= 252:         #[3,6]
                    pygame.draw.circle(screen, color, (403,217), 19)                
                if pos[0] > 378 and pos[0] <= 441 and pos[1] > 252 and pos[1] <= 315:         #[4,6]
                    pygame.draw.circle(screen, color, (403,279), 19)                
                if pos[0] > 378 and pos[0] <= 441 and pos[1] > 315 and pos[1] <= 378:         #[5,6]
                    pygame.draw.circle(screen, color, (403,341), 20)                
                if pos[0] > 378 and pos[0] <= 441 and pos[1] > 378 and pos[1] <= 441:         #[6,6]
                    pygame.draw.circle(screen, color, (403,403), 19)
                if pos[0] > 378 and pos[0] <= 441 and pos[1] > 441 and pos[1] <= 504:         #[7,6]
                    pygame.draw.circle(screen, color, (403,465), 19)


                #### column 8 CHECKS ####
                if pos[0] <= 504 and pos[0] > 441 and pos[1] <= 63:                           #[0,7]
                    pygame.draw.circle(screen, color, (465,31), 19)                
                if pos[0] > 441 and pos[0] <= 504 and pos[1] > 63 and pos[1] <= 126:          #[1,7]
                    pygame.draw.circle(screen, color, (465,93), 19)
                if pos[0] > 441 and pos[0] <= 504 and pos[1] > 126 and pos[1] <= 189:         #[2,7]
                    pygame.draw.circle(screen, color, (465,155), 19)
                if pos[0] > 441 and pos[0] <= 504 and pos[1] > 189 and pos[1] <= 252:         #[3,7]
                    pygame.draw.circle(screen, color, (465,217), 19)                
                if pos[0] > 441 and pos[0] <= 504 and pos[1] > 252 and pos[1] <= 315:         #[4,7]
                    pygame.draw.circle(screen, color, (465,279), 19)                
                if pos[0] > 441 and pos[0] <= 504 and pos[1] > 315 and pos[1] <= 378:         #[5,7]
                    pygame.draw.circle(screen, color, (465,341), 19)                
                if pos[0] > 441 and pos[0] <= 504 and pos[1] > 378 and pos[1] <= 441:         #[6,7]
                    pygame.draw.circle(screen, color, (465,403), 19)
                if pos[0] > 441 and pos[0] <= 504 and pos[1] > 441 and pos[1] <= 504:         #[7,7]
                    pygame.draw.circle(screen, color, (465,465), 19)

                if color == BLACK:
                    color = WHITE
                elif color == WHITE:
                    color = BLACK

                print('Next piece will be %s' % str(color))

        pygame.display.update()

def main():
    pygame.init()
    pygame.display.set_caption('Will this game work OR NAH')

    create_grid()
    initial_board()
    place_piece()
 
    pygame.quit()

if __name__ == '__main__':
    main()