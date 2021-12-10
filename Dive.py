'''
Created on 09.12.2021

@author: pucgenie+aoc212@gmail.com
'''
from typing import Iterable
from enum import Enum

submarine = {
	's': 0,
	'd': 0,
}

# should use namedtuple?
class Axis(Enum):
	forward = ('s', +1)
	down = ('d', +1)
	up = ('d', -1)
	

def parse_sane_command_lines(line):
	if len(line) > 32:
		print(len(line))
		#print(line)
		raise ValueError("Unexpectedly large input, aborting.")
	line = line.split()
	if len(line) > 2:
		print(len(line))
		raise ValueError("Too many tokens, aborting.")
	return (Axis[line[0]], int(line[1]),)

def move_submarine_path(
		commands: Iterable,
		# nothing special
	) -> int:
	for command in commands:
		submarine[command[0].value[0]] += command[0].value[1] * command[1]
	return submarine['s'] * submarine['d']



if __name__ == '__main__':
	from stdout_tools import *
	def argparse_extras(parser):
		pass #parser.add_argument('--window_size', type=int, default=3, help="""Sliding window size. 1 would allow calculating part 1.""",)
	def do_it(provider, args,):
		print_outcome(vector=move_submarine_path(
			provider,
			# nothing special
		))
	from linebased_main import linebased_main
	linebased_main(
		"#2 Dive part 1",
		do_it,
		example_data=[
			(Axis.forward, 5,),
			(Axis.down, 5,),
			(Axis.forward, 8,),
			(Axis.up, 3,),
			(Axis.down, 8,),
			(Axis.forward, 2,),
		],
		data_url='https://adventofcode.com/2021/day/2/input',
		data_parser=parse_sane_command_lines,
		argparse_extras=argparse_extras,
	)
