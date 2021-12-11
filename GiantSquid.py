'''
Created on 10.12.2021

@author: pucgenie+aoc212@gmail.com
'''

def_rows = 5
def_cols = 5
f_newline = "\n"

from os import linesep
class Board(object):
	def __init__(self, lines,):
		if len(lines) != def_rows:
			raise ValueError(f"Rows allowed: {def_rows}, rows provided: {len(lines)}")
		for row in lines:
			if len(row) != def_cols:
				raise ValueError(f"Columns allowed: {def_cols}, rows provided: {len(row)}")
		self.lines = lines
		self.markmap = [[False] * def_cols for _ in range(def_rows)]
	
	def mark(self, z,):
		for rowIdx, row in enumerate(self.lines):
			try:
				colIdx = row.index(z)
				self.markmap[rowIdx][colIdx] = True
			except ValueError:
				pass
	
	def is_bingo(self):
		for rowIdx, row in enumerate(self.markmap):
			if all(row):
				print(f"Bingo, row {rowIdx}")
				return True
		for colIdx, column in enumerate(zip(*self.markmap)):
			if all(column):
				print(f"Bingo, column {colIdx}, {column}")
				return True
		return False
	
	def calc_score(self):
		# zipping that often may hurt performance, but using indices would be more error-prone.
		return sum(
			z[0]
			for row in zip(self.lines, self.markmap,) # join numbers with markmap
			for z in zip(row[0], row[1],) # join each number in row to its markmap bit
			if z[1] == False # non-marked number
		)
	
	def __str__(self, *args, **kwargs):
		ret = []
		for line in self.lines:
			ret.append(" ".join([f"{n:>2}" for n in line]))
		return "\n".join(ret)

from typing import List
class Bingo(BaseException):
	def __init__(self, winners: List, win_num: int,):
		self.winners = winners
		self.win_num = win_num
	
	def __str__(self, *args, **kwargs):
		return f"Bingo-Boards:\n{f_newline.join((f'{board.calc_score() * self.win_num}{f_newline}{str(board)}{f_newline}' for board in self.winners))}"

if __name__ == '__main__':
	from stdout_tools import *
	def argparse_extras(parser):
		pass #parser.add_argument('--window_size', type=int, default=3, help="""Sliding window size. 1 would allow calculating part 1.""",)
	def do_it(provider, args,):
		data_iter = iter(provider)
		header = [int(z, 10,) for z in next(data_iter).split(',')]
		
		def parse_board(data_iter,):
			lines = []
			for i in range(def_rows):
				lines.append([int(z, 10,) for z in next(data_iter).split()])
			return Board(lines)
		
		boards = []
		for rawline in data_iter:
			if rawline != '':
				raise ValueError("Unexpected format.")
			boards.append(parse_board(data_iter))
		
		winners = []
		try:
			for z in header:
				print(f"Next number: {z}")
				# We'd like to remove elements while checking all boards so make a copy of the boards list.
				for board in boards[:]:
					board.mark(z)
					if board.is_bingo():
						winners.append(board)
						boards.remove(board)
				if len(winners) > 0:
					bingoX = Bingo(winners, z,)
					# added the if for part 2
					if len(boards) > 0:
						print(bingoX)
						winners.clear()
					else:
						raise bingoX
		except Bingo as bingo:
			print(bingo)
	from linebased_main import linebased_main
	linebased_main(
		"#4 Giant Squid",
		do_it,
		example_data=[
			'7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1',
      '',
			'22 13 17 11  0',
			' 8  2 23  4 24',
			'21  9 14 16  7',
			' 6 10  3 18  5',
			' 1 12 20 15 19',
			'',
			' 3 15  0  2 22',
			' 9 18 13 17  5',
			'19  8  7 25 23',
			'20 11 10 24  4',
			'14 21 16 12  6',
			'',
			'14 21 17 24  4',
			'10 16 15  9 19',
			'18  8 23 26 20',
			'22 11 13  6  5',
			' 2  0 12  3  7',
		],
		data_url='https://adventofcode.com/2021/day/4/input',
		argparse_extras=argparse_extras,
		parse_example_data=True,
	)
