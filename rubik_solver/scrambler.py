from .defs import available_moves

import random


def generate_random_scramble(num_moves):
	scramble = []
	last_move = None
	for _ in range(num_moves):
		last_move = random.choice(available_moves[last_move])
		scramble.append(last_move)
	return ' '.join(scramble).replace('1', '').replace('3', "'")