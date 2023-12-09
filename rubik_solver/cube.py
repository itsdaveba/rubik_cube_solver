from .scrambler import generate_random_scramble

import numpy as np


class Cube:
	def __init__(self, scramble=None):
		self.reset()
		self.position = self.apply_scramble(scramble)

	def reset(self):
		self.position = dict(
			orientation = np.zeros(20, dtype=np.int),
			permutation = np.arange(20))
		self.coordinates = (0,0,0,0)

	def is_solved(self, position=None):
		if position is None:
			position = self.position
		is_orientation = np.array_equal(position['orientation'], np.zeros(20, dtype=int))
		is_permutation = np.array_equal(position['permutation'], np.arange(20))
		return is_orientation and is_permutation

	def apply_scramble(self, scramble, position=None):
		self.scramble = scramble
		if position is None:
			position = self.position
		if self.scramble is not None:
			if type(self.scramble) == int:
				self.scramble = generate_random_scramble(scramble)
			for move in self.scramble.split():
				position = self.make_move(move, position)
		return position

	def make_move(self, move, position=None):
		if position is None:
			position = self.position
		if move == "U":
			return self._rearrange(position, [2, 0, 3, 1, 9, 11, 8, 10], 0)
		if move == "U2":
			return self._rearrange(position, [3, 2, 1, 0, 11, 10, 9, 8], 0)
		if move == "U'":
			return self._rearrange(position, [1, 3, 0, 2, 10, 8, 11, 9], 0)
		if move == "L":
			return self._rearrange(position, [3, 7, 1, 5, 15, 10, 18, 13], 2)
		if move == "L2":
			return self._rearrange(position, [7, 5, 3, 1, 18, 15, 13, 10], 0)
		if move == "L'":
			return self._rearrange(position, [5, 1, 7, 3, 13, 18, 10, 15], 2)
		if move == "F":
			return self._rearrange(position, [1, 5, 0, 4, 13, 8, 16, 12], 1)
		if move == "F2":
			return self._rearrange(position, [5, 4, 1, 0, 16, 13, 12, 8], 0)
		if move == "F'":
			return self._rearrange(position, [4, 0, 5, 1, 12, 16, 8, 13], 1)
		if move == "R":
			return self._rearrange(position, [4, 0, 6, 2, 12, 17, 9, 14], -2)
		if move == "R2":
			return self._rearrange(position, [6, 4, 2, 0, 17, 14, 12, 9], 0)
		if move == "R'":
			return self._rearrange(position, [2, 6, 0, 4, 14, 9, 17, 12], -2)
		if move == "B":
			return self._rearrange(position, [6, 2, 7, 3, 14, 19, 11, 15], -1)
		if move == "B2":
			return self._rearrange(position, [7, 6, 3, 2, 19, 15, 14, 11], 0)
		if move == "B'":
			return self._rearrange(position, [3, 7, 2, 6, 15, 11, 19, 14], -1)
		if move == "D":
			return self._rearrange(position, [5, 7, 4, 6, 18, 16, 19, 17], 0)
		if move == "D2":
			return self._rearrange(position, [7, 6, 5, 4, 19, 18, 17, 16], 0)
		if move == "D'":
			return self._rearrange(position, [6, 4, 7, 5, 17, 19, 16, 18], 0)

	def _rearrange(self, position, order, modifier):
		tmp1 = [position['orientation'][i] for i in order]
		if modifier != 0:
			tmp1 = np.concatenate((
				[(t + (1 if i == 0 or i == 3 else -1) * np.sign(modifier)) % 3 
				for t, i in zip(tmp1[:4], range(4))],
				[(t + (1 if modifier % 2 == 1 else 0)) % 2
				for t, i in zip(tmp1[4:], range(4))]))
		tmp2 = [position['permutation'][i] for i in order]
		j = 0
		order.sort()
		new_position = dict(orientation=np.copy(position["orientation"]),
			permutation=np.copy(position["permutation"]))
		for i in order:
			new_position['orientation'][i] = tmp1[j]
			new_position['permutation'][i] = tmp2[j]
			j += 1
		return new_position

	def get_coordinates(self, position=None):
		if position is None:
			position = self.position
			
		corner_orientation_index = 0
		corner_permutation_index = 0
		edge_orientation_index = 0
		edge_permutation_index = 0
		
		for i in range(7):
			corner_orientation_index *= 3
			corner_orientation_index += position["orientation"][i]
			
			corner_permutation_index *= 8-i
			for j in range(i+1, 8):
				if position["permutation"][i] > position["permutation"][j]:
					corner_permutation_index += 1
					
		for i in range(8, 19):
			edge_orientation_index *= 2
			edge_orientation_index += position["orientation"][i]
			
			if i != 18:
				edge_permutation_index *= 20-i
				for j in range(i+1, 20):
					if position["permutation"][i] > position["permutation"][j]:
						edge_permutation_index += 1
	
		return corner_orientation_index, corner_permutation_index, edge_orientation_index, edge_permutation_index