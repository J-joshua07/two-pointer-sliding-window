from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)


def level_order(root):
    if root is None:
        return

    queue = deque([root])

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()

            print(node.data, end=" ")

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        print()


level_order(root)