class TicTacToe:
    def _init_(self):
        self.board=[['']*3 for i in range(3)]
        self.player='X'

    def mark(self, i,j):
        if not (0<=i<=2 and 0<=j<=2):
            raise ValueError('Invalid board')
        if self.board[i][j]!=''
            raise ValueError('Position already occupied')
        if self.winner()is not None:
            raise ValueError('Game complete')
        self.board[i][j]=self.player
        if self.player=='X':
            self.player='0'
        else:
            self.player='X'

    def winner(self):
        for mark in 'X0':
            if (mark==self.board[0][0]==self.board[0][1]==self.board[0][2] or
                mark==self.board[1][0]==self.board[1][1]==self.board[1][2] or
                mark==self.board[2][0]==self.board[2][1]==self.board[2][2]):
                return mark
        return None
        
