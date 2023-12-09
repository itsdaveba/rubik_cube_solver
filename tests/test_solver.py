from .context import rubik_solver

import unittest
import numpy as np
import copy


MAX_DEPTH = 5

class TestCube(unittest.TestCase):
	def test_solver(self):
		cube = rubik_solver.Cube(MAX_DEPTH)
		orientation = copy.deepcopy(cube.position['orientation'])
		permutation = copy.deepcopy(cube.position['permutation'])
		solver = rubik_solver.Solver(cube)
		for depth in range(MAX_DEPTH):
			self.assertFalse(solver.search(solver.cube.position, depth))
			self.assertFalse(solver.solve(depth))
		self.assertTrue(solver.search(solver.cube.position, MAX_DEPTH))
		self.assertTrue(np.array_equal(cube.position['orientation'], orientation))
		self.assertTrue(np.array_equal(cube.position['permutation'], permutation))
		for depth in range(MAX_DEPTH+1):
			cube.reset()
			cube.position = cube.apply_scramble(depth)
			solution = solver.solve(depth)
			if depth != 0:
				self.assertNotEqual(solution, '')
			for move in solution.split():
				cube.position = cube.make_move(move)
			self.assertTrue(cube.is_solved())

if __name__ == "__main__":
	unittest.main()