from collections import defaultdict
from typing import NamedTuple


class Bag(NamedTuple):
    amount: int
    name: str


class Solver:
    def __init__(self, target, rules):
        self.target = target
        self._bags = self._parse_rules(rules)
        self._valid_bags = set()
        self._total_bags = defaultdict(int)

    def _parse_rules(self, rules):
        bags = defaultdict(list)
        for rule in rules:
            parent, content = rule.split(' bags contain ')
            for inner_bag in content.split(', '):
                amount, *name, _ = inner_bag.split(' ')
                if amount != 'no':
                    bags[parent].append(Bag(int(amount), ' '.join(name)))
        return bags

    def _solve(self, target):
        for parent in self._bags:
            content = tuple(bag.name for bag in self._bags[parent])
            if target in content:
                self._solve(parent)
                self._valid_bags.add(parent)

    def _count(self, target):
        for child in self._bags[target]:
            self._total_bags[child.name] += child.amount
            for _ in range(child.amount):
                self._count(child.name)

    @property
    def valid_bags(self):
        self._solve(self.target)
        return self._valid_bags

    @property
    def total_bags(self):
        self._count(self.target)
        return sum(self._total_bags.values())


with open('input.txt', 'r') as f:
    rules = f.read().splitlines()

solver = Solver('shiny gold', rules)
print(solver.total_bags)
