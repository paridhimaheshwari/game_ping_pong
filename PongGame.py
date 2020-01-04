from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import sys
import PongBall
import Player


#PongGame is graphical widget, which is enhanced with our specific functions
# This looks for similar name in any of the kivy files, to initialize it's layout
# >>>>> Didn't understand, how come widget is appearing without any parent layout. Is Widget a layout?
# 
class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    player1_score = ObjectProperty(None)
    player2_score = ObjectProperty(None)
    player1_score_value = 0
    player2_score_value = 0
    player1_name_entered = False
    player2_name_entered = False

    timer_running = False
    timer = None

    def __init__(self, **kwargs):
        super(PongGame, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)    

    def askPlayerNames(self):
        userNamesInput = BoxLayout(orientation = 'vertical')

        userName1Input = BoxLayout(orientation = 'horizontal')
        l = Label(text='Player 1', size_hint=(1.0, 1.0), halign="right", valign="middle")
        l.bind(size=l.setter('text_size'))  
        userName1Input.add_widget(l)
        userName1Input.add_widget(TextInput(text='Hello World', multiline=False))
        userNamesInput.add_widget(userName1Input)

        userName2Input = BoxLayout(orientation = 'horizontal', size=(400,50))
        l = Label(text='Player 2', halign="right", valign="middle")
        l.bind(size=l.setter('text_size'))  
        userName2Input.add_widget(l)
        userName2Input.add_widget(TextInput(text='Hello World', multiline=False))
        userNamesInput.add_widget(userName2Input)
        userNamesInput.pos = (self.x/2 ,self.height/2)
        userNamesInput.size = (400, 80)
        self.add_widget(userNamesInput)
        
        return

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
        elif keycode[1] == 'q' or keycode[1] == 'Q':
            sys.exit()
        else:
            if(self.timer_running == False and self.player1_name_entered == False and self.player2_name_entered == False):
                self.askPlayerNames()
            elif(self.timer_running == False):
                self.timer = Clock.schedule_interval(self.update, 1.0/60.0)
                self.timer_running = True


class PongApp(App):

#Note that build has to return a layout, which in this case is a widget. This can be boxlayout, relative layout etc
    def build(self):
        game = PongGame()
        game.serve_ball()
#        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    PongApp().run()