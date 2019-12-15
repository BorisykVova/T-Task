from typing import List, Optional

Matrix = List[List[float]]


class NorthWest:

    def __init__(self, matrix: Matrix, needs: List[float], stacks: List[float]):
        self.matrix = matrix
        self.needs = needs
        self.stacks = stacks

        self.close_t()

        self.n = len(self.stacks)
        self.m = len(self.needs)

        self.distribution = [[None for _ in range(self.m)] for _ in range(self.n)]

    def make_distribution(self) -> List[List[Optional[float]]]:
        index = 0
        for j in range(self.m):
            for i in range(index, self.n):
                stack = self.stacks[i]
                need = self.needs[j]

                value = min(stack, need)
                self.distribution[i][j] = value
                need -= value
                stack -= value

                self.stacks[i] = stack
                self.needs[j] = need

                index = i
                if need == 0:
                    break

        return self.distribution

    def close_t(self):
        total_needs = sum(self.needs)
        total_stacks = sum(self.stacks)

        if total_needs == total_stacks:
            return

        value = abs(total_stacks - total_needs)
        if total_needs > total_stacks:
            new_stack = [0 for _ in range(len(self.needs))]
            self.matrix.append(new_stack)
            self.stacks.append(value)
        else:
            for row in self.matrix:
                row.append(0)
            self.needs.append(value)