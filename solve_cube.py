from toto_cube.world import *
from toto_cube.search import *

if __name__ == "__main__":
    solver = Search(World([6, 6, 5]), 100)
    solver()
