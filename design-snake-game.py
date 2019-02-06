class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.w = width
        self.h = height
        self.food = food
        self.food_i = 0
        self.snake = [(0,0)]
        self.delta = {
            'U': (-1, 0),
            'L': (0, -1),
            'R': (0, 1),
            'D': (1, 0),
        }
        self.gameover = False
        
    def mv(self, loc, delta):
        return (loc[0]+delta[0], loc[1]+delta[1])

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        if self.gameover:
            return -1
        head = self.snake[0]
        next_head = self.mv(head, self.delta[direction])
        #print head, next_head
        if next_head[0] < 0 or next_head[0] >= self.h:
            self.gameover = True
            return -1
        if next_head[1] < 0 or next_head[1] >= self.w:
            self.gameover = True
            return -1
        if next_head in self.snake[:-1]:
            self.gameover = True
            return -1
        food = None
        if self.food_i < len(self.food):
            food = tuple(self.food[self.food_i])
        #print direction, head, next_head, food, self.snake
        if next_head == food:
            if next_head == self.snake[-1]:
                self.gameover = True
                return -1
            self.snake.insert(0, next_head)
            self.food_i += 1
        else:
            self.snake.insert(0, next_head)
            self.snake.pop(-1)
        return len(self.snake) - 1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
