import numpy as np
import matplotlib.pyplot as plt
import toto_cube.blocks as blocks


class World(object):
    def __init__(self, blocks, topography=None, search_position=[]):
        self.blocks = blocks
        self.topography = topography
        if self.topography is None:
            self.topography = np.zeros((5, 5, 5), dtype=np.int8)
        self.search_position = search_position
        self.size = 17 - np.sum(self.blocks)

    def is_solved(self):
        conj = True
        for x in range(5):
            for y in range(5):
                conj = conj and self.topography[x, y, 4]
        return conj

    def new_topography(self, block):
        if (
            self.coord[0] + block[0] > 5
            or self.coord[1] + block[1] > 5
            or self.coord[2] + block[2] > 5
        ):
            return None

        for x in range(block[0]):
            for y in range(block[1]):
                if self.topography[self.coord[0] + x, self.coord[1] + y, self.coord[2]]:
                    return None

        new_topography = np.array(self.topography)
        for x in range(block[0]):
            for y in range(block[1]):
                for z in range(block[2]):
                    new_topography[
                        self.coord[0] + x, self.coord[1] + y, self.coord[2] + z
                    ] = (self.size + 1)
        return new_topography

    def next_worlds(self):
        self.coord = None
        coord = [0, 0, 0]
        while coord[2] < 5:
            if not self.topography[coord[0], coord[1], coord[2]]:
                self.coord = coord
                break
            coord[0] += 1
            coord[1] += coord[0] // 5
            coord[2] += coord[1] // 5
            coord[0] = coord[0] % 5
            coord[1] = coord[1] % 5

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
                    next_worlds.append(
                        World(
                            left_blocks,
                            new_topo,
                            self.search_position + [len(next_worlds)],
                        )
                    )
        return next_worlds

    def show(self, figsize=4):
        axes = [5, 5, 5]
        data = np.zeros(axes, dtype=np.bool)
        colors = np.empty(axes + [4], dtype=np.float32)

        for x in range(5):
            for y in range(5):
                for z in range(5):
                    if self.topography[x, y, z]:
                        data[x, y, z] = True
                        colors[x, y, z] = (
                            blocks.colors[self.topography[x, y, z] - 1] / 255
                        )

        fig = plt.figure(figsize=(figsize, figsize))
        ax = fig.add_subplot(projection="3d")
        ax.voxels(data, facecolors=colors, edgecolors="black")
        ax.view_init(40, 45 * 2 + 180 * 2)
        plt.show()
