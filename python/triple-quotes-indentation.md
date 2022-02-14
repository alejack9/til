# Triple Quotes Indentation

The default python indentation in triple quotes (`'''...'''`) strings can be ignored using `textwrap.dedent` function.

Just wrap the string into the function and it will take care of the rest!

```python
from textwrap import dedent

'''\
  Hello World!''' # Output: "  Hello World!"
dedent('''\
  Hello World!''') # Output: "Hello World!"
```

[Source](https://stackoverflow.com/questions/1412374/how-to-remove-extra-indentation-of-python-triple-quoted-multi-line-strings)

[Documentation](https://docs.python.org/3/library/textwrap.html#textwrap.dedent)