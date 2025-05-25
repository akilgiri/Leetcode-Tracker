# Last updated: 5/25/2025, 1:08:31 PM
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix = self.vertical_reversal(matrix)
        matrix = self.transpose(matrix)
        print(matrix)

        # # vertical reversal and then transpose of matrix

        # edge_length = len(matrix)

        # top = 0
        # bottom = edge_length - 1

        # while top < bottom:
        #     for col in range(edge_length):
        #         temp = matrix[top][col]
        #         matrix[top][col] = matrix[bottom][col]
        #         matrix[bottom][col] = temp
        #     top += 1
        #     bottom -= 1

        # for col in range(edge_length):
        #     temp = matrix

        # for row in range(edge_length):
        #     for col in range(row+1, edge_length):
        #         temp = matrix[row][col]
        #         matrix[row][col] = matrix[col][row]
        #         matrix[col][row] = temp
        
        return matrix

    def vertical_reversal(self, matrix):
        top = 0
        bottom = len(matrix) -1

        while top < bottom:
            for col in range(len(matrix)):
                temp = matrix[top][col]
                matrix[top][col] = matrix[bottom][col]
                matrix[bottom][col] = temp
            top += 1
            bottom -= 1    

        return matrix   

    def transpose(self, matrix):
        for row in range(len(matrix)):
            for col in range(row+1, len(matrix)):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp
        return matrix