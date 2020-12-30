from collections import defaultdict


class Solver:
    def __init__(self, target, rules):
        self.target = target
        self._bags = self._parse_rules(rules)
        self._valid_bags = set()

    def _parse_rules(self, rules):
        bags = defaultdict(list)
        for rule in rules:
            parent, content = rule.split(' bags contain ')
            for inner_bag in content.split(', '):
                amount, *name, _ = inner_bag.split(' ')
                if amount != 'no':
                    bags[parent].append(' '.join(name))
        return bags

    def _solve(self, target):
        for parent in self._bags:
            content = self._bags[parent]
            if target in content:
                self._solve(parent)
                self._valid_bags.add(parent)

    @property
    def valid_bags(self):
        self._solve(self.target)
        return self._valid_bags


with open('input.txt', 'r') as f:
    rules = f.read().splitlines()

solver = Solver('shiny gold', rules)
print(len(solver.valid_bags))
