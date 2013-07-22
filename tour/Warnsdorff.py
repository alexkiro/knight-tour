class Warnsdorff:
    _knight_jumps = ((-2, 1), (-2, -1), #The 8 possible moves for a knight
                     (2, 1), (2, -1),
                     (1, -2), (-1, -2),
                     (1, 2), (-1, 2))
    def __init__(self, n, m, i, j):
        initial = i * m + j
        self.positions = [initial]
        self.n = n #rows number
        self.m = m #cols number
        self.visited = [False for _ in range(n * m)]
        self.visited[initial] = True
        
    def check_on_board(self, i, j):
        return i >= 0 and i < self.n and j >= 0 and j < self.m
    
    def calculate(self, p):
        """Returns the Warnsdorff coefficient for square p.
        This represent the number of not visited squares available
        for a knight from position p on the chess board.
        
        p - zero based index of the square in the flatten array          
        """
        count = 0
        i, j = p / self.m, p % self.m
        for jump in Warnsdorff._knight_jumps:
            if self.check_on_board(i + jump[0], j + jump[1]) and self.visited[(i + jump[0]) * self.m + j + jump[1]] == False:
                count += 1
        return count
    
    def start(self):
        """Start looking for the solution
        Returns the list of the squares and True if the solution is valid,
        False otherwise
        """
        count = 1
        while self.step() != None:
            count += 1
        return self.positions, count == self.n * self.m
    
    def step(self):
        i = self.positions[-1] / self.m
        j = self.positions[-1] % self.m
        pos = [] #list of tuples of form (<warnsdorff coefficient>,<position>)
        for jump in Warnsdorff._knight_jumps:
            p = (i + jump[0]) * self.m + j + jump[1]
            if self.check_on_board(i + jump[0], j + jump[1]) and self.visited[p] == False:                
                pos.append((self.calculate(p), p))
        if len(pos) != 0:
            pos = sorted(pos,key = lambda v: v[0])  #sort list accorindg to the Warnsdorff coefficient
            self.positions.append(pos[0][1])
            self.visited[pos[0][1]] = True
            return pos[0][1]
        else: #no available squares left
            return None
                
        
                
        
                
                
        
