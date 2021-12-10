'''
Created on 10.12.2021

@author: pucgenie+aoc212@gmail.com
'''

# example data word width hack
length_per_line = [None,]

def parse_sane_command_lines(line):
	if len(line) > 16:
		print(len(line))
		#print(line)
		raise ValueError("Unexpectedly large input, aborting.")
	# Try to parse as binary number. If this fails, abort operation.
	int(line, 2,)
	
	line_length = len(line)
	if length_per_line[0]:
		if line_length != length_per_line[0]:
			raise ValueError("Unexpected input format.")
	else:
		print(f"Encountered length of {line_length}")
		length_per_line[0] = line_length
	return line

def bits_to_int(bitlist):
	ret = 0
	place_value = 1
	bitlist.reverse()
	for bit in bitlist:
		if bit:
			ret += place_value
		place_value = place_value * 2
	return ret

if __name__ == '__main__':
	from stdout_tools import *
	def argparse_extras(parser):
		pass #parser.add_argument('--window_size', type=int, default=3, help="""Sliding window size. 1 would allow calculating part 1.""",)
	def do_it(provider, args,):
		gamma_digit_count =   None
		# You may think: Just invert the gamma rate. So tell me how to do it simpler than maintaining the inverse operation chain addition.
		epsilon_digit_count = None
		
		# We get to know the length_per_line when peeking the first line/word.
		first_element = True
		num_elements = 0
		for binstr in provider:
			if first_element:
				gamma_digit_count =   [0] * length_per_line[0]
				epsilon_digit_count = [0] * length_per_line[0]
				first_element = False
			for i in range(length_per_line[0]):
				if binstr[i] == '1':
					gamma_digit_count[i] += 1
				else:
					epsilon_digit_count[i] += 1
			num_elements += 1
		
		majority_req = num_elements / 2
		
		gamma_rate = [False] * length_per_line[0]
		epsilon_rate = [False] * length_per_line[0]
		for i in range(length_per_line[0]):
			gamma_rate[i] = gamma_digit_count[i] > majority_req
			epsilon_rate[i] = epsilon_digit_count[i] > majority_req
		
		print(f"gamma: count={gamma_digit_count}, {gamma_rate}")
		print(f"epsilon: count={epsilon_digit_count}, {epsilon_rate}")
		gamma_rate = bits_to_int(gamma_rate)
		epsilon_rate = bits_to_int(epsilon_rate)
		
		print_outcome(
			gamma_rate=gamma_rate,
			epsilon_rate=epsilon_rate,
			majority_req=majority_req,
			power_consumption=gamma_rate * epsilon_rate,
		)
	from linebased_main import linebased_main
	linebased_main(
		"#3 Binary Diagnostic part 1",
		do_it,
		example_data=[
			'00100',
			'11110',
			'10110',
			'10111',
			'10101',
			'01111',
			'00111',
			'11100',
			'10000',
			'11001',
			'00010',
			'01010',
		],
		data_url='https://adventofcode.com/2021/day/3/input',
		data_parser=parse_sane_command_lines,
		argparse_extras=argparse_extras,
		parse_example_data=True,
	)
