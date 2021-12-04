from _typeshed import Self
import time


class Search(object):
    def __init__(self, world, run_time, start_point=[], interactive=False):
        self.world = world
        self.run_time = run_time
        self.interactive = interactive
        self.start_point = start_point

    def __call__(self):
        print("Search started")
        self.calls = 0
        self.exhaustive = True

        self.start_time = time.time()
        self.solution = self.solve(self.world)
        self.log_results()
        return self.solution

    def log_results(self):
        print("Calls", self.calls)
        print("Time", time.time() - self.start_point)
        print("Exhaustive", self.exhaustive)
        print("solution", self.solution)

    def solve(self, world):
        self.calls += 1
        if self.interactive:
            print(world.size)
            world.show()
        # Stop conditions
        if world.is_solved():
            return world
        if time.time() - self.start_time > self.run_time:
            self.exhaustive = False
            return world.search_position
        # Search adjacent worlds
        for idx, new_world in enumerate(world.next_worlds()):
            if (
                world.size < len(self.start_point)
                and idx < self.start_point[world.size]
            ):
                continue
            solution = self.solve(new_world)
            if solution:
                return solution
