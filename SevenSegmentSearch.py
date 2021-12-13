'''
Created on 12.12.2021

@author: pucgenie+aoc212@gmail.com
'''

from collections import Counter

def split_data(n):
	analysis, cipher = n.split(' | ')
	return (sorted(analysis.split(), key=lambda x : len(x)), cipher.split(),)
	

class SSDigitMeta(object):
	LENGTHS = (6, 2, 5, 5, 4, 5, 6, 3, 7, 6,)
	SURE    = {2: 1, 3: 7, 4: 4, 7: 8,}

if __name__ == '__main__':
	def do_it(lines, args,):
		digit_count = Counter()
		
		from time import process_time_ns
		full_cpu = process_time_ns()
		
		count_ofse = 0
		for analysis, cipher, in lines:
			for scrambled in cipher:
				if len(scrambled) in SSDigitMeta.SURE:
					count_ofse += 1
		
		
		from stdout_tools import print_outcome
		print_outcome(
			digit_count=digit_count,
			count_ofse=count_ofse,
			full_cpu=process_time_ns() - full_cpu,
		)
	
	from linebased_main import linebased_main
	linebased_main(
		"#8 Seven Segment Search",
		do_it,
		example_data=(
			'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
			'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc    ',
			'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg         ',
			'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb   ',
			'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea   ',
			'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb  ',
			'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe  ',
			'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef    ',
			'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb       ',
			'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce      ',
		),
		data_url='https://adventofcode.com/2021/day/8/input',
		data_parser=split_data,
		parse_example_data=True,
		#argparse_extras=lambda parser : parser.add_argument('--days', type=int, default=256, help="""Count of days to simulate.""",)
	)
