---
layout: default
title: Code Walkthrough
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

## Navigate to other items
<ul>
    {% for doc in site.pages %}
      {% if doc.category == "code-walkthrough" %}
        <li><a href="{{ doc.url }}">{{ doc.title }}</a></li>
      {% endif %}
    {% endfor %}
</ul>