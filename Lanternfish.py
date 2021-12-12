'''
Created on 12.12.2021

@author: pucgenie+aoc212@gmail.com
'''
from collections import Counter

def int_positive(n):
	if n == '0':
		raise ValueError("Unexpected input")
	return int(n)

if __name__ == '__main__':
	def do_it(fish, args,):
		days = args.days
		del args
		
		born_at_day = [0] * days
		successors = Counter()
		for z in fish:
			# On the first day there were born some fish that were almost able to give birth again
			born_at_day[0] += 1
			successors[z] += 1
		
		def fish_thread(startday, n_fish,):
			for future_day in range(startday, days, 7,):
				born_at_day[future_day] += n_fish
				successors[future_day + 9] += n_fish
		
		while successors:
			swarms = list(successors.items())
			successors.clear()
			for day, n_fish, in swarms:
				fish_thread(day, n_fish,)
		
		from stdout_tools import print_outcome
		print_outcome(
			count=sum(born_at_day),
			#successors=successors,
		)
	
	from linebased_main import linebased_main
	linebased_main(
		"#6 Lanternfish part 2",
		do_it,
		example_data=(
			3,4,3,1,2,
		),
		data_url='https://adventofcode.com/2021/day/6/input',
		data_parser=int_positive,
		split_char=',',
		argparse_extras=lambda parser : parser.add_argument('--days', type=int, default=256, help="""Count of days to simulate.""",)
	)
