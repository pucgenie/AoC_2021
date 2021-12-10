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

def count_increases(levels: Iterable) -> int:
	current_level = None
	count_increased = 0
	count_skipped = 0
	for read_level in levels:
		try:
			if read_level > current_level:
				count_increased += 1
		except TypeError as e:
			# at first it is impossible to compare
			count_skipped += 1
		current_level = read_level
	if count_skipped > 1:
		raise ValueError(f"Unexpectedly skipped more than the first line, n={count_skipped}")
	return count_increased



if __name__ == '__main__':
	from stdout_tools import *
	from linebased_main import linebased_main
	linebased_main(
		"#1 Sonar Sweep",
		lambda provider, **kwargs : print_outcome(count_increased=count_increases(provider)),
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
		],
		data_url='https://adventofcode.com/2021/day/1/input',
		data_parser=parse_sane_int_lines,
	)
