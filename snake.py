# snake.py
import copy

class SnakeBlockVector:
    def __init__(self, x, y, direction) -> None:
        #x -> Int
        #y -> Int
        #direction -> char {'U', 'D', 'L', 'R'}
        self.x = x
        self.y = y
        self.direction = direction
        

BLOCK_SIZE = 32
VEL = BLOCK_SIZE
class Snake():
    def __init__(self, x, y) -> None:
        self.invalid_directions = {
            'U': 'D',
            'D': 'U',
            'L': 'R',
            'R': 'L',
        }
        self.increaseLength = True
        self.length = 2
        head = SnakeBlockVector(x, y, 'L')
        tail = SnakeBlockVector(x - BLOCK_SIZE, y, 'L')
        self.snakeBlocks = [head, tail]

    def update(self) -> None:

        if (self.increaseLength):
            tail = copy.copy(self.snakeBlocks[-1])
            

        for i in range(self.length - 1, 0, -1):
            self.snakeBlocks[i].x = self.snakeBlocks[i - 1].x
            self.snakeBlocks[i].y = self.snakeBlocks[i - 1].y
        
        if (self.increaseLength):
            self.snakeBlocks.append(tail)
            self.length += 1
            self.increaseLength = False
        

        head = self.snakeBlocks[0]
        match head.direction:
            case 'L':
                head.x -= VEL
                pass
            case 'R':
                head.x += VEL
                pass
            case 'U':
                head.y -= VEL
                pass
            case 'D':
                head.y += VEL
            

    def change_direction(self, direction) -> None: 
        head = self.snakeBlocks[0]
        if not(self.invalid_directions.get(head.direction) == direction):
            head.direction = direction
    
