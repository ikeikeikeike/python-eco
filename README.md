Python Eco
===========


Python Eco is a bridge to the [Eco](https://github.com/sstephenson/eco) (CoffeeScript Template) compiler.

```python
import eco

eco.compile(open("template.eco"))
# Out: u"function(...) {...}"

context = eco.context_for("Hello <%= @name %>")
context.call("render", {"name": "Sam"})
# Out: u'Hello Sam'

eco.render("Hello <%= @name %>", name="world")
# Out: u'Hello world'
```

Setup
-----
```bash
$ pip install eco
```

History
========
0.9 (2012-06-17)
-----------------
* first release

License
========
MIT License
