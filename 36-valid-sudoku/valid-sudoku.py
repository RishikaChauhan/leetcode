class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res=[]
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element !='.':
                    res +=[(i,element), (element,j),(i//3,j//3,element)]
        print(res)
        return len(res)==len(set(res))
        # print(board)
        # for i in range(9):
        #     if sum(list(map(int,board[i])))>45:
        #         return False
        
        # for i in range(9):
        #     sm=0
        #     for j in range(9):
        #         sm+=(int(board[j][i]))
        #     if sm>45: return False
        
