"""
    [Lecture 04.]
    Heaps ans Heap Sort

    1. Max Heapify
        - Time Complexity: 𝛩(n)

    2. Heap Sort
        - Time Complexity: 𝛩(nlogn)
        - n iterations, 𝛩(logn) for every iteration
"""
from typing import List


def heapify(arr: List[int], parent: int, tail_node: int) -> None:
    """
        Time Complexity: 𝛩(logn)
    """
    left_child = 2 * parent + 1
    right_child = 2 * parent + 2

    # See if left child of root exists and is greater than parent
    if left_child < tail_node and arr[parent] < arr[left_child]:
        arr[parent], arr[left_child] = arr[left_child], arr[parent]     # Swap

    # See if right child of root exists and is greater than parent
    if right_child < tail_node and arr[parent] < arr[right_child]:
        arr[parent], arr[right_child] = arr[right_child], arr[parent]   # Swap

    # Heapify the children
    if left_child < tail_node // 2:
        heapify(arr, left_child, tail_node)
    if right_child < tail_node // 2:
        heapify(arr, right_child, tail_node)


def max_heapify(arr: List[int]) -> None:
    """
        Time Complexity: 𝛩(n)
    """
    for i in range(len(arr)//2 - 1, -1, -1):
        heapify(arr, i, len(arr))


def heap_sort(arr: List[int]) -> None:
    """
        Time Complexity: 𝛩(nlogn)
    """
    # Step1. Build Max_Heap from unordered array
    max_heapify(arr)

    # Step4. Iterate
    for i in range(len(arr)-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]     # Step2. Find Maximum element and swap to last node
        heapify(arr, 0, i)                  # Step3. discard last node from heap and heapify


def main():
    arr = [1, 4, 2, 3, 9, 7, 8, 10, 14, 16]
    heap_sort(arr)
    print(arr)


if __name__ == "__main__":
    main()