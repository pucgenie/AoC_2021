'''
Created on 12.12.2021

@author: pucgenie+aoc212@gmail.com
'''

from collections import Counter
from string import ascii_lowercase
from typing import Set, Iterable

def split_data(n: str):
	analysis, cipher = n.split(' | ')
	return (tuple(map(set, sorted(analysis.split(), key=len,))), tuple(map(set, cipher.split(),)),)
	
SEVENSEGMENT = {
	0: set('abcefg'),
	1: set('cf'),
	2: set('acdeg'),
	3: set('acdfg'),
	4: set('bcdf'),
	5: set('abdfg'),
	6: set('abdefg'),
	7: set('acf'),
	8: set('abcdefg'),
	9: set('abcdfg'),
}

# alternative approach
#NORM_D  = {
#	0: 0b1110111,
#	1: 0b0010010,
#	2: 0b1011101,
#	3: 0b1011011,
#	4: 0b0111010,
#	5: 0b1101011,
#	6: 0b1101111,
#	7: 0b1010010,
#	8: 0b1111111,
#	9: 0b1111011,
#}

class SSDigitMeta(object):

	def __init__(self, segmentmap: dict,):
		self.segmentmap = segmentmap
		self.lengths = tuple(map(len, segmentmap.values(),))
		self.mapping = {i:set('abcdefg') for i in range(10)}
		self.wiring = {l:set('abcdefg') for l in ascii_lowercase[0:7]}
		self.known_wires = set()
		self.finished_wires = set()
		self.sure = {n:z for z, chars, in segmentmap.items() for n, oc, in Counter(self.lengths).most_common() if oc == 1 if len(chars) == n}
		self.counts = Counter()
		for segments in segmentmap.values():
			self.counts.update(segments)
	
	def decode_digit(self, cipher: Set,):
		return [i for i, k in self.mapping.items() if not cipher.difference(k)][0]
	
	def decode_number(self, ciphers: Iterable,):
		ret = 0
		for cipher in ciphers:
			ret *= 10
			ret += self.decode_digit(cipher)
		return ret
	
	def find_unique_wire_hole(self, analysis: Iterable,):
		wire_counts = Counter()
		for segments in analysis:
			wire_counts.update(segments)
		n_segments = len(self.counts)
		seldom_segment_counts = self.counts.most_common(2)
		if n_segments - seldom_segment_counts[0][1] == 1 and n_segments - seldom_segment_counts[1][1] > 1:
			# should find the 'f' wire
			wire = seldom_segment_counts[0][0]
			lonely_wire = wire_counts.most_common(1)[0][0]
			self.wiring[wire] = set(lonely_wire)
			self.known_wires.add(lonely_wire)
			self.finished_wires.add(wire)
			for impossibles in self.wiring.values():
				if len(impossibles) == 1 and lonely_wire in impossibles:
					continue
				impossibles.remove(lonely_wire)
		else:
			print("No unique wire-hole found.")
	
	def rewire(self):
		reloop = True
		while reloop:
			reloop = False
			for digit, wires, in self.mapping.items()[:]:
				unknown_wires = wires - self.known_wires
				if len(unknown_wires) != 1:
					continue
				the_wire = next(iter(unknown_wires))
				should_wire = next(iter(self.segmentmap[digit] - self.finished_wires))
				self.wiring[should_wire] = set(the_wire)
				self.known_wires.add(the_wire)
				self.finished_wires.add(should_wire)
				reloop = True


if __name__ == '__main__':
	def do_it(lines, args,):
		from time import process_time_ns
		full_cpu = process_time_ns()
		
		numbers = []
		for analysis, ciphers, in lines:
			meta = SSDigitMeta(SEVENSEGMENT)
			meta.find_unique_wire_hole(analysis)
			for scrambled in analysis:
				sure_mapping = meta.sure.get(len(scrambled))
				if sure_mapping:
					meta.mapping[sure_mapping] = scrambled
					for wire in scrambled:
						meta.wiring[wire] &= meta.segmentmap[sure_mapping]
			meta.rewire()
			for map_d in meta.mapping.items():
				print(map_d)
			for wire in meta.wiring.items():
				print(wire)
			print(meta.sure)
			break
			
			numbers.append(meta.decode_number(ciphers))
			print()
		
		from stdout_tools import print_outcome
		print_outcome(
			sum=sum(numbers),
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
