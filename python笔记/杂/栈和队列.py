# 栈

stack = []

# 入栈
stack.append('A')
print(stack)

# 出栈
res1 = stack.pop()
print(res1)
print(stack)


# 队列


import collections

# 创建一个队列
queue = collections.deque()
print(queue)

# 进队
queue.append("A")
queue.append("B")
print(queue)

# 出队
res2 = queue.popleft()
print(res2)
print(queue)
