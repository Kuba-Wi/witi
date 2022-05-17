
class Task:
    def __init__(self, p, w, d):
        self.p = p
        self.w = w
        self.d = d


def get_bits_pos(n):
    bin_num = f"{n:b}"
    bits_list = []
    for i in range(len(bin_num)):
        if bin_num[i] == "1":
            bits_list.append(len(bin_num) - i - 1)

    return bits_list

# tasks = [Task(2, 3, 4), Task(4, 3, 3), Task(1, 4, 5), Task(3, 2, 2)]
tasks = [Task(1, 2, 748),
         Task(46, 5, 216),
         Task(5, 7, 673),
         Task(93, 4, 514),
         Task(83, 1, 52),
         Task(53, 7, 7),
         Task(38, 1, 413), 
         Task(68, 6, 922),
         Task(84, 5, 91),
         Task(65, 4, 694)]

F = [0]
last_item = [-1]
for i in range(1, 2 ** len(tasks)):
    F.append(-1)
    last_item.append(-1)


def add_result(n):
    tasks_ids = get_bits_pos(n)
    if len(tasks_ids) == 1:
        F[n] = max(tasks[tasks_ids[0]].w * (tasks[tasks_ids[0]].p - tasks[tasks_ids[0]].d), 0)
        last_item[n] = tasks_ids[0]
        return

    C = 0
    for t_id in tasks_ids:
        C += tasks[t_id].p

    for t_id in tasks_ids:
        if F[2 ** t_id] == -1:
            add_result(2 ** t_id)
        if F[n - 2 ** t_id] == -1:
            add_result(n - 2 ** t_id)

        K = max((C - tasks[t_id].d) * tasks[t_id].w, 0)

        if (F[n] == -1) or (F[n - 2 ** t_id] + K < F[n]):
            F[n] = F[n - 2 ** t_id] + K
            last_item[n] = t_id


add_result(2 ** len(tasks) - 1)
print(F[-1])

index = 2 ** len(tasks) - 1
last = []
while index > 0:
    last.insert(0, last_item[index] + 1)
    index -= 2 ** last_item[index]

print(last)
            
