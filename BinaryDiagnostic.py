'''
Created on 10.12.2021

@author: pucgenie+aoc212@gmail.com
'''

# example data word width hack
length_per_line = [None,]

def parse_sane_data_lines(line):
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
	"""
	Could be optimized to use place_value=2^(length_per_line-1) and /2 instead of *2 - to not have to reverse the input list.
	"""
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
		level = 0
		def sort_xsb(srclist, level,):
			ret = [[], [],]
			for binstr in srclist:
				ret[1 if binstr[level] == '1' else 0].append(binstr)
			return ret
		
		# now we don't have any chance to stream-process everything. Needs memory.
		highlow = sort_xsb(provider, level,)
		level += 1
		del provider
		
		def majority(lists):
			return 1 if len(lists[1]) >= len(lists[0]) else 0
		
		einser = majority(highlow)
		nuller = 1 - einser
		
		highs = highlow[einser]
		lows = highlow[nuller]
		del highlow, einser, nuller
		
		for lv_x in range(level, length_per_line[0],):
			if len(highs) > 1:
				highs = sort_xsb(highs, lv_x,)
				highs = highs[majority(highs)]
			if len(lows) > 1:
				lows = sort_xsb(lows, lv_x,)
				lows = lows[1 - majority(lows)]
			
		oxygen_gr = int(highs[0], 2,)
		co2_sr = int(lows[0], 2,)

		print_outcome(
			oxygen_gr=oxygen_gr,
			co2_sr=co2_sr,
			life_sr=oxygen_gr * co2_sr,
		)
	from linebased_main import linebased_main
	linebased_main(
		"#3 Binary Diagnostic part 2",
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
		data_parser=parse_sane_data_lines,
		argparse_extras=argparse_extras,
		parse_example_data=True,
	)
