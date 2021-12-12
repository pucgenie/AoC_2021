'''
Created on 12.12.2021

@author: pucgenie+aoc212@gmail.com
'''

def int_positive(n):
	if n == '0':
		raise ValueError("Unexpected input")
	return int(n)

if __name__ == '__main__':
	def do_it(fish, args,):
		days = args.days
		del args
		
		# not using len(fish) so that streaming will be possible - although useless in this application.
		fish_sum = 0
		#born_at_day = [0] * days
		from collections import Counter
		successors = Counter()
		for z in fish:
			# On the first day there were born some fish that were almost able to give birth again
			#born_at_day[0] += 1
			fish_sum += 1
			successors[z] += 1
		del fish
		
		from time import process_time_ns
		full_cpu = process_time_ns()
		#timings = []
		#loop_count = 0
		while successors:
			#loop_count += 1
			#print(*successors.most_common(1))
			swarms = tuple(successors.items())
			successors.clear()
			#start_cpu = process_time_ns()
			for day, n_fish, in swarms:
				for future_day in range(day, days, 7,):
					#born_at_day[future_day] += n_fish
					fish_sum += n_fish
					successors[future_day + 9] += n_fish
			#timings.append(process_time_ns() - start_cpu)
		
		from stdout_tools import print_outcome
		print_outcome(
			count=fish_sum, #sum(born_at_day),
			#cpu_per_swarm=sum(timings)/len(timings),
			#cpu_min=min(timings),
			#cpu_max=max(timings),
			#loop_count=len(timings),
			full_cpu=process_time_ns() - full_cpu,
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
		argparse_extras=lambda parser : parser.add_argument('--days', type=int, default=1000, help="""Count of days to simulate.""",)
	)
