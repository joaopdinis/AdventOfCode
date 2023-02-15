import re
from collections import defaultdict

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

def max_pressure(valve, time, pressure, unopened_valves):
    if time <= 0 or len(unopened_valves) == 0:
        return pressure
    
    total_pressure = 0
    for v in unopened_valves:
        t = time - get_time(valve, v) - 1
        p = t * valves[v].flow_rate + pressure
        unopened_valves_rm_v = [x for x in unopened_valves if x != v]
        total_pressure = max(total_pressure, p, max_pressure(v, t, p, unopened_valves_rm_v))

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


print(max_pressure('AA', 30, 0, unopened_valves))

