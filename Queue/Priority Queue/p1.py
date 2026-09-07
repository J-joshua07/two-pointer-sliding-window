import heapq

pq = []

heapq.heappush(pq, (2, "Normal"))
heapq.heappush(pq, (1, "Emergency"))
heapq.heappush(pq, (3, "Low"))

print(heapq.heappop(pq))
print(heapq.heappop(pq))
print(heapq.heappop(pq))