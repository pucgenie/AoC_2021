'''
Created on 12.12.2021

@author: pucgenie+aoc212@gmail.com
'''

class Line(object):
	MAX_X = 1000
	MAX_Y = 1000
	STROKE = 1
	
	@classmethod
	def check_window_size(a, b,):
		if a[0] > Line.MAX_X:
			Line.MAX_X = a[0]
		if b[0] > Line.MAX_X:
			Line.MAX_X = b[0]
		if a[1] > Line.MAX_Y:
			Line.MAX_X = a[1]
		if b[1] > Line.MAX_Y:
			Line.MAX_X = b[1]
	
	def __init__(self, a, b,):
		self.a = a
		self.b = b
		# would be needed for dynamic sizing
		#Line.check_window_size(a, b,)
	
	def draw_onto(self, bitmap,):
		"""
		Doesn't work for all angles, but 45° steps are ok.
		"""
		x_distance = self.b[0] - self.a[0]
		y_distance = self.b[1] - self.a[1]
		x_direction = 1 if x_distance > 0 else 0 if x_distance == 0 else -1
		y_direction = 1 if y_distance > 0 else 0 if y_distance == 0 else -1
		
		x = self.a[0]
		y = self.a[1]
		
		if x_direction != 0:
			x_end = self.b[0] + Line.STROKE * (1 if x_direction >= 0 else -1)
			x_step, x_i = (x_distance * x_direction) / (y_distance * y_direction) if y_distance != 0 else -1, 0
			while x != x_end:
				# swap x and y for simpler console output
				bitmap[y][x] += 1
				x += x_direction
				x_i += 1
				if x_i >= x_step:
					y += y_direction
					x_i = 0
		elif y_direction != 0:
			y_end = self.b[1] + Line.STROKE * (1 if y_direction >= 0 else -1)
			y_step, y_i = (y_distance * y_direction) / (x_distance * x_direction) if x_distance != 0 else -1, 0
			while y != y_end:
				# swap x and y for simpler console output
				bitmap[y][x] += 1
				y += y_direction
				y_i += 1
				if y_i >= y_step:
					x += x_direction
					y_i = 0
		else:
			# supports "dots"
			bitmap[y][x] += 1

def parse_sane_lines(line):
	if len(line) > 18:
		raise ValueError(f"Unexpectedly large ({len(line)} characters) input, aborting.")
	line = line.split(' -> ')
	return Line(
		[int(n) for n in line[0].split(',')],
		[int(n) for n in line[1].split(',')],
	)

if __name__ == '__main__':
	def do_it(data_in, args,):
		# part 1 restriction. Could use filter but genexps look more pythonic.
		#data_in = (line for line in data_in if (line.a[0] == line.b[0]) or (line.a[1] == line.b[1]))
		
		# check all intersections or use a bitmap? If in doubt, STREAM: bitmap.
		# dynamically grow it?
		#bitmap = list(list())
		# remember to not re-use that one literal Y list if not using a list comprehension - which leaves us with:
		bitmap = [[0] * Line.MAX_Y for _ in range(Line.MAX_X)]
		for line in data_in:
			line.draw_onto(bitmap)
		
		count = sum(1 for sublist in bitmap for item in sublist if item >= 2)
		
		
		from stdout_tools import print_outcome
		print_outcome(
			count=count,
			#bitmap=bitmap,
		)
	
	from linebased_main import linebased_main
	linebased_main(
		"#5 Hydrothermal Venture",
		do_it,
		example_data=(
			'0,9 -> 5,9',
			'8,0 -> 0,8',
			'9,4 -> 3,4',
			'2,2 -> 2,1',
			'7,0 -> 7,4',
			'6,4 -> 2,0',
			'0,9 -> 2,9',
			'3,4 -> 1,4',
			'0,0 -> 8,8',
			'5,5 -> 8,2',
		),
		data_url='https://adventofcode.com/2021/day/5/input',
		data_parser=parse_sane_lines,
		parse_example_data=True,
	)
