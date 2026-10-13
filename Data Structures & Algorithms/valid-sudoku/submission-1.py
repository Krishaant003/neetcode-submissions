class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column = len(board)
        row = len(board[0])
        for i in range(column):
            count = dict()
            for j in range(row):
                number = board[i][j]
                if number == ".":
                    continue
                if number not in count:
                    count[number] = 0
                count[number] += 1
                if count[number] > 1:
                    return False
        for i in range(column):
            count = dict()
            for j in range(row):
                number = board[j][i]
                if number == ".":
                    continue
                if number not in count:
                    count[number] = 0
                count[number] += 1
                if count[number] > 1:
                    return False
        L = [[0]*10 for i in range(10)]
        print(L[0][1])
        for i in range(row):
            for j in range(column):
                number = board[i][j]
                if number == ".":
                    continue
                index = (j//3)+(i//3)*3
                print(index,number)
                L[index][int(number)] += 1
                if L[index][int(number)] > 1:
                    
                    return False
        
        return True
        