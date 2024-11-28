import numpy as np
# # temperatures = [73,74,75,71,69,72,76,73]

# # n = len(temperatures)
# # print(n)

# # for i in range(n):
# #     print(i)

# # nums = [4,1,2]

# # idx = {x: i for i,x in enumerate(nums)}
# # print(idx)

# stack = [1,2,3,4,5]

# print(stack.pop())

a = np.array([1,2,3,4,5])
b = np.array([[1,2,3],[4,5,6]])

print("a.mean:",np.mean(a))

print("b.axis=0:",np.mean(b, axis=0))
print("b.axis=1:",np.mean(b, axis=1))

