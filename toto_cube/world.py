import numpy as np
import matplotlib.pyplot as plt
import toto_cube.blocks as blocks


class World(object):
    def __init__(self, blocks, topography=None):
        self.blocks = blocks
        self.topography = topography
        if self.topography is None:
            self.topography = np.zeros((5, 5, 5), dtype=np.bool)

    def is_solved(self):
        conj = True
        for x in range(5):
            for y in range(5):
                conj &= self.topography[x][y][4]
        return conj

    def new_topography(self, block):
        if (
            self.coord["x"] + block[0] > 5
            or self.coord["y"] + block[1] > 5
            or self.coord["z"] + block[2] > 5
        ):
            return None

        for x in range(block[0]):
            for y in range(block[1]):
                if self.topography[
                    self.coord["x"] + x, self.coord["y"] + y, self.coord["z"]
                ]:
                    return None

        new_topography = np.array(self.topography)
        for x in range(block[0]):
            for y in range(block[1]):
                for z in range(block[2]):
                    new_topography[
                        self.coord["x"] + x, self.coord["y"] + y, self.coord["z"] + z
                    ] = True
        return new_topography

    def next_worlds(self):
        self.coord = None
        coord = {"x": 0, "y": 0, "z": 0}
        while coord["z"] < 5:
            if not self.topography[coord["x"]][coord["y"]][coord["z"]]:
                self.coord = coord
                break
            coord["x"] += 1
            coord["y"] += coord["x"] // 5
            coord["z"] += coord["y"] // 5
            coord["x"] = coord["x"] % 5
            coord["y"] = coord["y"] % 5

        next_worlds = []
        for block_type, remaining in enumerate(self.blocks):
            if not remaining:
                continue
            block = blocks.get_block(block_type)
            for orientation in block.orientations:
                new_topo = self.new_topography(orientation)
                if new_topo is not None:
                    left_blocks = np.array(self.blocks)
                    left_blocks[block_type] += -1
                    next_worlds.append(World(left_blocks, new_topo))
        return next_worlds

    def show(self, figsize=4):
        alpha = 0.9
        axes = [5, 5, 5]
        data = np.zeros(axes, dtype=np.bool)
        colors = np.empty(axes + [4], dtype=np.float32)

        for x in range(5):
            for y in range(5):
                for z in range(5):
                    if self.topography[x, y, z]:
                        data[x, y, z] = True
                        colors[x, y, z] = np.array([0.5, 0.5, 0.5, alpha])

        fig = plt.figure(figsize=(figsize, figsize))
        ax = fig.add_subplot(projection="3d")
        ax.voxels(data, facecolors=colors, edgecolors="black")
        ax.view_init(40, 45 * 2 + 180 * 2)
        plt.show()
