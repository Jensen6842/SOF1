class Blotris():
    def __init__(self, rows, cols):
        if (rows < 5) or (cols < 5):
            raise ValueError
        self._board = []
        self.temp = []
        for a in range(cols):
            self.temp.append(0)
        for b in range(rows):
            self._board.append(self.temp)

    #I hate this question
    def add(self, shape, row, col):
        self.board = self._board
        self.length = len(shape)
        self.width = len(shape[0])
        for a in range(self.length): #For every row in shape
            for b in range(self.width): #For every column in those lists
                if shape[a][b] == 1:
                    print(row+a, col+b)
                    if self._board[row+a][col+b] == 0:
                        self.board[row+a][col+b] = 1
                        print(self.board)
                    else:
                        return False
        self._board = self.board
        return True


    #I have no clue why this doesn't work
    #I am literally slamming my head against my desk
    def update(self):
        #Checks every row
        for a in range(len(self._board)):
            #Looks for row with all 1s
            if 0 in self._board[a]:
                pass
            else:
                #Row replaces the next row
                for b in range(a):
                    self._board[b+1] = self._board[b]
                #So this part makes the first row all 0s, but for some reason
                #it also makes others up to the all 1s into 0s
                #I spent 4 hours on question 5
                for c in range(len(self._board[0])):
                    self._board[0][c] = 0
