"""
	This module includes methods of StockMarket game which are shared
	by more than one file.

	Purpose of the module to write a driver for Item superclass
	and subclasses of the Item. 
	Its free to use and change.

	writen by Mustafa ALP.
	16.06.2015
"""

import os
from Money import Money
from Dollar import Dollar
from Gold import Gold
from Bond import Bond


#
#	method
#
def importItems():
	"""method imports all subclasses of the Item class """
	from Money import Money
	from Dollar import Dollar
	from Gold import Gold
	from Bond import Bond




#
#	method
#
def clear():
	"""	method clears the std output"""	
	if os.name=="posix":
		os.system("clear")
	else:
		os.system("cls")	


#
#	method
#
def setItemValue():
	"""method sets worths of all Items"""
	Money.setWorth()
	Dollar.setWorth()
	Gold.setWorth()
	Bond.setWorth()

#
#	method
#
def printPrices(user):
	"""method prints all Items worth to std output"""
	
	print """\titem prices  :\n"""

	for item in user.itemList:
		if item.name != 'money':
			print "\t%s\t : %d"%(item.name, item.worth())	

