import pygame

SCREEN = WIDTH, HEIGHT = 300, 300
CELLSIZE = 20
PADDING = 20
ROWS = COLS = (WIDTH - 4*PADDING) // CELLSIZE
print(ROWS, COLS)

pygame.init()
pygame.display.set_caption(title='DOTS & BOXES BY OR')
win = pygame.display.set_mode(SCREEN)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

'''
    We will define cell as a rectangle
    There are 4 options in total for an edge
'''
class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.index = self.row * ROWS + self.col * COLS
        self.rectangle= pygame.Rect((self.col*CELLSIZE + 2*PADDING, self.row*CELLSIZE + 3*PADDING, CELLSIZE, CELLSIZE))
        self.left = self.rectangle.left
        self.top = self.rectangle.top
        self.right = self.rectangle.right
        self.bottom = self.rectangle.bottom
        self.edgeOptions = [
             [(self.left, self.top), (self.right, self.top)],
             [(self.right, self.top), (self.right, self.bottom)],
             [(self.right, self.bottom), (self.left, self.bottom)],
             [(self.left, self.bottom), (self.left, self.top)]
             ]

        self.currentEdges = [False, False, False, False]
        self.winner = None
    
    def checkWinner(self):
        if not self.winner:
            if self.currentEdges == [True] * 4:
                self.winner = True


    def update(self, win):
        if self.winner:
            pygame.draw.rect(win, RED, self.rectangle)
        for index, edge in enumerate(self.currentEdges):
            if edge:
                # TODO : CHANGE THE COLOR OF LINE DEPENDS ON WHICH PLAYER IS PLAYING
                pygame.draw.line(win, BLACK, (self.edgeOptions[index][0]), self.edgeOptions[index][1], 2) 


cells = []
for row in range(ROWS):
    for col in range(COLS):
        cell = Cell(row, col)
        cells.append(cell)

position = None
current_cell = None
up = False
right = False
down = False
left = False


running = True # infinite loop 
while running:
    win.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        match (event.type):
            case pygame.MOUSEBUTTONDOWN:
                position = event.pos
            case pygame.MOUSEBUTTONUP:
                position = None
            case pygame.KEYDOWN: # Click
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    up = True
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    right = True
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    down = True
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    left = True
            case pygame.KEYUP: # Unclick
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    up = False
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    right = False
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    down = False
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    left = False
            case _:
                pass
    # Drawing dots inside the window
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.circle(win, BLACK, (col*CELLSIZE + 2*PADDING, row*CELLSIZE + 3*PADDING), 4)
    

    for cell in cells:
        cell.update(win)
        if position and cell.rectangle.collidepoint(position):
            current_cell = cell
    
    if current_cell:
        index = current_cell.index
        pygame.draw.circle(win, RED, (current_cell.rectangle.centerx, current_cell.rectangle.centery), 2)

        if up: # Create edge in top side of square
            current_cell.currentEdges[0] = True
            if index - ROWS >= 0:
                cells[index - ROWS].currentEdges[2] = True 

        if right: # Create edge in right side of square
            current_cell.currentEdges[1] = True
            if (index+1) % COLS > 0:
                cells[index+1].currentEdges[3] = True

        if down: # Create edge in bottom side of square
            current_cell.currentEdges[2] = True 
            if (index + ROWS) < len(cells):
                cells[index + ROWS].currentEdges[0] = True
                
        if left: # Create edge in left side of square
            current_cell.currentEdges[3] = True 
            if index % COLS > 0:
                cells[index-1].currentEdges[1] = True

        current_cell.checkWinner()
    pygame.display.update()

pygame.quit()