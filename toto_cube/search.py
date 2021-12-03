class Search(object):
    def __init__(self, world, max_calls):
        self.world = world
        self.max_calls = max_calls

    def __call__(self):
        print("Search started")
        self.calls = 0
        self.exhaustive = True

        self.solution = self.solve(self.world)
        self.log_results()
        return self.solution

    def log_results(self):
        print("Calls", self.calls)
        print("Exhaustive", self.exhaustive)
        print("solution", self.solution)

    def solve(self, world):
        world.show()
        if world.is_solved():
            return world
        if self.calls > self.max_calls:
            self.exhaustive = False
            return

        for new_world in world.next_worlds():
            solution = self.solve(new_world)
            if solution:
                return solution
