'''
Created on 10.12.2021

@author: pucgenie+aoc212@gmail.com
'''
from enum import Enum

class CallableEnum(Enum):
	"""
	https://www.linuxtut.com/en/49cbf3237fd4bc5f93ed/
Inherit this class to create a Callable Enum
	"""
	def __call__(self, *args,**kwargs):
		return self.value[0](*args,**kwargs)

def register(func):
	"""
Decorator to easily define tuples that contain functions
	"""
	return func
