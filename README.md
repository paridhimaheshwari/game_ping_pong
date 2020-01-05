# Ping Pong

# Pre-requisites
This program would need Kivy library to be used. Follow the instructions available at the following location:

* [Installation of Kivy](https://kivy.org/doc/stable/installation/installation-windows.html)

It has been tested with Python 3.x version.

# Developers

* Paridhi Maheshwari
* Aarushi Phulre

# Credits
Kivy library and object oriented programing is new to us. We started our learning from the tutorial available from:
* [Pong Game Tutorial](https://kivy.org/doc/stable/tutorials/pong.html)


# Features - Available

Following is achieved in the code so far:
* Supports two players with moving bats for each player at the edge of the table
1. Use 'W', 'S' to move the left side bat up and down.
2. Use Down and Up arrow keys to move the right bat
* Pause and Start of the game
* Scoring for the game
3. Capture name of the players
4. Declaring the winner
5. Limiting the game to 2 scores for demo, which can be configured programmatically

# Features - Backlog

* Splash screen for 3 seconds, showing the name of the game
* Title for the name of game
* Background for the table to capture air-hockey
* Voice feedback for ball hitting the edge and for win/lose
* Adding complexity with moving obstacles deviating the movement
* Reduce the random start span between 30 - 150 degrees.
* Hotkey to Pause, End, Reset the game
* Register player name and save it's winning score
* Show player score history

# Known problems

* Background for the widgets is not opaque and it confuses with the underlying screen content
* It does not have option to restart the game
* It does not give hint/instructions in the beginning on how to play
* Visual of bat and the actual batting surface are different
* It does not save history of scores

# Some key programming challenges faced

# Some key concepts used but were not studied

## Kivy Graphics Framework

Kivy is a graphics development framework, which helps in keeping code separate from the 
graphics objects. These objects can be easily be designed using a separate configuration
file with extension .ky. This file would contain root element and widgets. Widgets created
here should match the class definitions available in the code.

An important thing to remember here, code precedes this configuration file. So, if you have
a widget defined in configuration file, but ther is no class, it will give an error, xxx class
not found. Class defined in code, is extended from the Kivy General purpose classes or layouts.
These helps to do the basic work without writing any code. We can write code to shape the the 
graphics, add more objects in the code, or do the same for the given widget inside kivy file.

Another important learning here was, that every widget that we create has an embedded canvas
element which can be used to customize the look and feel through drawings of this canvas
using some standard instructions - rectangle, ellipse, line, color.

Within widget, embedded objects can be accessed inside code through ID. This Id first needs to
be declared in the respective object, then referred in the top level of the widget, which is then
referred in the code. All these variables should be initialised in the code using ObjectProperty(None)


## Class based development

With limited understanding on class, here is what we understood, class is collection of functions and variables.
Functions is a collection of program statements that can be invoked using a name. Now to invoke these functions,
one would need to call either through a "self" reference or through the object of the class. 

Object is the instantiation of class. It is similar to calling a function, but it results into a object variable.

Class __init__ method is invoked by default. It can invoke parent class constructor by using super().__init__.

These classes can be imported from other python file into our main file just like other import command.

All variables are defined inside the class and are accessed within the methods using ```self.variable```. Same thing
applies to methods invocation as well.


## Github to manage our code

We ran into issues of losing the working code while experimenting with various things. Here we learnt few basics of git,
where it can version our code. Following are the main commands, used by us:

* ```git init .```
* ```git add file```
* ```git checiout master```
* ```git commit```
* ```git status -s```
* ```git log```

We could retrieve few times previous version of code, by using ```git checkout <hashcode of last commit>```

## Code split across more than one file

Using basic functionality of import and classes, we could achieve this. This helped us to make our code little bit
modular.

## Packaging pythong code into executable

## Passing functions as parameters for callbacks

