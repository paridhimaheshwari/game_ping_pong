---
layout: default
title: Support
category: code-walkthrough
---

# PongBall.py
## Initialize
Initializes the widget attributes for this widget (ball)

```python
   velocity_x = NumericProperty(0)
   velocity_y = NumericProperty(0)
   velocity = ReferenceListProperty(velocity_x, velocity_y)
```

## Moving the ball

This file has got one class and only one method within it. It is key to defining velocity of the ball.

```python
def move(self):
        self.pos = Vector(*self.velocity) + self.pos
```

Note here ```*self.velocity```. This was set in the main class as per following code:

```python
self.pong_ball.velocity = Vector(6, 0).rotate(angle)
```

which means, move with every step by 6 points.

# UserNamesInputForm.py

## Initialization

Initializes the variables used in getting usernames from players. Note the cb_ functions which are
callback methods, that this widget will use to feed the information back to the invoking entity.

```python
def __init__(self, caller, cb_names_received, cb_names_not_received):
        super().__init__()
        self.caller = caller
        self.cb_names_not_received = cb_names_not_received
        self.cb_names_received = cb_names_received
```

## Save Names received

Validates in the User Names input diaglog box, if there is some value entered and invokes
```cb_names_received``` method with the names provided.

Other method ```cb_names_not_received``` is not used.

```python
 def save_names(self):
        if(self.p1_name != '' and self.p2_name != ''):
            self.cb_names_received(self.caller,(self.p1_name.text, self.p2_name.text))
        return
```

# Player.py

This is only to instantiate object and used by kivy file to further extend.

# Navigate to other items
<ul>
    {% for doc in site.pages %}
      {% if doc.category == "code-walkthrough" and doc.url != page.url%}
        <li><a class="page-link" href="{{site.url}}{{site.baseurl}}{{doc.url}}">{{ doc.title }}</a></li>

      {% endif %}
    {% endfor %}
</ul>