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
    ''' Create a new game in database with win scores of both players set to 0 '''
    global mycursor, mydb
    mycursor.execute('select max(gameid) from games;')
    gameids = mycursor.fetchone()
    newGameId = gameids[0]+1
    mycursor.execute("insert into games (gameid, playerid1, playerid2, p1score, p2score) values("+str(newGameId) +", "+str(playerId1)+", "+str(playerId2)+", 0, 0 );")
    mydb.commit()
    return newGameId
    
    

def updateWinCount(gameid, playerId):
    ''' Increment the count of the win score for the player Id, after matching with player 1 or player2'''
    global mycursor, mydb
    mycursor.execute('select playerid1, playerid2 from games where gameid='+str(gameid)+';')
    game_players = mycursor.fetchone()
    if(game_players[0] == playerId):
        mycursor.execute('update games set p1score=p1score+1 where (gameid='+str(gameid)+');')
    elif (game_players[1] == playerId):
        mycursor.execute('update games set p2score=p2score+1 where (gameid='+str(gameid)+');')
    else:
        print('Some error in playerId')
        return
    mydb.commit()

def addNewPlayer(name):
    ''' Check if name is not existing in the players, then add'''   
    global mycursor, mydb
    
    mycursor.execute("select playerid, playerName from players where playerName='"+name+"';")
    players = mycursor.fetchone()
    if(players is not None):
        return players[0]
    else:
        mycursor.execute("select max(playerid) from players;")
        playerids = mycursor.fetchone()
        newPlayerId = playerids[0]+1
        mycursor.execute("insert into players (playerid, playerName) values("+str(newPlayerId)+", '"+name+"');")
        mydb.commit()
        return newPlayerId

def findTotalScore(playerId):
    ''' Total win games x 10'''
    
    #find if player has played as p1 and won or player has played as p2 and won
    mycursor.execute("select sum(p1score) from games where playerid1="+str(playerId)+";")
    score1 = mycursor.fetchone()
    mycursor.execute("select sum(p2score) from games where playerid2="+str(playerId)+";")
    score2 = mycursor.fetchone()
    return (score1[0] + score2[0])*10

def findTotalWins(playerId):
    print("findTotalWins:Player:",playerId)
    mycursor.execute("select count(p1score) from games where playerid1="+str(playerId)+" and p1score > p2score;")
    wins1 = mycursor.fetchone()
    mycursor.execute("select count(p2score) from games where playerid2="+str(playerId)+" and p2score > p1score;")
    wins2 = mycursor.fetchone()
    print("findTotalWins:Wins: ", wins1[0] + wins2[0])
    return (wins1[0] + wins2[0])
     
def findTotalGames(playerId):
    print("findTotalGames:Player:",playerId)
    mycursor.execute("select count(p1score) from games where playerid1="+str(playerId)+";")
    games1 = mycursor.fetchone()
    mycursor.execute("select count(p2score) from games where playerid2="+str(playerId)+";")
    games2 = mycursor.fetchone()
    print("findTotalGames: ", games1[0] + games2[0])
    return (games1[0] + games2[0])
    
connectToMysql()
'''
print("All the games status before starting of")
getAllResults()
print("Starting a game")
gid = initiateGame(2,3)
print("New game id: ", gid)
print("All game results including the new one")
getAllResults()
print("Let the player 1 = 1 win")
updateWinCount(gid, 3)
print("All game results including the new one")
getAllResults()
print("Let the player 1 = 1 win")
updateWinCount(gid, 3)
print("All game results including the new one")
getAllResults()
print("Let the player 1 = 1 win")
updateWinCount(gid, 2)
print("All game results including the new one")
getAllResults()
print("Let the player 1 = 3 win")
updateWinCount(gid, 3)
print("All game results including the new one")
getAllResults()

print("Total wins for player 1")
print(findTotalWins(2), findTotalWins(3))
print(findTotalGames(2), findTotalGames(3))
print(findTotalScore(2), findTotalScore(3))
'''


