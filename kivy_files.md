---
layout: default
title: Kivy
category: code-walkthrough
---

# pong.kv

Main Widet here is ```PongGame```. This comprise of 

* Canvas 
* Label (Player 1 score) - ```player1_score_one```
* Label (Player 1 Name) - ```player1_name```
* Label (Player 2 score) - ```player2_score_two```
* Label (Player 2 Name) - ```player2_name```
* PongBall -  ```pong_ball```
* Player1 Bat - ```player_x```
* Player2 Bat - ```player_y```
* Splash Screen (Welcome) - ```splash_screen```
* Splash Screen (Winning) - ```winning_splash```

# usernames.kv

This is the dialog box that pops at the start of game to input player names. It has got 
following widgets:

* Dialog Box with Canvas setting
 + UserInput Box for player 1
   - Label
   - TextInput - ```p1_name``` 
 + UserInput Box for player 2
   - Label
   - TextInput - ```p2_name``` 
 + Controls Box
   - Button for save ```btn_save```
   - Button for cancel ```btn_cancel```