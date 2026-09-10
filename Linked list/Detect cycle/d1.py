class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# Create nodes
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

head.next = node2
node2.next = node3
node3.next = node4

# Create cycle
node4.next = node2

print(has_cycle(head))