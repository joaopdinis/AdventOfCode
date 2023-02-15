from __future__ import annotations
from re import findall, search
import math
class Monkey:
    def __init__(self, items:list[int], operation:str, divisor:int, test_results:tuple[int]) -> None:
        self.items:list[int] = items
        self.operation:str = operation
        self.divisor:int = divisor
        self.test_results:tuple(int) = test_results
        self.items_inspected = 0
    
    def inspectItems(self, monkeys:list[Monkey], lcm:int) -> None:
        for item in self.items:
            item = self.do_operation(item)
            
            item  = item % lcm

            if item % self.divisor == 0:
                monkeys[self.test_results[0]].addItem(item)
            else:
                monkeys[self.test_results[1]].addItem(item)
            
            self.items_inspected += 1

        self.items = []

            
    def do_operation(self, old:int) -> int:
        return eval(self.operation)

    def addItem(self, item:int) -> None:
        self.items.append(item)

    def __str__(self) -> str:
        return f'  Items: {self.items}\n  Operation: {self.operation}\n  Divisor: {self.divisor}\n    True: {self.test_results[0]}\n    False: {self.test_results[1]}'

monkeys:list[Monkey] = []

line_index = 1
input_monkey_lines = 7
for line in open('input.txt'):
    if line == '\n':
        continue

    if line_index == 2:
        items = [int(s) for s in findall(r'-?\d+\.?\d*', line)]
    elif line_index == 3:
        operation = line.split('=')[1]
    elif line_index == 4:
        test = int(search(r'\d+', line).group())
    elif line_index == 5:
        true_value = int(search(r'\d+', line).group())
    elif line_index == 6:
        false_value = int(search(r'\d+', line).group())
        line_index = 0
        monkeys.append(Monkey(items, operation, test, (true_value, false_value)))
        items = []

    line_index += 1


lcm = math.lcm(*[monkey.divisor for monkey in monkeys])
rounds = 10000

for i in range(rounds):
    round = i + 1
    for monkey in monkeys:
        monkey.inspectItems(monkeys, lcm)
    

top_2_monkeys = sorted([monkey.items_inspected for monkey in monkeys], reverse=True)[:2]

print(top_2_monkeys[0]*top_2_monkeys[1])