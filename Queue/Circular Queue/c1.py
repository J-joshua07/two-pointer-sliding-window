class CircularQueue:

    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, value):

        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full")
            return

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value

    def dequeue(self):

        if self.front == -1:
            print("Queue is Empty")
            return

        value = self.queue[self.front]
        self.queue[self.front] = None

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return value

    def display(self):
        print(self.queue)


q = CircularQueue(5)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

q.display()

print("Removed:", q.dequeue())
print("Removed:", q.dequeue())

q.enqueue(60)
q.enqueue(70)

q.display()