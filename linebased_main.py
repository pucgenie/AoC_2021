'''
Created on 09.12.2021

@author: pucgenie+aoc212@gmail.com
'''
def apply_filters(data_filter, data_parser, content_lines,):
	if data_filter:
		content_lines = filter(data_filter, content_lines,)
	if data_parser:
		content_lines = map(data_parser, content_lines,)
	return content_lines

def linebased_main(puzzle_name, do_it, example_data=None,
		data_filter=None, data_parser=None, data_url=None, parse_example_data=False,
		argparse_extras=None, split_char=None,
	):
	import argparse
	parser = argparse.ArgumentParser(description=f"Advent of Code 2021, {puzzle_name}", formatter_class=argparse.ArgumentDefaultsHelpFormatter,)
	parser.add_argument('--session', type=str, metavar="cookie", help="Session cookie to use when gathering input data. If omitted, example values are used.")
	if argparse_extras:
		argparse_extras(parser)
	args = parser.parse_args()
	
	if not args.session:
		print("mode: test")
		content_lines = example_data
		if parse_example_data:
			content_lines = apply_filters(data_filter, data_parser, content_lines,)
		do_it(
			content_lines,
			args=args,
		)
		exit(16)
		raise BaseException("It's the end of the universe.")
	# https://docs.python.org/3/library/urllib.request.html recommends requests module instead, so...
	import requests
	with requests.get(data_url, timeout=5, cookies={'session': args.session,}) as content:
		content_lines = apply_filters(data_filter, data_parser, content.text.split(split_char) if split_char else content.text.splitlines(),)
		do_it(
			content_lines,
			args=args,
		)
