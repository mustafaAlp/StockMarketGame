#!/usr/bin/env python
"""
	This module includes Gold class which is a subclass of the Item class.

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
class Gold(Item):
	"""
		subclass Gold derived from Item superclass

		purpose of the Gold class:
		to learn inheritance and polymorphizm in python
	"""
	def __init__(self):
		super(Gold, self).__init__()
		self._name = 'gold'
	
#
#	object property
#		
	def name():
	    doc = "The name property, keeps name of the Item and can't be changed"
	    def fget(self):
	        return self._name
	    return locals()
	name = property(**name())

#
#	object static method
#		
	@staticmethod
	def setWorth():
		"""changes worth of Gold items"""
		Gold._worth = ra.randint(18, 38)

#
#	object static method
#		
	@staticmethod
	def worth():
		"""@return worth of Gold items"""	
		return Gold._worth
