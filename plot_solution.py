import numpy as np
from toto_cube.world import *

if __name__ == "__main__":
    solution = World([], np.load("solution/solution.npy"))
    solution.show()

