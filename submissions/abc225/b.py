import sys

N = int(input())
d = dict()

# 登場回数を数えて、N-1のnodeがあればyes
for _ in range(N-1):
    a, b = input().split()
    if d.get(a):
        d[a] += 1
    else:
        d[a] = 1

    if d.get(b):
        d[b] += 1
    else:
        d[b] = 1

for value in d.values():
    if value == N - 1:
        print("Yes")
        sys.exit()

print("No")