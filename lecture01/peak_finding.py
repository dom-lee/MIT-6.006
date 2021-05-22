from typing import *

"""
Lecture 1
Peak Finding (1-D and 2-D)
"""


def find_1d_peak(arr: List[int]) -> int:
    """
    Complexity: Θ(log(n))
    """
    n = len(arr)
    if n == 1:
        return arr[0]
    elif n == 2:
        return arr[0] if arr[0] >= arr[1] else arr[1]
    elif arr[n // 2] < arr[(n // 2) - 1]:
        return find_1d_peak(arr[:n // 2])
    elif arr[n // 2] < arr[(n // 2) + 1]:
        return find_1d_peak(arr[(n // 2) + 1:])

    return arr[n // 2]


def find_2d_peak(arr: List[List[int]]) -> int:
    """
    Complexity: T(n, m) = T(n/2, m) + Θ(m) = Θ(m*log(n))
    """
    n = len(arr)
    m = len(arr[0])

    middle_row = n // 2
    max_in_row = float('-inf')
    column_index = 0

    for j in range(m):
        if arr[middle_row][j] > max_in_row:
            max_in_row = arr[middle_row][j]
            column_index = j

    if n == 1:
        return max_in_row

    elif n == 2:
        if arr[middle_row][column_index] >= arr[middle_row - 1][column_index]:
            return max_in_row
        else:
            return find_2d_peak(arr[:1])

    elif arr[middle_row][column_index] <= arr[middle_row - 1][column_index]:
        return find_2d_peak(arr[:middle_row])

    elif arr[middle_row][column_index] <= arr[middle_row + 1][column_index]:
        return find_2d_peak(arr[middle_row + 1:])

    return max_in_row


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 10, 8, 2]
    matrix = [[4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2],
              [5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3],
              [6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4],
              [7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5],
              [8, 9, 10, 11, 12, 11, 10, 9, 8, 7, 6],
              [7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5],
              [6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4],
              [5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3],
              [4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2],
              [3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1],
              [2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0]]

    print(find_1d_peak(array))
    print(find_2d_peak(matrix))
