``python-eco is a bridge to the ECO Template compiler.``

Description
===========
python-eco is a bridge to the ECO Template compiler.

Requirements
============
* CoffeeScript

Features
========


Setup
=====

.. highlight:: bash

::

    $ pip install eco


**Python Eco**
~~~~~~~~~~~~~~~

.. highlight:: python

::

    import eco

    eco.compile(open("template.eco"))
    # => "function(...) {...}"

    context = eco.context_for("Hello <%= @name %>")
    context.call("render", {"name": "Sam"})
    # > u'Hello Sam'

    eco.render("Hello <%= @name %>", name="world")
    # > u'Hello world'


History
========
0.9 (2012-06-17)
~~~~~~~~~~~~~~~~~
* first release

License
=======
MIT License
