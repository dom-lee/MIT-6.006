"""
    [Lecture 05.]
    Binary Search Tree, BST Sort

    Time Complexity: 𝛩(h)
    - h: height of the tree
    - worst case: time complexity -> 𝛩(n)

    Space Complexity: 𝛩(n)
"""

from typing import List


class Node:
    def __init__(self, key: int):
        self.val = key
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.val)


class BinarySearchTree:
    def __init__(self, keys: List[int]):
        self.root = None

        for key in keys:
            self.insert(key)
                    
    # Insert a node into Binary Search Tree
    def insert(self, key: int) -> None:
        node = Node(key)
        parent = self.root

        if not parent:
            self.root = node
            return

        while parent:
            if parent.val < key:
                if parent.right:
                    # keep travel to right
                    parent = parent.right
                else:
                    parent.right = node
                    node.parent = parent
                    return
            else:
                if parent.left:
                    # keep travel to left
                    parent = parent.left
                else:
                    parent.left = node
                    node.parent = parent
                    return

    def search(self, key: int) -> Node or None:
        node = self.root

        while node:
            if node.val == key:
                return node
            elif node.val < key:
                if node.right:
                    node = node.right
                else:
                    return None
            else:
                if node.left:
                    node = node.left
                else:
                    return None

    def sort(self) -> List[int]:
        sorted_list = []

        def sort_recursion(node):
            if node:
                sort_recursion(node.left)
                sorted_list.append(node.val)
                sort_recursion(node.right)

        sort_recursion(self.root)

        return sorted_list

    def min(self, node: Node = None) -> Node:
        if not node:
            node = self.root

        while node.left:
            node = node.left
        return node

    def max(self, node: Node = None) -> Node:
        if not node:
            node = self.root
        while node.right:
            node = node.right
        return node

    def delete(self, key: int) -> None:
        node = self.search(key)

        if not node:
            return
        else:
            if node.left and node.right:
                replace_node = self.min(node.right)
                node.val = replace_node.val
                replace_node.parent.left = None
            else:
                parent = node.parent
                child = node.left or node.right
                child.parent = parent

                if node is parent.left:
                    parent.left = child
                else:
                    parent.right = child

    def count_less_than(self, key: int) -> int:
        def count_recursion(node):
            if not node:
                return 0

            if node.val < key:
                return 1 + count_recursion(node.left) + count_recursion(node.right)
            else:
                return count_recursion(node.left)

        return count_recursion(self.root)

        
def main():
    bst = BinarySearchTree([49, 46, 79, 43, 64, 83])
    print(bst.count_less_than(79))


if __name__ == "__main__":
    main()