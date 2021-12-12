'''
Created on 12.12.2021

@author: pucgenie+aoc212@gmail.com
'''
def int_positive(n):
	if n == '0':
		raise ValueError("Unexpected input")
	return int(n)

def parse_sane_input(line):
	return (int_positive(n) for n in line.split(','))

if __name__ == '__main__':
	def do_it(data_in, args,):
		fish = list(*data_in)
		for _ in range(80):
			num_zeroes = 0
			for i in range(len(fish)):
				# can't use %7 because of 8.
				predecessor = (fish[i] - 1)
				if predecessor == -1:
					predecessor = 6
					num_zeroes += 1
				fish[i] = predecessor
			while num_zeroes > 0:
				fish.append(8)
				num_zeroes -= 1
			#print(fish)
		
		from stdout_tools import print_outcome
		print_outcome(
			count=len(fish),
			#bitmap=bitmap,
		)
	
	from linebased_main import linebased_main
	linebased_main(
		"#6 Lanternfish",
		do_it,
		example_data=(
			'3,4,3,1,2',
		),
		data_url='https://adventofcode.com/2021/day/6/input',
		data_parser=parse_sane_input,
		parse_example_data=True,
	)
