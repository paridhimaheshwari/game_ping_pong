---
layout: default
title: Main App
---

# PongGame.py

## Initialising Game

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

## PongGame object initialization

This is ```__init__``` method. It initializes parent class, binds keyboard for user interaction, cleans up initial board
from other objects, leaving behin splash and ball.

It also initiates timer, that runs once to kill the spash shown after 3 seconds.

```python
def __init__(self, **kwargs):
        super(PongGame, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self.winning_splash_object = self.winning_splash.__self__
        self.clear_widgets(children = [self.player1_score, self.player2_score, self.player1_name, self.player2_name, self.player1, self.player2, self.winning_splash])
        self.splash_timer = Clock.schedule_once(self.remove_splash, 3)
```


## Initializing Ball

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

## Initializing Keyboard for player interaction

This is implemented through method ```_on_keyboard_down```. It is initialized as part of PongGame's ```__init__``` method.

```python
self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
```

In keyboard handling, right player movements are handled through arrow keys, left player movements are handled through 
'w' and 's' keys. Movement changes the position of the player1 or player2 position by 20 points. Also, it calculates,
if it touches the upper or bottom side of the board, it will stop.

'q' is reserved for exiting the game. It also exits with 'Esc' key as well.

default actions, invokes the method ```invokeUserNamesInput``` checks for UserNamesInput form or initialization of long running timer that runs the game.

```python
    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print("Flags are: ", self.timer_running, self.player_names_entered, self.winning_player, self.flag_game_initialised)
        if keycode[1] == 'w':
            self.player1.center_y += 20
            if(self.player1.top > self.height):
                self.player1.top -= 20
        elif keycode[1] == 's':
            self.player1.center_y -= 20
            if(self.player1.y < 0):
                self.player1.y += 20
        elif keycode[1] == 'up':
            self.player2.center_y += 20
            if(self.player2.top > self.height):
                self.player2.top -= 20
        elif keycode[1] == 'down':
            self.player2.center_y -= 20
            if(self.player2.y < 0):
                self.player2.y += 20
        elif keycode[1] == 'q' or keycode[1] == 'Q':
            sys.exit()
        else:
            self.invokeUserNamesInput()
```

```invokeUserNamesInput``` performs following things:

* checks if game is initialize. (```flag_game_initialised```)
* checks if timer was already running and player names are provided
* if above conditions are satisfied than only initiate the timer which has embedded method ```update```
* Sets the ```timer_running``` flag

```python
def invokeUserNamesInput(self):
            if(self.flag_game_initialised):
                if(self.timer_running == False and self.player_names_entered == False):
                    self.askPlayerNames()
                elif(self.timer_running == False and self.winning_player == None):
                    self.timer = Clock.schedule_interval(self.update, 1.0/60.0)
                    self.timer_running = True
```

## Movement of ball and THE AIR HOCKEY GAME

This is handled through ```update``` method of this class.

```python
def update(self, dt):
        # call ball.move and other stuff
        self.pong_ball.move()
        # Check if ball has touched the player 1
        if(not (self.pong_ball.center_y < self.player1.top and self.pong_ball.center_y > self.player1.y) and self.pong_ball.x < 0):
            self.player2_score_value += 1
            self.player2_score.text = str(self.player2_score_value)
            if(self.player2_score_value >= self.MAX_SCORE):
                self.winning_player = self.player2_name.text
            self.timer.cancel()
            self.timer_running = False
            self.serve_ball()
```
Following is done in this code:

* Moves the ball, that basically would change the location of ball in the direction set initially (explained later in the PongBall.py)
* checks for the boundaries - top, bottom and bounce back the ball
* Checks for the left and right boundaries. Compares it with the location of player1 and player2. If it collides
it bounces back, else it stops the game, updates the scores and serves the ball again

```python
        # bounce off top and bottom
        if (self.pong_ball.y < 0) or (self.pong_ball.top > self.height):
            self.pong_ball.velocity_y *= -1

        # bounce off left and right
        if (self.pong_ball.x < 0) or (self.pong_ball.right > self.width):
            self.pong_ball.velocity_x *= -1
```

* As the score changes, it is decided and saved, the winning player. It works as a flag (```winning_player```)

Similar code repeats once more to capture the second check:

```python
       # Check if pong_ball has touched the player 2
        if(not (self.pong_ball.center_y < self.player2.top and self.pong_ball.center_y > self.player2.y) and self.pong_ball.right > self.width):
            self.player1_score_value += 1
            self.player1_score.text = str(self.player1_score_value)
            if(self.player1_score_value >= self.MAX_SCORE):
                self.winning_player = self.player1_name.text
            self.timer.cancel()
            self.timer_running = False
            self.serve_ball()
```

Next comes, is to show Winning Team, if ```winning_player``` flag is set.

## Variables initialization (Class attributes)

Following attributes are used inside the class, and initialized.

```python
MAX_SCORE = 2
    flag_game_initialised = False
    pong_ball = ObjectProperty(None)
    winning_player = None
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    player1_score = ObjectProperty(None)
    player2_score = ObjectProperty(None)
    player1_score_value = 0
    player1_name = ObjectProperty(None)
    player2_name = ObjectProperty(None)
    player2_score_value = 0
    player_names_entered = False
    winning_splash = ObjectProperty(None)
    winning_splash_object = ObjectProperty(None)
    p1_name = "Paridhi"
    p2_name = "Aarushi"
    unInputForm = ObjectProperty(None)
    splash_screen = ObjectProperty(None)
    timer_running = False
    timer = None
```
