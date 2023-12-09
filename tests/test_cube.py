from .context import rubik_solver
from .context import available_moves

import numpy as np
import unittest


benchmark_scrambles = [
("F' D U' L2 B2 D2 B2 D B F U L2 R2 B2 U' L F' D U2 F' D2 U L U' B' U' B2 U R2 U",
	np.array([ 1, 2, 0, 1, 2, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1]),
	np.array([ 7, 1, 4, 3, 2, 6, 5, 0,19, 8,15,12,17,16,18,11,14,13, 9,10])),
("U B2 D F2 D R B' R' D B D2 F R D' F R D2 L' B' D U' R B2 D B2 R U' F2 D' R2",
	np.array([ 0, 0, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0]),
	np.array([ 0, 6, 7, 1, 2, 4, 5, 3, 18,13,15,10,17,14,19,11,16, 9, 8,12])),
("D' F2 L2 B2 L B D2 F L2 D2 U2 B2 F2 L R' D U2 L2 U L' U L F' R' F U' B2 F2 L' R'",
	np.array([ 2, 1, 2, 1, 1, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0]),
	np.array([ 7, 4, 5, 1, 3, 2, 0, 6,16, 9,19,18, 8,10,17,15,13,11,12,14])),
("D2 L' D R F R' D' U' R' U2 R' D F2 D U L' F' D' L2 U' B' F' D2 B' L2 U2 B D' U2 L'",
	np.array([ 0, 1, 1, 0, 2, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0]),
	np.array([ 2, 6, 4, 0, 3, 7, 5, 1,18,15,19,10, 9,12,13, 8,11,17,16,14])),
("U L2 B F L2 D' U' B D' B2 F' L2 R' F' L R2 F R' U B L2 F' U2 L D U' L2 R' B2 L",
	np.array([ 0, 1, 1, 0, 2, 0, 2, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]),
	np.array([ 7, 0, 6, 5, 4, 1, 2, 3,18,19, 8,15,11,14,12,13,10,16,17, 9]))]

class TestCube(unittest.TestCase):
	def test_cube(self):
		cube = rubik_solver.Cube()
		self.assertTrue(cube.is_solved())
		self.assertEqual(cube.scramble, None)
		for scramble, orientation, permutation in benchmark_scrambles:
			cube = rubik_solver.Cube(scramble)
			self.assertFalse(cube.is_solved())
			self.assertTrue(np.array_equal(cube.position['orientation'], orientation))
			self.assertTrue(np.array_equal(cube.position['permutation'], permutation))
			cube.reset()
			cube.position = cube.apply_scramble(scramble)
			self.assertFalse(cube.is_solved())
			self.assertTrue(np.array_equal(cube.position['orientation'], orientation))
			self.assertTrue(np.array_equal(cube.position['permutation'], permutation))
		for i in range(100):
			cube = rubik_solver.Cube(i)
			if i == 0:
				self.assertTrue(cube.is_solved())
			else:
				self.assertFalse(cube.is_solved())
			self.assertEqual(len(cube.scramble.split()), i)
		self.assertTrue(cube.is_solved(rubik_solver.Cube().position))
		for move in available_moves[None]:
			tmp1 = cube.make_move(move)
			tmp2 = cube.make_move(move, rubik_solver.Cube().position)
			self.assertFalse(np.array_equal(tmp1['orientation'], tmp2['orientation']))
			self.assertFalse(np.array_equal(tmp1['permutation'], tmp2['permutation']))

if __name__ == "__main__":
	unittest.main()