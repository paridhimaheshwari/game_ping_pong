---
layout: default
title: Blogging Like a Hacker
---
# Code Walkthrough

There are following source code files in our code:

## Python code

* ```PongGame.py```
* ```PongBall.py```
* ```UserNameInputForm.py```
* ```Player.py```

## Kivy Graphic Objects files

* ```pong.kv```
* ```usernames.kv```

# Functionality by each file

## PongGame.py

### Initialising Game

It has two classes:

* PongGame
* PongApp

Program starts from

```
PongApp().run()
```

This line creates object of the class ```PongApp```. ```PongApp``` is derived from Kivy generic class ```App```.
This base class (App) provides the basic building blocks for creating the graphical application for us. To get
application running, it provides method - ```run```, which is invoked here.

As ```App``` starts to run, it invokes the overloaded method - ```build```, where we are supposed to initialize our
graphical objects and their functions. Following is done:

* Load the kivy graphical object definition files

```python
def load_kivy_files(self):
        Builder.load_file('usernames.kv')
```
* Create instance of ```PongGame```
* Initialize ball through method of ```PongGame``` i.e. ```serve_ball```
* return this instance to the main ```App```


```python
def build(self):
    self.load_kivy_files()
    game = PongGame()
    game.serve_ball()
    return game
```

### Initializing Ball

In last section serve_ball was referred. It performs a very important function to initialize ball position,
movement of direction:

```python
def serve_ball(self):
        self.pong_ball.center = self.center
        angle = randint(0, 360-120)
        if(angle > 60):
            angle+=60
        if(angle > 240):
            angle+=60
        self.pong_ball.velocity = Vector(6, 0).rotate(angle)
        self.player1.center = Vector(0,350)
        self.player2.center = Vector(800,350)
        print("Serve", self.center[0], self.center[1], angle)
```        

In the above, note the setting up of angle. It is important to avoid ball to move in a direction which is 
very close to the vertical axis as it will slows down the speed at which ball will travel from left to right
or vice-versa. ```velocity``` attribute of ```pong_ball``` is initialized at x = 6, y = 0. That means it
is a straight line from origin on x-axis, 6 points length. and when we rotate for it's initial movement,
it is allowed to be 60 degrees up or down on either sides. If it becomes 90 degrees, as an example, it will 
keep oscillating on the same place.

Two player objects are created through kivy file, and their position is initialized here.

First argument in all the program maps to x-axis or width or row. Second argument maps to y-axis or height or column.

