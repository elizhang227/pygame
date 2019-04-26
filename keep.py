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

def main():
    pygame.init()
    bg = [0, 0, 0] # Green color for canvas
    width = 497
    height = 497 # Size of canvas
    screen = pygame.display.set_mode((width, height)) # sets the screen to the desired size desired on line 6
    pygame.display.set_caption('Will this game work OR NAH')
    
    for row in range(8):
        for column in range(8):
            color = GREEN
            #pygame.draw.circle(screen, color, ((margin + grid_width) * column + margin, (margin + grid_height) * row + margin), 10)
            pygame.draw.rect(screen, color, [(margin + grid_width) * column + margin, (margin + grid_height) * row + margin, grid_width, grid_height])

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
                #### ROW 1 CHECKS ####
                # if pos[0] <= 378 and pos[0] > 315 and pos[1] <= 63:    #[0,5]
                #     pygame.draw.circle(screen, RED, (341,31), 19)
                # if pos[0] <= 441 and pos[0] > 378 and pos[1] <= 63:    #[0,6]
                #     pygame.draw.circle(screen, RED, (403,31), 19)
                # if pos[0] <= 504 and pos[0] > 441 and pos[1] <= 63:    #[0,7]
                #     pygame.draw.circle(screen, RED, (465,31), 19)


                #### COLUMN 1 CHECKS ####
                # if pos[0] <= 63 and pos[1] <= 63:                           #[0,0]
                #     #round it to middle value of that square to use for coordinates                
                #     pygame.draw.circle(screen, RED, (31,31), 19) # POSITION OF DIAGONAL CIRCE ADD 62,62 // HORIZONTAL&VERTICAL ADD 61,61                 
                # if pos[0] < 63 and pos[1] > 63 and pos[1] <= 126:           #[1,0]
                #     pygame.draw.circle(screen, RED, (31,93), 19)
                # if pos[0] < 63 and pos[1] > 126 and pos[1] <= 189:          #[2,0]          
                #     pygame.draw.circle(screen, RED, (31,155), 19)
                # if pos[0] < 63 and pos[1] > 189 and pos[1] <= 252:          #[3,0]
                #     pygame.draw.circle(screen, RED, (31,217), 19)
                # if pos[0] < 63 and pos[1] > 252 and pos[1] <= 315:          #[4,0]
                #     pygame.draw.circle(screen, RED, (31,279), 19)
                # if pos[0] < 63 and pos[1] > 315 and pos[1] <= 378:          #[5,0]
                #     pygame.draw.circle(screen, RED, (31,341), 19)
                # if pos[0] < 63 and pos[1] > 378 and pos[1] <= 441:          #[6,0]
                #     pygame.draw.circle(screen, RED, (31,403), 19)
                # if pos[0] < 63 and pos[1] > 441 and pos[1] <= 504:          #[7,0]
                #     pygame.draw.circle(screen, RED, (31,465), 19)


                #### COLUMN 2 minus 1 CHECKS ####
                # if pos[0] <= 126 and pos[0] > 63 and pos[1] <= 63:                          #[0,1]
                #     pygame.draw.circle(screen, RED, (92,31), 19)                    
                # if pos[0] > 63 and pos[0] <= 126 and pos[1] > 63 and pos[1] <= 126:         #[1,1]
                #     pygame.draw.circle(screen, RED, (93,93), 19)                    
                # if pos[0] > 63 and pos[0] <= 126 and pos[1] > 126 and pos[1] <= 189:        #[2,1]
                #     pygame.draw.circle(screen, RED, (93,155), 19)
                # if pos[0] > 63 and pos[0] <= 126 and pos[1] > 189 and pos[1] <= 252:        #[3,1]
                #     pygame.draw.circle(screen, RED, (93,217), 19)
                # if pos[0] > 63 and pos[0] <= 126 and pos[1] > 252 and pos[1] <= 315:        #[4,1]
                #     pygame.draw.circle(screen, RED, (93,279), 19)
                # if pos[0] > 63 and pos[0] <= 126 and pos[1] > 315 and pos[1] <= 378:        #[5,1]
                #     pygame.draw.circle(screen, RED, (93,341), 19)
                # if pos[0] > 63 and pos[0] <= 126 and pos[1] > 378 and pos[1] <= 441:        #[6,1]
                #     pygame.draw.circle(screen, RED, (93,403), 19)
                # if pos[0] > 63 and pos[0] <= 126 and pos[1] > 441 and pos[1] <= 504:        #[7,1]
                #     pygame.draw.circle(screen, RED, (93,465), 19)


                #### column 3 CHECKS ####
                # if pos[0] <= 189 and pos[0] > 126 and pos[1] <= 63:                             #[0,2]
                #     pygame.draw.circle(screen, RED, (155,31), 19)
                # if pos[0] > 126 and pos[0] <= 189 and pos[1] > 63 and pos[1] <= 126:            #[1,2]
                #     pygame.draw.circle(screen, RED, (155,93), 19)
                # if pos[0] > 126 and pos[0] <= 189 and pos[1] > 126 and pos[1] <= 189:           #[2,2]
                #     pygame.draw.circle(screen, RED, (155,155), 19)                
                # if pos[0] > 126 and pos[0] <= 189 and pos[1] > 189 and pos[1] <= 252:           #[3,2]       
                #     pygame.draw.circle(screen, RED, (155,217), 19)
                # if pos[0] > 126 and pos[0] <= 189 and pos[1] > 252 and pos[1] <= 315:           #[4,2]
                #     pygame.draw.circle(screen, RED, (155,279), 19)
                # if pos[0] > 126 and pos[0] <= 189 and pos[1] > 315 and pos[1] <= 378:           #[5,2]
                #     pygame.draw.circle(screen, RED, (155,341), 19)
                # if pos[0] > 126 and pos[0] <= 189 and pos[1] > 378 and pos[1] <= 441:           #[6,2]
                #     pygame.draw.circle(screen, RED, (155,403), 19)
                # if pos[0] > 126 and pos[0] <= 189 and pos[1] > 441 and pos[1] <= 504:           #[7,2]
                #     pygame.draw.circle(screen, RED, (155,465), 19)


                #### column 4 CHECKS ####
                # if pos[0] <= 252 and pos[0] > 189 and pos[1] <= 63:                             #[0,3]
                #     pygame.draw.circle(screen, RED, (217,31), 19)
                # if pos[0] > 189 and pos[0] <= 252 and pos[1] > 63 and pos[1] <= 126:            #[1,3]
                #     pygame.draw.circle(screen, RED, (217,93), 19)
                # if pos[0] > 189 and pos[0] <= 252 and pos[1] > 126 and pos[1] <= 189:           #[2,3]
                #     pygame.draw.circle(screen, RED, (217,155), 19)                                    
                # if pos[0] > 189 and pos[0] <= 252 and pos[1] > 189 and pos[1] <= 252:           #[3,3]
                #     pygame.draw.circle(screen, RED, (217,217), 19)                
                # if pos[0] > 189 and pos[0] <= 252 and pos[1] > 252 and pos[1] <= 315:           #[4,3]
                #     pygame.draw.circle(screen, RED, (217,279), 19)
                # if pos[0] > 189 and pos[0] <= 252 and pos[1] > 315 and pos[1] <= 378:           #[5,3]
                #     pygame.draw.circle(screen, RED, (217,341), 19)
                # if pos[0] > 189 and pos[0] <= 252 and pos[1] > 378 and pos[1] <= 441:           #[6,3]
                #     pygame.draw.circle(screen, RED, (217,403), 19)
                # if pos[0] > 189 and pos[0] <= 252 and pos[1] > 441 and pos[1] <= 504:           #[7,3]
                #     pygame.draw.circle(screen, RED, (217,465), 19)


                # #### column 5 CHECKS ####
                # if pos[0] <= 315 and pos[0] > 252 and pos[1] <= 63:                           #[0,4]
                #     pygame.draw.circle(screen, RED, (279,31), 19)                
                # if pos[0] > 252 and pos[0] <= 315 and pos[1] > 63 and pos[1] <= 126:          #[1,4]
                #     pygame.draw.circle(screen, RED, (279,93), 19)
                # if pos[0] > 252 and pos[0] <= 315 and pos[1] > 126 and pos[1] <= 189:         #[2,4]
                #     pygame.draw.circle(screen, RED, (279,155), 19)
                # if pos[0] > 252 and pos[0] <= 315 and pos[1] > 189 and pos[1] <= 252:         #[3,4]
                #     pygame.draw.circle(screen, RED, (279,217), 19)                
                # if pos[0] > 252 and pos[0] <= 315 and pos[1] > 252 and pos[1] <= 315:         #[4,4]
                #     pygame.draw.circle(screen, RED, (279,279), 19)                
                # if pos[0] > 252 and pos[0] <= 315 and pos[1] > 315 and pos[1] <= 378:         #[5,4]
                #     pygame.draw.circle(screen, RED, (279,341), 19)
                # if pos[0] > 252 and pos[0] <= 315 and pos[1] > 378 and pos[1] <= 441:         #[6,4]
                #     pygame.draw.circle(screen, RED, (279,403), 19)
                # if pos[0] > 252 and pos[0] <= 315 and pos[1] > 441 and pos[1] <= 504:         #[7,4]
                #     pygame.draw.circle(screen, RED, (279,465), 19)


                # #### column 6 CHECKS ####
                # if pos[0] <= 378 and pos[0] > 315 and pos[1] <= 63:                           #[0,5]
                #     pygame.draw.circle(screen, RED, (341,31), 19)                
                # if pos[0] > 315 and pos[0] <= 378 and pos[1] > 63 and pos[1] <= 126:          #[1,5]
                #     pygame.draw.circle(screen, RED, (341,93), 19)
                # if pos[0] > 315 and pos[0] <= 378 and pos[1] > 126 and pos[1] <= 189:         #[2,5]
                #     pygame.draw.circle(screen, RED, (341,155), 19)
                # if pos[0] > 315 and pos[0] <= 378 and pos[1] > 189 and pos[1] <= 252:         #[3,5]
                #     pygame.draw.circle(screen, RED, (341,217), 19)                
                # if pos[0] > 315 and pos[0] <= 378 and pos[1] > 252 and pos[1] <= 315:         #[4,5]
                #     pygame.draw.circle(screen, RED, (341,279), 19)                
                # if pos[0] > 315 and pos[0] <= 378 and pos[1] > 315 and pos[1] <= 378:         #[5,5]
                #     pygame.draw.circle(screen, RED, (341,341), 20)                
                # if pos[0] > 315 and pos[0] <= 378 and pos[1] > 378 and pos[1] <= 441:         #[6,5]
                #     pygame.draw.circle(screen, RED, (341,403), 19)
                # if pos[0] > 315 and pos[0] <= 378 and pos[1] > 441 and pos[1] <= 504:         #[7,5]
                #     pygame.draw.circle(screen, RED, (341,465), 19)


                # #### column 7 CHECKS ####
                # if pos[0] <= 441 and pos[0] > 378 and pos[1] <= 63:                           #[0,6]
                #     pygame.draw.circle(screen, RED, (403,31), 19)                
                # if pos[0] > 378 and pos[0] <= 441 and pos[1] > 63 and pos[1] <= 126:          #[1,6]
                #     pygame.draw.circle(screen, RED, (403,93), 19)
                # if pos[0] > 378 and pos[0] <= 441 and pos[1] > 126 and pos[1] <= 189:         #[2,6]
                #     pygame.draw.circle(screen, RED, (403,155), 19)
                # if pos[0] > 378 and pos[0] <= 441 and pos[1] > 189 and pos[1] <= 252:         #[3,6]
                #     pygame.draw.circle(screen, RED, (403,217), 19)                
                # if pos[0] > 378 and pos[0] <= 441 and pos[1] > 252 and pos[1] <= 315:         #[4,6]
                #     pygame.draw.circle(screen, RED, (403,279), 19)                
                # if pos[0] > 378 and pos[0] <= 441 and pos[1] > 315 and pos[1] <= 378:         #[5,6]
                #     pygame.draw.circle(screen, RED, (403,341), 20)                
                # if pos[0] > 378 and pos[0] <= 441 and pos[1] > 378 and pos[1] <= 441:         #[6,6]
                #     pygame.draw.circle(screen, RED, (403,403), 19)
                # if pos[0] > 378 and pos[0] <= 441 and pos[1] > 441 and pos[1] <= 504:         #[7,6]
                #     pygame.draw.circle(screen, RED, (403,465), 19)


                #### column 8 CHECKS ####
                if pos[0] <= 504 and pos[0] > 441 and pos[1] <= 63:                           #[0,7]
                    pygame.draw.circle(screen, RED, (465,31), 19)                
                if pos[0] > 441 and pos[0] <= 504 and pos[1] > 63 and pos[1] <= 126:          #[1,7]
                    pygame.draw.circle(screen, RED, (465,93), 19)
                if pos[0] > 441 and pos[0] <= 504 and pos[1] > 126 and pos[1] <= 189:         #[2,7]
                    pygame.draw.circle(screen, RED, (465,155), 19)
                if pos[0] > 441 and pos[0] <= 504 and pos[1] > 189 and pos[1] <= 252:         #[3,7]
                    pygame.draw.circle(screen, RED, (465,217), 19)                
                if pos[0] > 441 and pos[0] <= 504 and pos[1] > 252 and pos[1] <= 315:         #[4,7]
                    pygame.draw.circle(screen, RED, (465,279), 19)                
                if pos[0] > 441 and pos[0] <= 504 and pos[1] > 315 and pos[1] <= 378:         #[5,7]
                    pygame.draw.circle(screen, RED, (465,341), 19)                
                if pos[0] > 441 and pos[0] <= 504 and pos[1] > 378 and pos[1] <= 441:         #[6,7]
                    pygame.draw.circle(screen, RED, (465,403), 19)
                if pos[0] > 441 and pos[0] <= 504 and pos[1] > 441 and pos[1] <= 504:         #[7,7]
                    pygame.draw.circle(screen, RED, (465,465), 19)



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