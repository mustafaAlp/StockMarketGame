#!/usr/bin/env python
"""
	This module includes StockMarket game and methods.

	Purpose of the module to write a driver for Item superclass
	and subclasses of the Item. 
	Its free to use and change.

	writen by Mustafa ALP.
	16.06.2015
"""
import re

from SharedMethodsOfStockMarket import *
from User import User
from DataBase import *

importItems()


#
#	method:
#
def getUserName():
	"""	
		Asks number of players and takes names each one of them
		@return list of player names 
	"""

	try:
		userNum=int(raw_input("\n\tenter nuber of players (exp -> 2)\n\t-> "))
	except ValueError:
		clear()
		print "\n\tinvalid input, please try again"
		return getUserName() 

	nameList=[]
	for i in range(0,userNum) :
		name=raw_input("\n\n\t enter %d. players name\n\t-> "%(i+1) )
		nameList.append(name)
		clear()
	return nameList

#
#	method
#
def setPlayer(nameList):
	"""
		@paramater nameList: the list which keeps user names as string

		method creates a user object list with strings from paramater named nameList

		@return a list which includes user object instances
	"""
	userList=[]

	for i in nameList:
		newPlayer=User(i)
		userList.append(newPlayer)

	return userList


#
#	method
#
def result(playerList):
	"""
		@paramater playerList: list which keeps players

		method calculates all players net worth, finds the winner
		and sands players to database 
	"""
	for i in playerList:
		i.sellAssets()

	sort_players(playerList)
		
	clear()				
	print "\n\tthe winner is %s \n\n"%playerList[0].name

	for i in playerList:
		print "\tplayer %s, net worth : %d "%(i.name, i.itemList[0].quantity)
		
	gameData = handleData(playerList)
	saveHighScores(gameData)


#
#	method
#
def playStockMarket():
	"""
		method offers users two choose:
			play the game
			or
			display the High scores
	"""
	clear()
	
	print "\n\n\tplease always use lowercase characters\n\n\n"
	
	choose = raw_input("""\tto play the game type 'start'
		\n\tto see the high scores type 'scores'
		\n\tto terminate programme type 'exit'
		\n\t -> """)

	clear()

	if re.search("start", choose):		
		player_names = getUserName()
		users=setPlayer(player_names)
		season(users)
	elif re.search("scores", choose):
		displayHighscores()
	elif re.search("exit", choose):
		clear()
		pass
	else:
		playStockMarket()


#
#	method
#
def season(playerList):
	"""
		@paramater  playerList: list keeps players 

		season method represents a complete play of the game
		every week item worths chages
		every player has one turn for each week.
		at the and of the season, method calculates players networths   
	"""
	for j in range(1,12):
		setItemValue()
		for k in range(len(playerList)):
			clear()
			while 1:
				print "\n\t%s. week,  %s's turn "%(j,playerList[k].name)
				playerList[k].print_asset()

				printPrices(playerList[0])
				choose=raw_input("""\n\tchoose the operation  \n\n\tbuy \
					\n\tsell\n\tpass\n\t-> """)

				clear()
				if choose=="buy":
					playerList[k].buy()
				elif choose=="sell":
					playerList[k].sell()
				elif choose=="pass":
					break
				else:
					clear()
					print "\n\tinvalid input, please try again"			
	result(playerList)	



	
#
#	method
#
def sort_players(playerList):
	"""	
		method sorts the playerList by using selection sort algorithm
		
		@paramater playerList	:	list which keeps scores of the players who just played the game.
		@return : list which keep new version of sorted high scores  
	"""
	for i in xrange(0, len(playerList)):
		for j in xrange(i, len(playerList)):

			if playerList[i].itemList[0].quantity < playerList[j].itemList[0].quantity:
				temp = playerList[j]
				playerList[j] = playerList[i]
				playerList[i] = temp
				




	
#
#	method
#
def handleData(playerList):
	"""
		method prepares data to write to the database

		@paramater playerList: the list which includes User objects
		@return a list which includes tuples to write database
	"""
	gameData = list()
	counter = 0

	for player in playerList:
		if counter < 20:
				gameData.append( (player.name, player.itemList[0].quantity) )	
		counter += 1

	return gameData
	
