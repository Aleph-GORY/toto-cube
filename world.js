let empty_topography = [
    [
        [false, false, false, false, false,],
        [false, false, false, false, false,],
        [false, false, false, false, false,],
        [false, false, false, false, false,],
        [false, false, false, false, false,],
    ],
    [
        [false, false, false, false, false,],
        [false, false, false, false, false,],
        [false, false, false, false, false,],
        [false, false, false, false, false,],
        [false, false, false, false, false,],
    ],
    [
        [false, false, false, false, false,],
        [false, false, false, false, false,],
        [false, false, false, false, false,],
        [false, false, false, false, false,],
        [false, false, false, false, false,],
    ],
    [
        [false, false, false, false, false,],
        [false, false, false, false, false,],
        [false, false, false, false, false,],
        [false, false, false, false, false,],
        [false, false, false, false, false,],
    ],
    [
        [false, false, false, false, false,],
        [false, false, false, false, false,],
        [false, false, false, false, false,],
        [false, false, false, false, false,],
        [false, false, false, false, false,],
    ],
]

class World {
    constructor(blocks, topography) {
        this.blocks = blocks;
        this.topography = topography;
        if (!this.topography) {
            this.topography = empty_topography;
        }
    }

    get is_solved() {
        let conj = true;
        for (let x = 0; x < 5; x++) {
            for (let y = 0; y < 5; y++) {
                conj &= this.topography[x][y][4];
            }
        }
        return conj;
    }

    new_topography(block) {
        if (this.coord.x + block[0] > 5 || this.coord.y + block[1] > 5)
            return;
        for (let x = 0; x < block[0]; x++) {
            for (let y = 0; y < block[1]; y++) {
                if (this.topography[this.coord.x + x][this.coord.y + y][this.coord.z])
                    return;
            }
        }

        var new_topography = this.topography.map(
            x => x.map(y => y.map(z => z))
        );
        for (let x = 0; x < block[0]; x++) {
            for (let y = 0; y < block[1]; y++) {
                for (let z = 0; z < block[2]; z++) {
                    new_topography[this.coord.x + x][this.coord.y + y][this.coord.z + z] = true;
                }
            }
        }
        // console.log(new_topography);
        return new_topography;
    }

    next_worlds() {
        //Find join coord
        this.coord = null;
        var coord = {
            x: 0,
            y: 0,
            z: 0
        };
        while (coord.z < 5) {
            if (!this.topography[coord.x][coord.y][coord.z]) {
                this.coord = coord;
                break;
            }
            coord.x++;
            coord.y += parseInt(coord.x / 5);
            coord.z += parseInt(coord.y / 5);
            coord.x %= 5;
            coord.y %= 5;
        }
        // console.log(this.coord);

        // Possible worlds
        let next_worlds = [];
        let idx = 0;
        for (let block_id = 0; block_id < this.blocks.length; block_id++) {
            let block = this.blocks[block_id];
            if (!block)
                continue;
            for (var orientation of block.orientations) {
                let new_topo = this.new_topography(orientation);
                if (new_topo) {
                    let left_blocks = [...this.blocks];
                    delete left_blocks[block_id];
                    next_worlds[idx++] = new World(left_blocks, new_topo);
                }
            }
        }
        return next_worlds;
    }

    show() {
        cube = this.topography.map(
            x => x.map(y => y.map(z => z))
        );
    }
}