#Fishing
--------------------

Prints colourful fish

-----------------------

First ```pip install colorama```

From command line:

```
python3 fishing.py
```

will print a random coloured fish.


Or from interpreter:

```
from fishing import fish

fish()
```

fish takes optional parameters index (0 or 1) for a left or right facing fish and colour (a string). e.g.

```
fish(0, 'green')

fish(colour='red')

fish(index=1)
```

Currently available colours are (case insensitive): RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE

If an unknown colour or a non-colour string is provided, a random one will be chosen.

