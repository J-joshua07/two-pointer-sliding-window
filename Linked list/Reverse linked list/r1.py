class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_linked_list(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev