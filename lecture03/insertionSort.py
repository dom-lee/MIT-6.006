"""
Lecture 3: Insertion Sort & Merge Sort

Insertion Sort
- Time Complexity: 𝛩(n^2)
- Space Complexity: 𝛩(1)
"""

from typing import List


def insertion_sort(arr: List[int]) -> List[int]:
    """
       𝛩(n^2) Compares, 𝛩(n^2) Swaps
    """
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i - j] < arr[i - j - 1]:
                arr[i - j], arr[i - j - 1] = arr[i - j - 1], arr[i - j]

    return arr


def bianry_insertion_sort(arr: List[int]) -> List[int]:
    """
       - 𝛩(nlogn) Compares, 𝛩(n^2) Swaps
    """
    for i in range(1, len(arr)):
        key = arr[i]
        swap_index = binary_search(arr[:i], 0, i, key)

        del arr[i]
        arr.insert(swap_index, key)

    return arr


def binary_search(arr, low, high, key):
    if high - low == 1:
        if arr[low] < key:
            return high
        else:
            return low

    else:
        mid = (high + low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search(arr, low, mid, key)
        else:
            return binary_search(arr, mid, high, key)


def main():
    arr = [1, 5, 2, 6, 3, 7, 4]
    for _ in range(5):
        arr.extend(arr)

    print(insertion_sort(arr))
    # print(bianry_insertion_sort(arr))


if __name__ == "__main__":
    import profile

    profile.run("main()")