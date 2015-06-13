#!/usr/bin/env python
"""
	This module includes Bond class which is a subclass of the Item class.

	Purpose of the module to learn how to use 
	inheritance and polymorphizm in the python. 
	Its free to use and change.

	writen by Mustafa ALP.
	16.06.2015
"""

import random as ra
from Item import Item

#		
#		
#	object		
#		
#		
class Bond(Item):
	"""
		subclass Bond derived from Item superclass

		purpose of the Bond class:
		to learn inheritance and polymorphizm in python
	"""
	def __init__(self):
		super(Bond, self).__init__()
		self._name = 'bond'

#
#	object property
#			
	def name():
	    doc = """The name property, keeps name of the Item and can't be changed"""
	    def fget(self):
	        return self._name
	    return locals()
	name = property(**name())
		
#
#	object static method
#		
	@staticmethod
	def setWorth():
		"""changes worth of Bond items"""
		Bond._worth = ra.randint(25, 75)

#
#	object static method
#		
	@staticmethod
	def worth():
		"""@return worth of Bond items"""	
		return Bond._worth
