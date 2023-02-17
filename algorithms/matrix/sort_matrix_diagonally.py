"""
Given a m * n matrix mat of integers,
sort it diagonally in ascending order
from the top-left to the bottom-right
then return the sorted array.

mat = [
    [3,3,1,1],
    [2,2,1,2],
    [1,1,1,2]
]

Should return:
[
    [1,1,1,1],
    [1,2,2,2],
    [1,2,3,3]
]
"""

from heapq import heappush, heappop
from typing import List


def sort_diagonally(mat: List[List[int]]) -> List[List[int]]:
    
    branches = set()
    total_num_branches = 9

    # If the input is a vector, return the vector
    if len(mat) == 1 or len(mat[0]) == 1:
        # ID: 1
        branches.add(1)
        return mat
    else:
        # ID: 2 
        branches.add(2)

    # Rows + columns - 1
    # The -1 helps you to not repeat a column
    for i in range(len(mat)+len(mat[0])-1):
        # ID: 3
        branches.add(3)

        # Process the rows
        if i+1 < len(mat):
            # ID: 4
            branches.add(4)
            # Initialize heap, set row and column
            h = []
            row = len(mat)-(i+1)
            col = 0

            # Traverse diagonally, and add the values to the heap
            while row < len(mat):
                # ID: 5
                branches.add(5)
                heappush(h, (mat[row][col]))
                row += 1
                col += 1

            # Sort the diagonal
            row = len(mat)-(i+1)
            col = 0
            while h:
                # ID: 6
                branches.add(6)
                ele = heappop(h)
                mat[row][col] = ele
                row += 1
                col += 1
        else:
            # Process the columns
            # Initialize heap, row and column
            # ID: 7
            branches.add(7)
            h = []
            row = 0
            col = i - (len(mat)-1)

            # Traverse Diagonally
            while col < len(mat[0]) and row < len(mat):
                # ID: 8
                branches.add(8)
                heappush(h, (mat[row][col]))
                row += 1
                col += 1

            # Sort the diagonal
            row = 0
            col = i - (len(mat)-1)
            while h:
                # ID: 9
                branches.add(9)
                ele = heappop(h)
                mat[row][col] = ele
                row += 1
                col += 1

    with open('data/branch-coverage', 'a') as f:
        function_name = "sort_matrix_diagonally"
        total_branches = 9
        ratio = str(len(branches) / total_branches)
        f.write(
            f'{function_name},{total_branches},{ratio},'
        )
        branches_not_found = ""
        for i in range(1, int(total_branches) + 1):
            if i not in branches:
                branches_not_found += f"{str(i)};"
        if branches_not_found == "":
            f.write("0")
        else:
            branches_not_found = branches_not_found.strip(";")
            f.write(branches_not_found)

        f.write('\n')


    # Return the updated matrix
    return mat
