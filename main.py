from cycle import Cycle
from northwest_corner_method import NorthWest
from potential import Potential
from exes import Exes

from input_data import matrix, needs, stacks

north = NorthWest(matrix, needs, stacks)
filled_matrix = north.make_distribution()

for row in filled_matrix:
    print(row)
print(f'F(x) = {Exes(matrix, filled_matrix).get_exes()}')
print('-----------------------')

while True:
    potential = Potential(matrix, filled_matrix)
    cell = potential.get_coords()
    print(f'Cell: {cell}')
    if cell is None:
        break

    cycle = Cycle(filled_matrix, cell)

    filled_matrix = cycle.make_cycle()

    print('Cycle: ')

    for row in cycle.cycle_map:
        print(row)

    print()
    print('Matrix: ')

    for row in filled_matrix:
        print(row)
    print(f'F(x) = {Exes(matrix, filled_matrix).get_exes()}')
    print('-----------------------')
