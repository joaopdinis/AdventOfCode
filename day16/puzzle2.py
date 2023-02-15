import re
from collections import defaultdict
from itertools import combinations, permutations
from random import sample

class Valve:
    def __init__(self, label, flow_rate, next_valves) -> None:
        self.label = label
        self.flow_rate = flow_rate
        self.next_valves = next_valves
    
    def __str__(self) -> str:
        return f'{self.label}: {self.flow_rate} -- {self.next_valves}'


def get_time(v_src, v_dst):
    visited = defaultdict(bool)
    dist = defaultdict(int)
    
    queue = []

    queue.append(v_src)
    visited[v_src] = True

    while len(queue) != 0:
        s = queue.pop(0)

        for i in valves[s].next_valves:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                dist[i] = dist[s] + 1
                if i == v_dst:
                    return dist[i]
    
    return -1

def max_pressure(valve1, valve2, time1, time2, pressure, unopened_valves):
    if (time1 <= 0 and time2 <= 0) or len(unopened_valves) == 0:
        return pressure
    
    total_pressure = 0
    if len(unopened_valves) == 1:
        v = unopened_valves[0]
        t1 = time1 - get_time(valve1, v) - 1
        t2 = time2 - get_time(valve2, v) - 1
        if t1 >= 0 and t1 >= t2:
            p = t1 * valves[v].flow_rate + pressure
        elif t2 >= 0 and t2 >= t1:
            p = t2 * valves[v].flow_rate + pressure
        else:
            p = 0
        # print(p)
        total_pressure = max(total_pressure, p, pressure)
    else:
        func = combinations if valve1 == 'AA' and valve2 == 'AA' else permutations

        for v,u in func(sample(unopened_valves, min(5, len(unopened_valves))), 2):

            t1 = time1 - get_time(valve1, v) - 1
            t2 = time2 - get_time(valve2, u) - 1
            p1 = t1 * valves[v].flow_rate
            p2 = t2 * valves[u].flow_rate
            p = p1 + p2 + pressure
            # print(p)
            unopened_valves_rm_v_u = [x for x in unopened_valves if x != v and x != u]
            total_pressure = max(total_pressure, p, max_pressure(v, u, t1, t2, p, unopened_valves_rm_v_u))

    return total_pressure

valves = defaultdict(Valve)

input = [l.strip() for l in open('input.txt')]

unopened_valves = []
for line in open('input.txt'):
    flow_rate = int(re.search('\d+', line).group())
    valves_line = re.findall('[A-Z]{2}', line)
    if flow_rate > 0 :
        unopened_valves.append(valves_line[0])

    valves[valves_line[0]] = Valve(valves_line[0], flow_rate, valves_line[1:])

print(unopened_valves)
print(max_pressure('AA', 'AA', 26, 26, 0, unopened_valves))

