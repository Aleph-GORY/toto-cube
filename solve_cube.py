from toto_cube.world import *
from toto_cube.search import *

if __name__ == "__main__":
    solver = Search(World([6, 6, 5]), 60 * 60, start_point=[],)
    solution = solver()
    # solution = World([6, 6, 5])
    if isinstance(solution, World):
        print(solution.search_position)
        print(solution.topography)
        solution.show()
