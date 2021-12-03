class Search {
    constructor(world, max_calls) {
        this.world = world;
        this.max_calls = max_calls;
    }

    search() {
        console.log("Search started");
        this.calls = 0;
        this.exhaustive = true;

        this.solution = this.solve(this.world)
        this.log_results();
        return this.solution;
    }

    log_results() {
        console.log("Calls", this.calls);
        console.log("Time");
        console.log("Exhaustive", this.exhaustive);
        console.log("solution", this.solution);
    }

    solve(world) {
        if (cubes.length < 15) {
            cubes.push(world.topography);
            console.log(cubes);
            cubes[0] = world.topography
        }
        if (world.is_solved)
            return world;
        if (this.calls++ > this.max_calls) {
            this.exhaustive = false;
            return;
        }

        for (let new_world of world.next_worlds()) {
            let solution = this.solve(new_world);
            if (solution) {
                return solution;
            }
        }
    }
}
