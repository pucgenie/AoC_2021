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

def print_outcome(**kwargs):
	"""
	Prints YAML-style structured single-level output.
	"""
	for key in kwargs:
		print(f"""{key}: {kwargs[key]}""")

def do_it(provider: Iterable,):
	print_outcome(count_increased=count_increases(provider))


if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser(description="Advent of Code 2021, #1 Sonar Sweep")
	parser.add_argument('--session', type=str, metavar="cookie", help="Session cookie to use when gathering input data. If omitted, example values are used.")
	args = parser.parse_args()
	
	count_increased = None
	if not args.session:
		print("mode: test")
		do_it([
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
		])
		exit(16)
		raise BaseException("It's the end of the universe.")
	# https://docs.python.org/3/library/urllib.request.html recommends requests module instead, so...
	import requests
	with requests.get('https://adventofcode.com/2021/day/1/input', timeout=5, cookies={'session': args.session,}) as content:
		do_it(
			map(parse_sane_int_lines, content.text.splitlines())
		)
	#count_increased = fetch_and_process_data(count_increases)
