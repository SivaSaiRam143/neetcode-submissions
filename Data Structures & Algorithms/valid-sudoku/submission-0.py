class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,9):
            nums = []
            for x in board[i]:
                if x != ".":
                    nums.append(x)
            if len(nums) != len(set(nums)): return False
            nums = []
            for j in range(0,9):
                if board[j][i] != ".": 
                    nums.append(board[j][i])
            if len(nums) != len(set(nums)): return False

        nums = [0,3,6]
        for i in nums:
            for j in nums:
                cur_list = [board[i][j],board[i][j+1],board[i][j+2], board[i+1][j], board[i+2][j], board[i+1][j+1], board[i+2][j+1], board[i+1][j+2], board[i+2][j+2]]
                cur_list = [x for x in cur_list if x!="."]
                if len(cur_list) != len(set(cur_list)): return False
        return True