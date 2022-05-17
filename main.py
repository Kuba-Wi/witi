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


def fill_F(n, F, tasks, last_tasks):
    tasks_ids = get_bits_pos(n)
    if len(tasks_ids) == 1:
        F[n] = max(tasks[tasks_ids[0]].w * (tasks[tasks_ids[0]].p - tasks[tasks_ids[0]].d), 0)
        last_tasks[n] = tasks_ids[0]
        return

    C = 0
    for t_id in tasks_ids:
        C += tasks[t_id].p

    for t_id in tasks_ids:
        if F[2 ** t_id] == -1:
            fill_F(2 ** t_id, F, tasks, last_tasks)
        if F[n - 2 ** t_id] == -1:
            fill_F(n - 2 ** t_id, F, tasks, last_tasks)

        K = max((C - tasks[t_id].d) * tasks[t_id].w, 0)

        if (F[n] == -1) or (F[n - 2 ** t_id] + K < F[n]):
            F[n] = F[n - 2 ** t_id] + K
            last_tasks[n] = t_id


def witi(tasks):
    F = [0]
    last_tasks = [-1]
    for i in range(1, 2 ** len(tasks)):
        F.append(-1)
        last_tasks.append(-1)

    fill_F(2 ** len(tasks) - 1, F, tasks, last_tasks)

    index = 2 ** len(tasks) - 1
    tasks_order = []
    while index > 0:
        tasks_order.insert(0, last_tasks[index] + 1)
        index -= 2 ** last_tasks[index]

    return F[-1], tasks_order


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

res, ord = witi(tasks)
print(res, ord)   
