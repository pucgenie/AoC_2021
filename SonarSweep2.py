'''
Created on 09.12.2021

@author: pucgenie+aoc212@gmail.com
'''
from typing import Iterable

def parse_sane_int_lines(line):
	if len(line) > 8:
		print(len(line))
		#print(line)
		raise ValueError("Unexpectedly large input, aborting.")
	return int(line)

def count_increases(levels: Iterable, window_size: int,) -> int:
	levels_iter = iter(levels)
	from collections import deque
	from itertools import islice
	current_window = deque(islice(levels_iter, window_size,), maxlen=window_size,)
	# first window exceptional behaviour
	current_level = sum(current_window)
	#print(f"{current_level} (N/A - no previous sum)")
	count_increased = 0
	for read_level in levels_iter:
		current_window.append(read_level)
		sum_level = sum(current_window)
		#direction = "no change"
		if sum_level > current_level:
			count_increased += 1
			#direction = "increased"
		#elif sum_level < current_level:
			#direction = "decreased"
		current_level = sum_level
		#print(f"{current_level} ({direction})")
		#print(current_window)
	return count_increased



if __name__ == '__main__':
	from stdout_tools import *
	window_size = 3
	def argparse_extras(parser):
		parser.add_argument('--window_size', type=int, default=3, help="""Sliding window size. 1 would allow calculating part 1.""",)
	def do_it(provider, args,):
		print_outcome(count_increased=count_increases(provider, args.window_size,))
	from linebased_main import linebased_main
	linebased_main(
		"#1 Sonar Sweep part 2",
		do_it,
		example_data=[
			199,
			200,
			208,
			210,
			200,
			207,
			240,
			269,
			260,
			263,
			100,
		],
		data_url='https://adventofcode.com/2021/day/1/input',
		data_parser=parse_sane_int_lines,
		argparse_extras=argparse_extras,
	)
