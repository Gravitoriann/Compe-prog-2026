import pygame
from Bloc_C.game_logic import Board
from Bloc_C.game_logic import Coord
from Bloc_C.game_logic import Crab

TILE_SIZE = 100
BORDER_SIZE = 2
MS_WAIT_BETWEEN_MOVES = 500

def init_pygame(board, name="CRAB ESCAPE"):
    pygame.init()
    width = board.cols * TILE_SIZE
    height = board.rows * TILE_SIZE
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(name)
    return screen

def get_tile_rect(coord: Coord):
    x = coord.x * TILE_SIZE
    y = coord.y * TILE_SIZE

    return pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)

def draw_board(screen, board: Board):
    for y in range(board.rows):
        for x in range(board.cols):
            draw_tile(screen, Coord(x, y))
    # draw crabs on top
    draw_crabs(screen, board)

def draw_tile(screen, coord: Coord):
    px = coord.x * TILE_SIZE
    py = coord.y * TILE_SIZE
    rect = pygame.Rect(px , py, TILE_SIZE, TILE_SIZE)
    
    pygame.draw.rect(screen, (20, 20, 20), rect, BORDER_SIZE)

COLOR_MAP = {
    '1': (255, 50, 50),     # Red
    '2': (50, 200, 50),     # Green
    '3': (50, 100, 255),    # Blue
    '4': (255, 220, 50),    # Yellow
    '5': (255, 100, 200),   # Pink
    '6': (150, 50, 255),    # Purple
    '7': (255, 150, 50),    # Orange
    '8': (50, 220, 220),    # Cyan
    '9': (180, 100, 50),    # Brown
    '10': (100, 255, 180),   # Mint
    '11': (200, 200, 200),   # Light Gray
    '12': (255, 80, 120)     # Coral
}

def draw_crabs(screen, board: Board):
    for crab in board.crabs:
        draw_crab(screen, crab)

def draw_crab(screen, crab: Crab):
    color = COLOR_MAP[crab.number]
    for coord in crab.position.coords:
        px = coord.x * TILE_SIZE
        py = coord.y * TILE_SIZE
        pygame.draw.rect(screen, color, (px, py, TILE_SIZE, TILE_SIZE))

def run_pygame_animation(board: Board, moves: list[str], name = ""):
    screen = init_pygame(board, name)

    screen.fill((200, 200, 200))
    draw_board(screen, board)  

    for move in moves:
        board.move_crab(move)
        screen.fill((200, 200, 200))
        draw_board(screen, board)

        pygame.time.wait(MS_WAIT_BETWEEN_MOVES)        
        pygame.display.flip()

    pygame.time.wait(MS_WAIT_BETWEEN_MOVES)
    pygame.quit()

