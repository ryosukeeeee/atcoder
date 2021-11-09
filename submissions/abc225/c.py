import sys
import math

N, M = map(int, input().split())

col = list(map(int, input().split()))

# 7で割ったあまり 
# 何列目か
row_index = col[0] % 7

# 何行目か
col_index = math.ceil(col[0] / 7)

# 7列目ならrow_indexは0
# Mが2より大きいとNo
if row_index == 0 and M > 2:
    print("No")
    sys.exit()

if M > (9 - row_index):
    print("No")
    sys.exit()

# col[1]以降の値をチェックする
for i in range(1, len(col)):
    if col[0] + i != col[i]:
        print("No")
        sys.exit()

# 2行目以降のチェック
for i in range(N - 1):
    col = list(map(int, input().split()))

    # 7で割ったあまり 
    # 何列目か
    next_row_index = col[0] % 7
    if row_index != next_row_index:
        print("No")
        sys.exit()

    # 何行目か
    next_col_index = math.ceil(col[0] / 7)
    if col_index + i + 1 != next_col_index:
        print("No")
        sys.exit()

    # col[1]以降の値をチェックする
    for j in range(1, len(col)):
        if col[0] + j != col[i]:
            print("No")
            sys.exit()

print("Yes")