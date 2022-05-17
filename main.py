
class Task:
    def __init__(self, p, w, d):
        self.p = p
        self.w = w
        self.d = d


def get_bits_pos(num):
    bin_num = f"{num:b}"
    bits_list = []
    for i in range(len(bin_num)):
        if bin_num[i] == "1":
            bits_list.append(len(bin_num) - i - 1)

    return bits_list

tasks = [Task(2, 3, 4), Task(4, 3, 3), Task(1, 4, 5), Task(3, 2, 2)]
results = [0]
for i in range(1, 2**len(tasks)):
    results.append(-1)


print(results)

get_bits_pos(13)

def add_result(num):
    bits_pos = get_bits_pos(num)
    if len(bits_pos) == 1:
        results[num] = tasks[bits_pos[0]].w * (tasks[bits_pos[0]].p - tasks[bits_pos[0]].d)
        if results[num] < 0:
            results[num] = 0
        return

    for pos in bits_pos:
        if results[2**pos] == -1:
            add_result(2**pos)
        elif results[num - 2**pos] == -1:
            add_result(num - 2**pos)
            
