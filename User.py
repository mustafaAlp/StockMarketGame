#!/usr/bin/env python
"""
	This module includes User class.

	Purpose of the module to write a driver for Item superclass
	and subclasses of the Item. 
	Its free to use and change.

	writen by Mustafa ALP.
	16.06.2015	
"""
import re

from SharedMethodsOfStockMarket import *


importItems()


#
#	Object 
#
class User(object):
	"""purpose of User class:
			to create usable programme for Item superclass and 
			all subclasses of Item

		User class should be initialized with a string 
	"""
	
	#
	#	object constructor
	#
	def __init__(self,name):
		"""
		@parameter name: string will be used to initialize name property

		"""
		self._name = name
		self.itemList = []
		self.itemList.append(Money())
		self.itemList.append(Dollar())
		self.itemList.append(Gold())
		self.itemList.append(Bond())

		self.itemList[0].quantity = 1000

#
#	object property
#					
	def name():
	    doc = "The name property, keeps name of the user"
	    def fget(self):
	        return self._name
	    def fset(self, value):
	        self._name = value
	    return locals()
	name = property(**name())	



#
#	object method
#		
	def buy(self):
		"""
			User object member method buy:
				method takes no parameter
				method asks user to what item users would like to buy
				user have to use lower case characters.
				user have to start with a name of an item, string lenght isn't important
		"""
		printPrices(User(""))			
		choose=raw_input("""\n\ttype name of the item you want to buy (exp -> gold )\
		\n\ttype 'cancel' to get out from this menu\n\n\t-> """)		

		for item in self.itemList:
			if choose.startswith(item.name):
				self.buy_item(choose, item)
				clear()
				return 
		if re.search("cancel", choose):
			clear()			
			return
		else:	
			clear()
			print "\n\tinvalid input, please try again\n"
			self.buy()


#
#	object method
#		
	def buy_item(self, choose, item):
		"""
			@parameter choose	: string which keeps order of the player
			@parameter item 	: the Item object which player would like to buy	

			User object member method buy_item:
				if type of the item is Money method calls buy() method again

				if choose string includes 'max' word method automatically buys maximum 
					quantity of item

				method asks user to what quantity of item user would like to buy				
				if user orders more than maximum, method buys maximum				
		"""
		if re.search("money", item.name):
			clear()
			self.buy()
			return

		maximum = self.itemList[0].quantity/item.worth()

		if re.search("max", choose):
			self.itemList[0].quantity = self.itemList[0].quantity - item.worth()*maximum
			item.quantity = item.quantity + maximum
			
		else:
			try:
				howmany=int(raw_input("\n\thow many %s you want to buy (max:%d)\n\t-> "%(item.name, maximum)))
			except ValueError:
				clear()
				print "\n\tinvalid input, please try again"
				self.buy_item(choose, item)
				return

			cond1 = howmany<=maximum
			cond2 = howmany>=0
			if  cond1 and cond2 :
				self.itemList[0].quantity= self.itemList[0].quantity - item.worth()*howmany
				item.quantity = item.quantity + howmany
			elif not cond1 :
				self.itemList[0].quantity= self.itemList[0].quantity - item.worth()*maximum
				item.quantity = item.quantity + maximum


#
#	object method
#		
	def sell(self):
		"""
			User object member method sell:
				method takes no parameter
				method asks user to what item users would like to sell
				user have to use lower case characters.
				user have to start with a name of an item, string lenght isn't important
		"""
		self.print_asset()
		choose=raw_input("""\n\ttype name of the item you want to sell (exp -> gold )\
		\n\ttype 'cancel' to get out from this menu\n\n\t-> """)
		clear()

		for item in self.itemList:
			if choose.startswith(item.name):
				self.sell_item(choose, item)
				clear()
				return

		if re.search("cancel", choose):
			clear()			
			return
		else:	
			clear()
			print "\n\tinvalid input, please try again\n"
			self.sell()



#
#	object method
#		
	def sell_item(self, choose, item):
		"""
			@parameter choose	: string which keeps order of the player
			@parameter item 	: the Item object which player would like to buy	

			User object member method sell_item:
				if type of the item is Money method calls sell() method again

				if choose string includes 'max' word method automatically buys maximum 
					quantity of item

				method asks user to what quantity of item user would like to buy				
				if user orders more than maximum, method buys maximum				
		"""
		if re.search("money", item.name):
			clear()
			self.sell()
			return 

		if re.search("max", choose):
			self.itemList[0].quantity = self.itemList[0].quantity + item.worth()*item.quantity
			item.quantity = item.quantity - item.quantity

		else:
			try:
				howmany=int(raw_input("\n\thow many %s you want to sell (max:%d)\n\t-> "%(item.name, item.quantity )))
			except ValueError:
				clear()
				print "\n\tinvalid input, please try again\n"
				self.sell_item(choose, item)
				return

			cond1 = howmany<=item.quantity
			cond2 = howmany>=0
			if  cond1 and  cond2:
					self.itemList[0].quantity= self.itemList[0].quantity + item.worth()*howmany
					item.quantity = item.quantity - howmany
			elif not cond1 :
				self.itemList[0].quantity= self.itemList[0].quantity + item.worth()*item.quantity
				item.quantity = item.quantity - item.quantity

#
#	object method
#		
	def print_asset(self):
		"""
			User object member method print_asset:
				method prints assets of the user to standart output
		"""
		print """\n\n\n\tassets of %s  :\n"""%(self.name)

		for item in self.itemList:
			print """\t%s\t : %d"""%(item.name, item.quantity)		

		print """\n\n\n"""

#
#	object method
#		
	def sellAssets(self):
		"""
			User object member method sellAssets:
				method converts all assets to Money with current worth of the Items
				this methond only helps to calculate results of the game
		"""
		for item in self.itemList:
			if item.name != 'money':
				self.itemList[0].quantity = self.itemList[0].quantity + item.totalWorth()
				item.quantity = 0




