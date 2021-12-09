'''
Created on 09.12.2021

@author: pucgenie+aoc212@gmail.com
'''

def print_outcome(**kwargs):
	"""
	Prints YAML-style structured single-level output.
	"""
	for key in kwargs:
		print(f"""{key}: {kwargs[key]}""")
