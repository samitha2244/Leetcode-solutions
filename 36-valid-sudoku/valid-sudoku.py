class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row=[set() for i in range(9)]
        column=[set() for i in range(9)]
        box=[set() for i in range(9)]
        for i in range(0,9):
            for j in range(0,9):
                num=board[i][j]
                if num==".":
                    continue
                if num in row[i]:
                    return False
                else:
                    row[i].add(num) 
        for i in range(0,9):
            for j  in range(0,9):
                num=board[i][j]
                if num==".":
                    continue
                if num in column[j]:
                    return False
                else:
                    column[j].add(num)
        for i in range(0,9):
            for j in range(0,9):
                num=board[i][j]
                if num==".":
                    continue
                box_index = (i // 3) * 3 + (j // 3)

                if num in box[box_index]:
                    return False
                else:
                    box[box_index].add(num)
        return True                                    

        