'''
Created on 12.12.2021

@author: pucgenie+aoc212@gmail.com
'''
from statistics import mean
from math import floor, ceil

def int_natural(n):
	if n[0] == '-':
		raise ValueError("Unexpected input")
	return int(n)

if __name__ == '__main__':
	def do_it(crab_depths, args,):
		# we will need it often
		crab_depths = tuple(cd for cd in crab_depths)
		
		from time import process_time_ns
		full_cpu = process_time_ns()
		
		ideal_depth = min(crab_depths)
		perfect_depth = mean(crab_depths)
		
		def fuel_consumpt(depth):
			return sum(n*(n+1)/2 for n in (abs(depth - cd) for cd in crab_depths))
		
		min_fuel_consumption = fuel_consumpt(ideal_depth)
		for depth in range(ideal_depth + 1, max(crab_depths) + 1):
			test_fuel = fuel_consumpt(depth)
			if test_fuel < min_fuel_consumption:
				min_fuel_consumption = test_fuel
				ideal_depth = depth
		
		from stdout_tools import print_outcome
		print_outcome(
			ideal_depth=ideal_depth,
			perfect_depth=perfect_depth,
			fuel_consumpt=min_fuel_consumption,
			perfect_fuel_consumpt=fuel_consumpt(perfect_depth),
			fuel_floor= fuel_consumpt(floor(perfect_depth)),
			fuel_ceil= fuel_consumpt(ceil(perfect_depth)),
			full_cpu=process_time_ns() - full_cpu,
		)
	
	from linebased_main import linebased_main
	linebased_main(
		"#7 The Treachery Of Whales",
		do_it,
		example_data=(
			16,1,2,0,4,2,7,1,2,14,
		),
		data_url='https://adventofcode.com/2021/day/7/input',
		data_parser=int_natural,
		split_char=',',
		#argparse_extras=lambda parser : parser.add_argument('--days', type=int, default=256, help="""Count of days to simulate.""",)
	)
