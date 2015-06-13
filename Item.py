#!/usr/bin/env python
"""
	This module includes Item class which is a superclass.

	Purpose of the module to learn how to use
	inheritance and polymorphizm in the python.
	Its free to use and change.

	writen by Mustafa ALP.
	16.06.2015
"""

#
#
#	object
#
#
class Item(object):
	"""
		Item superclass
		purpose of the Item class:
		to learn inheritance and polymorphizm in python
		Item class is an abstaract baseclass
	"""

	# @property "_worth" will be used as a static variable
	# this is why it isn't a property
	_worth = 0

#
#	object method
#
	def __init__(self):
		self._quantity = 0

#
#	object property
#
	def quantity():
	    doc = "The quantity property, keeps an Items quantity"

	    def fget(self):
	        return self._quantity

	    def fset(self, value):
	        self._quantity = value

	    return locals()

	quantity = property(**quantity())


#
#	object method
#
	def totalWorth(self):
		"""@return multiply of worth and quantity properties"""
		return self._quantity * self._worth
