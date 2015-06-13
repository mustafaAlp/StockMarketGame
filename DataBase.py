#!/usr/bin/env python
"""
	This module includes dataBase methods for StockMarket game.

	Purpose of the module to learn how to use sqlite3 in python. 
	Its free to use and change.

	writen by Mustafa ALP.
	16.06.2015
"""
import os
import sqlite3 as sql

#
#	method
#
def displayHighscores():
	""" method prints records from database to std output """

	dbFile = "StockMarket.db"	

	if os.path.isfile(dbFile):
		db = sql.connect(dbFile)
		im = db.cursor()

		im.execute("SELECT * FROM high_score ORDER BY score DESC")
		data = im.fetchall()

		
		print "\n\n\tPLAYER\t\t SCORE\n\t-----------------------"
		
		for player in data:
			print "\t%s\t\t : %s"%(player[0], player[1])
		print "\n\n"


	else:
		clear()
		print "\n\n\tthere is no record in the database\n\n"


#
#	method
#	
def saveHighScores(playerList):
	"""
		@paramater playerList : a list of tuples each keeps player info

		if there is records on dataBase :
			methdod adds new records to table.
			
			if there is more record than 20
				deletes lowest scores

		if there is no records on dataBase :
			 method creates a database and a table on the database
			 		saves playerList to database
	"""
			
	dbFile = "StockMarket.db"	

	if os.path.isfile(dbFile):
		db = sql.connect(dbFile)
		im = db.cursor()

		for player in playerList:
			im.execute("INSERT INTO high_score VALUES(?, ?)" , player)			

		im.execute("SELECT * FROM high_score ORDER BY score DESC")
		data = im.fetchall()

		counter = 0
		for player in data:
			if counter > 19:
				im.execute("DELETE FROM high_score WHERE player = ? AND score = ?" ,player)
			counter += 1



	else:	#if there is no database file					
		db = sql.connect(dbFile)
		im = db.cursor()

		im.execute("CREATE TABLE high_score(player, score)")

		for player in playerList:
			im.execute("INSERT INTO high_score VALUES(?, ?)" ,player)
	db.commit()

