import sys

class Group:
    # グループに含まれる電車の番号
    contents = set()

    # グループの連結状態
    trains = []

    def isin(self, train_number):
        if train_number in self.contents:
            return True
        else:
            return False
    
    def print_desc(self):
        s = str(len(self.contents))
        s += " " + " ".join(self.trains)
        


N, Q = list(map(int, input().split()))
groups = []

for _ in range(Q):
    query = list(map(int, input().split()))
    q_type = query[0]

    # query[1]とquery[2]を連結する
    if q_type == 1:
        target_left = query[1]
        target_right = query[2]
        target_left_group = None
        target_right_group = None
        for group in groups:
            if group.isin(target_left):
                target_left_group = group
                continue

            if group.isin(target_right):
                target_right_group = group

        

        pass
    # query[1]とquery[2]を離す
    elif q_type == 2:
        pass
    # output
    else:
        target = query[1]
        for group in groups:
            if group.isin(target):
                group.print_desc()
                break

        print("1 " + str(target))


