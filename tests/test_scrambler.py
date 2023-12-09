from .context import rubik_solver

import unittest


N_SCRAMBLES = 100
N_MOVES = 100

class TestScrambler(unittest.TestCase):
	def test_scrambler(self):
		for _ in range(N_SCRAMBLES):
			scramble_list = rubik_solver.generate_random_scramble(N_MOVES).split()
			for i in range(len(scramble_list)-1):
				self.assertFalse(scramble_list[i][0] == scramble_list[i+1][0])
				self.assertFalse(scramble_list[i][0] == 'D' and scramble_list[i+1][0] == 'U')
				self.assertFalse(scramble_list[i][0] == 'L' and scramble_list[i+1][0] == 'R')
				self.assertFalse(scramble_list[i][0] == 'B' and scramble_list[i+1][0] == 'F')

if __name__ == "__main__":
	unittest.main()