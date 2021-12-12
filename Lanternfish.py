'''
Created on 12.12.2021

@author: pucgenie+aoc212@gmail.com
'''
from _collections import deque
def int_positive(n):
	if n == '0':
		raise ValueError("Unexpected input")
	return int(n)

if __name__ == '__main__':
	def do_it(fish, args,):
		days = args.days
		del args
		
		born_at_day = [0] * days
		successors = deque()
		for z in fish:
			# On the first day there were born some fish that were almost able to give birth again
			born_at_day[0] += 1
			for future_day in range(z, days, 7,):
				born_at_day[future_day] += 1
				successors.append(future_day)
		while successors:
			print(len(successors))
			for future_day in range(successors.pop() + 9, days, 7,):
				born_at_day[future_day] += 1
				successors.append(future_day)
		
		from stdout_tools import print_outcome
		print_outcome(
			count=sum(born_at_day),
			#bitmap=bitmap,
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
