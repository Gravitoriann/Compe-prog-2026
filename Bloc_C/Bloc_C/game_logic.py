from enum import Enum

class Coord:
    ## X is from 0 (left) to 5 (right)
    ## Y is from 0 (top) to 5 (bottom)
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Direction(Enum):
    HORIZONTAL = 0
    VERTICAL = 1
    ANY = 2

class Position:
    def __init__(self, coords: list[Coord]):
        self.coords = coords
    
    def set_coords(self, coords: list[Coord]):
        self.coords = coords

def is_overlaping(pos1: list[Coord], pos2: list[Coord]):
    for pos in pos1:
        for p in pos2:
            if pos == p:
                return True
    return False

class Crab:
    # Number is a str and the crab ID
    def __init__(self, number: str, position: Position, direction: Direction):
        self.number = number
        self.position = position
        self.direction = direction

    def set_position(self, coords: list[Coord]):
        self.position.set_coords(coords)
        
    def __str__(self):
        return f"{self.number}"

class Board:
    def __init__(self, crabs: list[Crab]):
        self.rows = 6
        self.cols = 6
        self.crabs = crabs

    def level_cleared(self):
        ## wining tile for Crab 1 is (5, 2)
        crab = next((crab for crab in self.crabs if crab.number == '1'), None)
        if crab == None:
            print("Board corrupted!!")
            return False
        
        if any(coord == Coord(5, 2) for coord in crab.position.coords):
            return True
        return False

    def __str__(self):
        tiles = [['0' for _ in range(self.cols)] for _ in range(self.rows)]
        for crab in self.crabs:
            for pos in crab.position:
                tiles[pos.y][pos.x] = crab.number
        lines = []
        for row in tiles:
            line_str = "".join(tile for tile in row)
            lines.append(line_str)

        return "\n".join(lines)

    ## Return True if move was succesful, False instead
    def move_crab(self, command):
        crab_number = command[0]
        crab = next((crab for crab in self.crabs if crab.number == crab_number), None)
        if crab == None:
            print("Invalid crab number!!")
            return False
        
        ## Check for direction of movement vs Crab direction
        if ((command[1] == 'U' or command[1] == 'D') and crab.direction == Direction.HORIZONTAL) or ((command[1] == 'R' or command[1] == 'L') and crab.direction == Direction.VERTICAL):
            print("Invalid direction for this crab!!")
            return False
        
        new_coords: list[Coord] = []
        for coord in crab.position.coords:
            if command[1] == 'U':
                new_coords.append(Coord(coord.x, coord.y-1))
            elif command[1] == 'D':
                new_coords.append(Coord(coord.x, coord.y+1))
            elif command[1] == 'L':
                new_coords.append(Coord(coord.x-1, coord.y))
            elif command[1] == 'R':
                new_coords.append(Coord(coord.x+1, coord.y))

        for new_coord in new_coords:
            if new_coord.x < 0 or new_coord.x > 5 or new_coord.y < 0 or new_coord.y > 5:
                print("Invalid move out of bound position!!")
                return False
            
        for other_crab in self.crabs:
            if crab.number != other_crab.number and is_overlaping(new_coords, other_crab.position.coords):
                print("Invalid move overlapping crabs!!")
                return False
            
        crab.set_position(new_coords)
        return True

    def test_path(self, commands: str):
        for command in commands:
            is_valid_move = self.move_crab(command)
            if not is_valid_move:
                return False
            if self.level_cleared():
                return True
        return False
