from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
from kivy.core.window import Window
import sys

class Player (Widget):
    def move(self):
        pass

class PongBall(Widget):

    # velocity of the ball on x and y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # referencelist property so we can use ball.velocity as
    # a shorthand, just like e.g. w.pos for w.x and w.y
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    print("Initial Position: ", velocity_x, velocity_y)
 
    def move(self):
#        print("Before...", self.pos[0], self.pos[1])
        print("Position: ", *self.velocity)
        self.pos = Vector(*self.velocity) + self.pos
#        print("After...", self.pos[0], self.pos[1])

class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    player1_score = ObjectProperty(None)
    player2_score = ObjectProperty(None)
    player1_score_value = 0
    player2_score_value = 0
    timer_running = False
    timer = None

    def __init__(self, **kwargs):
        super(PongGame, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)    

    def serve_ball(self):
        self.ball.center = self.center
        self.ball.velocity = Vector(6, 0).rotate(randint(0, 360))
        self.player1.center = Vector(0,350)
        self.player2.center = Vector(800,300)
        print("Serve", self.center[0], self.center[1])
  
    def update(self, dt):
        print("Being called")
        # call ball.move and other stuff
        self.ball.move()
        # Check if ball has touched the player 1
        if(not (self.ball.center_y < self.player1.top and self.ball.center_y > self.player1.y) and self.ball.x < 0):
            self.player2_score_value += 1
            self.player2_score.text = str(self.player2_score_value)
            self.timer.cancel()
            self.timer_running = False
            self.serve_ball()

       # Check if ball has touched the player 2
        if(not (self.ball.center_y < self.player2.top and self.ball.center_y > self.player2.y) and self.ball.right > self.width):
            self.player1_score_value += 1
            self.player1_score.text = str(self.player1_score_value)
            self.timer.cancel()
            self.timer_running = False
            self.serve_ball()
    
        # bounce off top and bottom
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        # bounce off left and right
        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1
    # ``move`` function will move the ball one step. This
    #  will be called in equal intervals to animate the ball
        return True


    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
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
        else:
            if(self.timer_running == False):
                self.timer = Clock.schedule_interval(self.update, 1.0/60.0)
                self.timer_running = True


class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
#        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    PongApp().run()