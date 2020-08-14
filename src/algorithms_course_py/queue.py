from collections import deque
# deque is optimized for access near endpoints

# craete an empty deque object
queue = deque()

# add some items
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(queue)

# pop item off left
queue.popleft()
print(queue)