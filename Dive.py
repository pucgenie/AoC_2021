'''
Created on 09.12.2021

@author: pucgenie+aoc212@gmail.com
'''
from typing import Iterable
from enum import Enum, auto

class Submarine(object):
	def __init__(self):
		self.depth = 0
		self.aim = 0
		self.horizontal_position = 0
	
	def down(self, units,):
		self.aim += units
	
	def up(self, units,):
		self.aim -= units
	
	def forward(self, units,):
		self.horizontal_position += units
		self.depth += self.aim * units
	
	def move_submarine_path(self,
			commands: Iterable,
			# nothing special
		) -> int:
		for command in commands:
			# guarded by Enum validation
			getattr(self, command[0].name)(command[1])

class Axis(Enum):
	forward = auto()
	down = auto()
	up = auto()

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



if __name__ == '__main__':
	from stdout_tools import *
	def argparse_extras(parser):
		pass #parser.add_argument('--window_size', type=int, default=3, help="""Sliding window size. 1 would allow calculating part 1.""",)
	def do_it(provider, args,):
		submarine = Submarine()
		submarine.move_submarine_path(
			provider,
			# nothing special
		)
		print_outcome(vector=submarine.horizontal_position * submarine.depth)
	from linebased_main import linebased_main
	linebased_main(
		"#2 Dive part 2",
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
