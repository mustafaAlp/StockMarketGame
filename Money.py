#!/usr/bin/env python
"""
	This module includes Money class which is a subclass of the Item class.

	Purpose of the module to learn how to use 
	inheritance and polymorphizm in the python. 
	Its free to use and change.

	writen by Mustafa ALP.
	16.06.2015
"""
from Item import Item

#		
#		
#	object		
#		
#		
class Money(Item):
	"""
		subclass Money derived from Item superclass

		purpose of the Money class:
		to learn inheritance and polymorphizm in python
	"""
	def __init__(self):
		super(Money, self).__init__()
		Money._worth = 1
		self._name = 'money'

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
		"""this medhot not much usefull"""
		Money._worth = 1 

