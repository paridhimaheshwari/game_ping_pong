#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 21:41:46 2020

@author: paridhimaheshwari
""" 

"""Connecting to mysql and find score of player1"""

#%%
import mysql.connector

mydb = None
mycursor = None

def connectToMysql():
  global mycursor, mydb
  mydb = mysql.connector.connect(host='localhost', user='root', passwd='', database='pong')
  mycursor = mydb.cursor()

def getAllResults():  
   global mycursor
   mycursor.execute('select g.gameid, p1.playerName as player1Name,g.p1score,  p2.playerName as player2Name, g.p2score from games g left join players p1 on p1.playerid=g.playerid1 left join players p2 on p2.playerid = g.playerid2 ;')
   games = mycursor.fetchall()
   for game in games:
       print(game)

def initiateGame(playerId1, playerId2):
    global mycursor
    mycursor.execute('insert into games (gameid='+2)

def updateWinCount(playerId):
    mycursor.execute()

def addNewPlayer(name):
    mycursor.execute()

def findTotalScore(playerId):
    mycursor.execute()

def findTotalGames(playerId):
    mycursor.execute()
     
def findTotalWins(playerId):
    mycursor.execute()
    
connectToMysql()
print(mydb, mycursor)
getAllResults()


