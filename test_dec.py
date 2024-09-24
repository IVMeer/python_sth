from collections import deque

st = 'abcd'
dst = deque(st)

print(dst)

dst.append(1)
print(dst)

dtt = deque()
dtt.append(1)
dtt.appendleft(3)
print(dtt)