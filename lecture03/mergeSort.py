"""
Lecture 3: Insertion Sort & Merge Sort

Merge Sort (divide and conquer)
- Time Complexity: 𝛩(nlogn)
    T(n) = C + 2T(n/2) + C*n

- Space Complexity: 𝛩(n)
"""
from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) > 1:
        mid = len(arr) // 2

        left_arr = arr[:mid]
        right_arr = arr[mid:]

        # sorting recursively
        merge_sort(left_arr)
        merge_sort(right_arr)

        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    return arr


def main():
    unsorted_arr = [1, 9, 2, 8, 6, 5, 1, 9, 2, 7, 4, 6, 9, 2, 8, 3, 7, 4, 6, 5]
    sorted_arr = merge_sort(unsorted_arr)
    print(sorted_arr)


if __name__ == "__main__":
    import profile

    profile.run("main()")
