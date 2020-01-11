---
layout: default
title: Code Walkthrough
category: code-walkthrough
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
      {% if doc.category == "code-walkthrough" and doc.url != page.url%}
        <li><a class="page-link" href="{{site.url}}{{site.baseurl}}{{doc.url}}">{{ doc.title }}</a></li>

      {% endif %}
    {% endfor %}
</ul>